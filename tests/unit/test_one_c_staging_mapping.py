from forprint_accounting_registry_service.one_c_io.directories import (
    OneCDirectoryItemSnapshot,
    OneCDirectoryKind,
    OneCDirectorySnapshot,
)
from forprint_accounting_registry_service.one_c_io.discovery import (
    create_raw_extract_batch,
)
from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    MappingIssueType,
)
from forprint_accounting_registry_service.one_c_io.reports import (
    OneCReportCategory,
    OneCReportDefinition,
    OneCReportRequest,
    generate_report_snapshot_from_fixture,
)
from forprint_accounting_registry_service.one_c_io.staging import (
    apply_mapping_to_staging_payload,
    directory_import_to_staging_records,
    raw_extract_batch_to_staging_records,
    report_snapshot_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.types import FieldCriticality


def test_raw_extract_maps_to_staging() -> None:
    batch = create_raw_extract_batch(
        source_id="snapshot-001",
        source_name="fixture",
        table_name="Counterparties",
        records=[{"Код": "000001", "Unknown": "preserve"}],
    )

    records = raw_extract_batch_to_staging_records(batch)

    assert records[0].record_type == "raw_extract:Counterparties"
    assert records[0].raw_payload["record"]["Unknown"] == "preserve"


def test_directory_import_maps_to_staging() -> None:
    snapshot = OneCDirectorySnapshot(
        snapshot_id="dir-001",
        directory_kind=OneCDirectoryKind.NOMENCLATURE_ACCOUNTING_REFERENCES,
        source_name="fixture",
        items=[
            OneCDirectoryItemSnapshot(
                item_id="item-001",
                raw_payload={"Name": "Example"},
                normalized_payload={"name": "Example"},
            )
        ],
    )

    records = directory_import_to_staging_records(snapshot)

    assert records[0].raw_payload["accounting_reference_only"] is True


def test_report_snapshot_maps_to_staging() -> None:
    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="request-001",
        report_code=definition.report_code,
    )
    snapshot = generate_report_snapshot_from_fixture(
        snapshot_id="report-001",
        definition=definition,
        request=request,
        rows=[{"payment": "PAY-001"}],
    )

    records = report_snapshot_to_staging_records(snapshot)

    assert records[0].record_type.startswith("report:")
    assert records[0].raw_payload["accounting_only"] is True


def test_missing_critical_field_creates_mapping_issue() -> None:
    result = apply_mapping_to_staging_payload(
        source_payload={},
        definitions=[
            FieldMappingDefinition(
                source_field="Код",
                target_field="one_c_code",
                required=True,
                criticality=FieldCriticality.CRITICAL,
            )
        ],
    )

    assert result.issues[0].issue_type == MappingIssueType.MANUAL_REVIEW_REQUIRED