from pathlib import Path

from forprint_accounting_registry_service.one_c_io.import_pipeline import (
    OneCImportPipelineStatus,
    OneCSandboxImportPipeline,
)
from forprint_accounting_registry_service.one_c_io.mapping import FieldMappingDefinition
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.types import FieldCriticality
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from sqlmodel import Session

FIXTURES = Path("tests/fixtures/one_c/exports")


def create_source(sanitized: bool = True, production_allowed: bool = False) -> OneCSandboxSource:
    return OneCSandboxSource(
        source_id="pipeline-source",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path=str(FIXTURES / "counterparties.json"),
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
        sanitized=sanitized,
        production_allowed=production_allowed,
    )


def run_pipeline(export_path: Path, source: OneCSandboxSource):
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)

    with Session(engine) as session:
        pipeline = OneCSandboxImportPipeline(session)
        return pipeline.run_file_export_import(
            source=source,
            export_path=export_path,
            mapping_definitions=[
                FieldMappingDefinition(source_field="Код", target_field="one_c_code"),
                FieldMappingDefinition(
                    source_field="ЄДРПОУ",
                    target_field="tax_id",
                    required=True,
                    criticality=FieldCriticality.CRITICAL,
                ),
            ],
            target_kind="counterparty_accounting_reference",
        )


def test_pipeline_runs_on_sanitized_json_fixture() -> None:
    result = run_pipeline(FIXTURES / "counterparties.json", create_source())

    assert result.raw_snapshot_count == 1
    assert result.staging_record_count == 1
    assert result.mapping_issue_count >= 1
    assert result.manual_review_required_count >= 1
    assert result.status == OneCImportPipelineStatus.BLOCKED_BY_MAPPING_ISSUES


def test_pipeline_runs_on_sanitized_csv_fixture() -> None:
    result = run_pipeline(FIXTURES / "counterparties.csv", create_source())

    assert result.raw_snapshot_count == 1
    assert result.staging_record_count == 1


def test_pipeline_returns_unsupported_source_for_unknown_format(tmp_path: Path) -> None:
    path = tmp_path / "export.bin"
    path.write_text("unknown", encoding="utf-8")

    result = run_pipeline(path, create_source())

    assert result.status == OneCImportPipelineStatus.UNSUPPORTED_SOURCE


def test_pipeline_refuses_unsanitized_source() -> None:
    result = run_pipeline(FIXTURES / "counterparties.json", create_source(sanitized=False))

    assert result.status == OneCImportPipelineStatus.FAILED


def test_pipeline_refuses_production_source() -> None:
    result = run_pipeline(
        FIXTURES / "counterparties.json",
        create_source(production_allowed=True),
    )

    assert result.status == OneCImportPipelineStatus.FAILED