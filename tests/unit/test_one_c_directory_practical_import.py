from pathlib import Path

from forprint_accounting_registry_service.one_c_io.directories import (
    OneCDirectoryExportPackage,
    OneCDirectoryItemSnapshot,
    OneCDirectoryKind,
    OneCDirectorySnapshot,
    build_directory_import_batch,
    directory_snapshot_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
)

FIXTURES = Path("tests/fixtures/one_c/exports")


def test_counterparty_directory_csv_fixture_imports_as_accounting_reference() -> None:
    result = parse_one_c_export_file(
        FIXTURES / "counterparties.csv",
        target_kind="counterparty_accounting_reference",
    )
    assert result.batch is not None

    snapshot = OneCDirectorySnapshot(
        snapshot_id="dir-csv-001",
        directory_kind=OneCDirectoryKind.COUNTERPARTY_ACCOUNTING_REFERENCES,
        source_name=result.batch.source_path,
        items=[
            OneCDirectoryItemSnapshot(
                item_id=row.raw_values["Код"],
                raw_payload=row.raw_values,
                normalized_payload={"one_c_code": row.raw_values["Код"]},
            )
            for row in result.batch.rows
        ],
    )

    batch = build_directory_import_batch(snapshot)
    staging = directory_snapshot_to_staging_records(snapshot)

    assert batch.items_count == 1
    assert staging[0].raw_payload["accounting_reference_only"] is True


def test_directory_export_remains_dry_run_and_manual_approval_required() -> None:
    package = OneCDirectoryExportPackage(
        package_id="directory-export",
        directory_kind=OneCDirectoryKind.NOMENCLATURE_ACCOUNTING_REFERENCES,
    )

    assert package.dry_run is True
    assert package.production_write_allowed is False
    assert package.manual_approval_required is True