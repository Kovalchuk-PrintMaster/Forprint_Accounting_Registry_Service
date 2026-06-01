# python scripts/one_c_run_import_pipeline.py

"""
Safe local OneC import pipeline smoke runner.

Default:
    in-memory storage, sanitized fixture only, no live 1C.
"""

from pathlib import Path

from forprint_accounting_registry_service.one_c_io.import_pipeline import (
    OneCSandboxImportPipeline,
)
from forprint_accounting_registry_service.one_c_io.mapping import FieldMappingDefinition
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from sqlmodel import Session


def run_pipeline() -> str:
    """Run pipeline against sanitized fixture."""
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)

    source = OneCSandboxSource(
        source_id="cli-source",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/exports/counterparties.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
        sanitized=True,
        production_allowed=False,
    )

    with Session(engine) as session:
        pipeline = OneCSandboxImportPipeline(session)
        result = pipeline.run_file_export_import(
            source=source,
            export_path=Path("tests/fixtures/one_c/exports/counterparties.json"),
            mapping_definitions=[
                FieldMappingDefinition(source_field="Код", target_field="one_c_code"),
                FieldMappingDefinition(source_field="Назва", target_field="name"),
            ],
            target_kind="counterparty_accounting_reference",
        )
        return result.status


def main() -> int:
    """CLI entrypoint."""
    print(f"Pipeline status: {run_pipeline()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())