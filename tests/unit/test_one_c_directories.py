from forprint_accounting_registry_service.one_c_io.directories import (
    OneCDirectoryExportPackage,
    OneCDirectoryItemSnapshot,
    OneCDirectoryKind,
    OneCDirectorySnapshot,
    build_directory_import_batch,
    directory_snapshot_to_staging_records,
)


def build_directory_snapshot() -> OneCDirectorySnapshot:
    return OneCDirectorySnapshot(
        snapshot_id="dir-snapshot-001",
        directory_kind=OneCDirectoryKind.COUNTERPARTY_ACCOUNTING_REFERENCES,
        source_name="sanitized_fixture",
        items=[
            OneCDirectoryItemSnapshot(
                item_id="one-c-counterparty-001",
                raw_payload={"Код": "000001", "Назва": "ТОВ Приклад"},
                normalized_payload={"one_c_code": "000001", "name": "ТОВ Приклад"},
            )
        ],
    )


def test_directory_snapshot_is_accounting_reference_only() -> None:
    snapshot = build_directory_snapshot()

    assert snapshot.production_allowed is False
    assert snapshot.sanitized is True
    assert snapshot.items[0].accounting_reference_only is True


def test_directory_import_batch_creates_staging_records() -> None:
    snapshot = build_directory_snapshot()

    batch = build_directory_import_batch(snapshot)
    records = directory_snapshot_to_staging_records(snapshot)

    assert batch.items_count == 1
    assert records[0].record_type.startswith("directory:")
    assert records[0].raw_payload["accounting_reference_only"] is True


def test_directory_export_package_is_dry_run_by_default() -> None:
    package = OneCDirectoryExportPackage(
        package_id="dir-export-001",
        directory_kind=OneCDirectoryKind.COUNTERPARTY_ACCOUNTING_REFERENCES,
    )

    assert package.dry_run is True
    assert package.production_write_allowed is False
    assert package.manual_approval_required is True