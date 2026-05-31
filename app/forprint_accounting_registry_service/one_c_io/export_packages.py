"""
Dry-run 1C export package hardening.

Purpose:
    Validate future accounting export packages without live 1C writes.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.mapping import MappingIssue
from forprint_accounting_registry_service.one_c_io.types import OneCVersion


class OneCExportPackageType(StrEnum):
    """Allowed dry-run export package types."""

    INVOICE_EXPORT = "invoice_export"
    PAYMENT_EXPORT = "payment_export"
    DIRECTORY_EXPORT = "directory_export"
    ACCOUNTING_DOCUMENT_EXPORT = "accounting_document_export"


class OneCDryRunExportPackage(BaseModel):
    """Dry-run export package for future 1C adapter writes."""

    package_id: str
    package_type: OneCExportPackageType
    target_adapter: str
    target_version: OneCVersion
    records: list[dict[str, Any]] = Field(default_factory=list)

    dry_run_only: bool = True
    production_write_allowed: bool = False
    manual_approval_required: bool = True
    mapping_issues: list[MappingIssue] = Field(default_factory=list)


class OneCExportPackageValidationResult(BaseModel):
    """Validation result for dry-run export package."""

    package_id: str
    valid: bool
    errors: list[str] = Field(default_factory=list)


def validate_dry_run_export_package(
    package: OneCDryRunExportPackage,
) -> OneCExportPackageValidationResult:
    """Validate dry-run export package safety."""
    errors: list[str] = []

    if not package.dry_run_only:
        errors.append("dry_run_only must be true")

    if package.production_write_allowed:
        errors.append("production_write_allowed must be false")

    if not package.manual_approval_required:
        errors.append("manual_approval_required must be true")

    if not package.target_adapter:
        errors.append("target_adapter is required")

    return OneCExportPackageValidationResult(
        package_id=package.package_id,
        valid=not errors,
        errors=errors,
    )