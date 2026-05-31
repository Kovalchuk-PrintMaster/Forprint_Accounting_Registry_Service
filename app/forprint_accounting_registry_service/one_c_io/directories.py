"""
OneC directory import/export models.

Purpose:
    Handle accounting directory snapshots from 1C-like sources.

Boundary:
    Directory data is accounting reference/projection only.
    It is not CRM client registry or Library catalog truth.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.storage.models import OneCStagingRecord


class OneCDirectoryKind(StrEnum):
    """Supported accounting directory kinds."""

    COUNTERPARTY_ACCOUNTING_REFERENCES = "counterparty_accounting_references"
    NOMENCLATURE_ACCOUNTING_REFERENCES = "nomenclature_accounting_references"
    ACCOUNTING_DOCUMENT_REFERENCES = "accounting_document_references"
    PAYMENT_STATUS_REFERENCES = "payment_status_references"
    UNIT_CODE_REFERENCES = "unit_code_references"
    TAX_CODE_REFERENCES = "tax_code_references"


class OneCDirectoryItemSnapshot(BaseModel):
    """One directory item snapshot."""

    item_id: str
    raw_payload: dict[str, Any] = Field(default_factory=dict)
    normalized_payload: dict[str, Any] = Field(default_factory=dict)
    accounting_reference_only: bool = True


class OneCDirectorySnapshot(BaseModel):
    """Accounting directory snapshot."""

    snapshot_id: str
    directory_kind: OneCDirectoryKind
    source_name: str
    items: list[OneCDirectoryItemSnapshot] = Field(default_factory=list)
    real_1c_data: bool = False
    sanitized: bool = True
    production_allowed: bool = False


class OneCDirectoryImportBatch(BaseModel):
    """Directory import batch shell."""

    batch_id: str
    snapshot_id: str
    directory_kind: OneCDirectoryKind
    items_count: int
    status: str = "created"


class OneCDirectoryExportPackage(BaseModel):
    """Dry-run directory export package."""

    package_id: str
    directory_kind: OneCDirectoryKind
    records: list[dict[str, Any]] = Field(default_factory=list)
    dry_run: bool = True
    production_write_allowed: bool = False
    manual_approval_required: bool = True


class OneCDirectoryMappingIssue(BaseModel):
    """Directory mapping issue."""

    item_id: str
    field_name: str | None = None
    message: str
    severity: str = "warning"


def build_directory_import_batch(
    snapshot: OneCDirectorySnapshot,
) -> OneCDirectoryImportBatch:
    """Create import batch from directory snapshot."""
    return OneCDirectoryImportBatch(
        batch_id=f"directory-import-{snapshot.snapshot_id}",
        snapshot_id=snapshot.snapshot_id,
        directory_kind=snapshot.directory_kind,
        items_count=len(snapshot.items),
    )


def directory_snapshot_to_staging_records(
    snapshot: OneCDirectorySnapshot,
) -> list[OneCStagingRecord]:
    """Map directory snapshot into OneCStagingRecord objects."""
    records: list[OneCStagingRecord] = []

    for index, item in enumerate(snapshot.items, start=1):
        records.append(
            OneCStagingRecord(
                snapshot_id=snapshot.snapshot_id,
                record_type=f"directory:{snapshot.directory_kind}",
                source_row_number=index,
                one_c_id=item.item_id,
                raw_payload={
                    "source_name": snapshot.source_name,
                    "directory_kind": snapshot.directory_kind,
                    "item": item.raw_payload,
                    "accounting_reference_only": True,
                },
                normalized_payload=item.normalized_payload,
            )
        )

    return records