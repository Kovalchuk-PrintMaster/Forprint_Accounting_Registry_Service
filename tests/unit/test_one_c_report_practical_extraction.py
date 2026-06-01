from pathlib import Path

from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
)
from forprint_accounting_registry_service.one_c_io.reports import (
    OneCReportCategory,
    OneCReportDefinition,
    OneCReportRequest,
    generate_report_snapshot_from_fixture,
)

FIXTURES = Path("tests/fixtures/one_c/exports")


def test_payment_register_fixture_parses_into_report_snapshot() -> None:
    result = parse_one_c_export_file(
        FIXTURES / "payment_register.yaml",
        target_kind="payment_register_snapshot",
    )
    assert result.batch is not None

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
        snapshot_id="snapshot-001",
        definition=definition,
        request=request,
        rows=[row.raw_values for row in result.batch.rows],
    )

    assert snapshot.definition.accounting_only is True
    assert snapshot.production_allowed is False
    assert snapshot.rows[0].raw_values["document_number"] == "PAY-001"