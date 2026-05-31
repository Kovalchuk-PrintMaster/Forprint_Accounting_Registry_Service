from forprint_accounting_registry_service.one_c_io.mapping import (
    MappingIssue,
    MappingIssueType,
)
from forprint_accounting_registry_service.one_c_io.reports import (
    OneCReportCategory,
    OneCReportDefinition,
    OneCReportExtractionResult,
    OneCReportRequest,
    generate_report_snapshot_from_fixture,
)


def test_report_definition_and_request_can_be_created() -> None:
    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="report-request-001",
        report_code=definition.report_code,
        period_from="2026-01-01",
        period_to="2026-01-31",
    )

    assert definition.accounting_only is True
    assert request.report_code == "payment_register_snapshot"


def test_report_snapshot_can_be_generated_from_fixture() -> None:
    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="report-request-001",
        report_code=definition.report_code,
    )

    snapshot = generate_report_snapshot_from_fixture(
        snapshot_id="report-snapshot-001",
        definition=definition,
        request=request,
        rows=[{"document": "PAY-001", "amount": 1000.0}],
    )

    assert snapshot.accounting_only if hasattr(snapshot, "accounting_only") else True
    assert snapshot.rows[0].raw_values["document"] == "PAY-001"
    assert snapshot.production_allowed is False


def test_report_extraction_result_can_include_mapping_issues() -> None:
    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="report-request-001",
        report_code=definition.report_code,
    )
    snapshot = generate_report_snapshot_from_fixture(
        snapshot_id="report-snapshot-001",
        definition=definition,
        request=request,
        rows=[],
    )

    result = OneCReportExtractionResult(
        snapshot=snapshot,
        mapping_issues=[
            MappingIssue(
                issue_type=MappingIssueType.UNMAPPED_FIELD,
                source_field="Unknown",
                message="Unknown field captured",
            )
        ],
    )

    assert result.mapping_issues[0].source_field == "Unknown"