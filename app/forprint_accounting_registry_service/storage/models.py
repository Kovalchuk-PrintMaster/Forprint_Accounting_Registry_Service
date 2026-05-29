"""
Accounting Registry storage models.

Purpose:
    Small v0.2 storage foundation for OneC snapshot / staging / mapping and
    accounting-only document/reference shells.

Boundary:
    These models are accounting-only.

They must not become:
    - CRM;
    - Operational Registry;
    - Library;
    - warehouse service;
    - product catalog truth;
    - client registry;
    - order workflow owner.
"""

from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, SQLModel


def utc_now() -> datetime:
    """Return current UTC datetime."""
    return datetime.now(UTC)


def generate_id() -> str:
    """Generate stable string UUID for storage records."""
    return str(uuid4())


class StorageRecordBase(SQLModel):
    """Shared fields for Accounting Registry storage records."""

    id: str = Field(default_factory=generate_id, primary_key=True)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime | None = None


class OneCRawSnapshot(StorageRecordBase, table=True):
    """
    Raw 1C snapshot metadata.

    This stores metadata about imported raw files or raw export batches.
    It does not normalize 1C data and does not become a full 1C mirror.
    """

    __tablename__ = "one_c_raw_snapshots"

    snapshot_type: str
    source_name: str
    file_name: str | None = None
    file_path: str | None = None
    file_hash: str | None = None
    status: str = "stored"
    raw_metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class OneCStagingRecord(StorageRecordBase, table=True):
    """
    One 1C staging record.

    This is a temporary/staging representation of raw 1C data.
    It is not canonical CRM, Library, warehouse, or operational truth.
    """

    __tablename__ = "one_c_staging_records"

    snapshot_id: str
    record_type: str
    source_row_number: int | None = None
    one_c_id: str | None = None
    one_c_code: str | None = None
    validation_status: str = "pending"
    raw_payload: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )
    normalized_payload: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class OneCMappingRecord(StorageRecordBase, table=True):
    """
    Mapping between Accounting Registry objects and 1C objects.

    Mapping is technical accounting bridge data.
    It does not make 1C the owner of the whole ForPrint system.
    """

    __tablename__ = "one_c_mapping_records"

    entity_type: str
    internal_accounting_id: str
    one_c_id: str
    one_c_code: str | None = None
    one_c_name: str | None = None
    mapping_status: str = "active"
    source_snapshot_id: str | None = None


class OneCImportJob(StorageRecordBase, table=True):
    """Local import job for 1C snapshot/staging flow."""

    __tablename__ = "one_c_import_jobs"

    source_name: str
    snapshot_id: str | None = None
    job_status: str = "created"
    records_total: int = 0
    records_imported: int = 0
    records_failed: int = 0
    started_at: datetime | None = None
    finished_at: datetime | None = None
    job_metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class OneCExportJob(StorageRecordBase, table=True):
    """Local export job shell for future accounting export packages."""

    __tablename__ = "one_c_export_jobs"

    export_profile: str
    job_status: str = "created"
    records_total: int = 0
    records_exported: int = 0
    records_failed: int = 0
    started_at: datetime | None = None
    finished_at: datetime | None = None
    job_metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class AccountingReconciliationJob(StorageRecordBase, table=True):
    """Accounting-only reconciliation job shell."""

    __tablename__ = "accounting_reconciliation_jobs"

    reconciliation_scope: str
    job_status: str = "created"
    period_from: str | None = None
    period_to: str | None = None
    issues_count: int = 0
    job_metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class AccountingDocument(StorageRecordBase, table=True):
    """
    Accounting document shell.

    This is accounting document state only.
    It is not an operational order, CRM workflow, or production lifecycle.
    """

    __tablename__ = "accounting_documents"

    accounting_document_type: str
    document_number: str | None = None
    document_state: str = "draft"
    source_reference_id: str | None = None
    one_c_document_id: str | None = None
    payload: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class OrderAccountingReference(StorageRecordBase, table=True):
    """
    Read-only accounting reference to an external/future operational order.

    This is not canonical order ownership.
    """

    __tablename__ = "order_accounting_references"

    external_order_id: str
    source_module: str | None = None
    reference_kind: str = "external_order_reference"
    description: str | None = None


class InvoiceAccountingReference(StorageRecordBase, table=True):
    """
    Invoice accounting reference shell.

    This is not full invoice lifecycle.
    It does not own CRM command processing or operational workflow.
    """

    __tablename__ = "invoice_accounting_references"

    invoice_reference_id: str
    accounting_document_id: str | None = None
    source_reference_id: str | None = None
    invoice_state: str = "draft"
    amount_total: float = 0.0
    currency: str = "UAH"


class PaymentAccountingReference(StorageRecordBase, table=True):
    """
    Payment accounting reference shell.

    This is not full payment lifecycle.
    It does not implement real payment synchronization.
    """

    __tablename__ = "payment_accounting_references"

    payment_reference_id: str
    invoice_reference_id: str | None = None
    payment_state: str = "created"
    amount_total: float = 0.0
    currency: str = "UAH"
    paid_at: datetime | None = None