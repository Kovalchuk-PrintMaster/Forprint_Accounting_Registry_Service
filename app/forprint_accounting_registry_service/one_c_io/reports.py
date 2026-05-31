"""
OneC report extraction interface.

Purpose:
    Represent accounting report-like snapshots extracted from 1C-like data.

Boundary:
    These are Accounting Registry report snapshots.
    They are not CRM dashboards or Operational Registry reports.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.mapping import MappingIssue


class OneCReportCategory(StrEnum):
    """Supported placeholder report categories."""

    COUNTERPARTY_BALANCE_SNAPSHOT = "counterparty_balance_snapshot"
    INVOICE_REGISTER_SNAPSHOT = "invoice_register_snapshot"
    PAYMENT_REGISTER_SNAPSHOT = "payment_register_snapshot"
    SALES_TURNOVER_SNAPSHOT = "sales_turnover_snapshot"
    MUTUAL_SETTLEMENT_SNAPSHOT = "mutual_settlement_snapshot"
    NOMENCLATURE_TURNOVER_SNAPSHOT = "nomenclature_turnover_snapshot"


class OneCReportDefinition(BaseModel):
    """One report definition placeholder."""

    report_code: str
    category: OneCReportCategory
    title: str
    accounting_only: bool = True


class OneCReportRequest(BaseModel):
    """Request for report extraction from fixture/test data."""

    request_id: str
    report_code: str
    period_from: str | None = None
    period_to: str | None = None
    source_name: str | None = None


class OneCReportRow(BaseModel):
    """One report row preserving raw values."""

    row_number: int
    raw_values: dict[str, Any] = Field(default_factory=dict)
    normalized_values: dict[str, Any] = Field(default_factory=dict)


class OneCReportSnapshot(BaseModel):
    """Extracted accounting report snapshot."""

    snapshot_id: str
    definition: OneCReportDefinition
    request: OneCReportRequest
    rows: list[OneCReportRow] = Field(default_factory=list)
    real_1c_data: bool = False
    sanitized: bool = True
    production_allowed: bool = False


class OneCReportExtractionResult(BaseModel):
    """Report extraction result with optional mapping issues."""

    snapshot: OneCReportSnapshot
    mapping_issues: list[MappingIssue] = Field(default_factory=list)
    status: str = "created"


def generate_report_snapshot_from_fixture(
    snapshot_id: str,
    definition: OneCReportDefinition,
    request: OneCReportRequest,
    rows: list[dict[str, Any]],
) -> OneCReportSnapshot:
    """Create report snapshot from sanitized fixture rows."""
    return OneCReportSnapshot(
        snapshot_id=snapshot_id,
        definition=definition,
        request=request,
        rows=[
            OneCReportRow(
                row_number=index,
                raw_values=row,
                normalized_values={},
            )
            for index, row in enumerate(rows, start=1)
        ],
    )