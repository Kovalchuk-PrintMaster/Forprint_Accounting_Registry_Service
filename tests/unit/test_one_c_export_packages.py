from forprint_accounting_registry_service.one_c_io.export_packages import (
    OneCDryRunExportPackage,
    OneCExportPackageType,
    validate_dry_run_export_package,
)
from forprint_accounting_registry_service.one_c_io.types import OneCVersion


def test_invoice_dry_run_export_package_validates() -> None:
    package = OneCDryRunExportPackage(
        package_id="pkg-001",
        package_type=OneCExportPackageType.INVOICE_EXPORT,
        target_adapter="OneCFileExchangeAdapter",
        target_version=OneCVersion.ONE_C_8_3,
        records=[{"invoice_reference_id": "invoice-ref-001"}],
    )

    result = validate_dry_run_export_package(package)

    assert result.valid is True


def test_directory_dry_run_export_package_validates() -> None:
    package = OneCDryRunExportPackage(
        package_id="pkg-002",
        package_type=OneCExportPackageType.DIRECTORY_EXPORT,
        target_adapter="OneCManualExportImportAdapter",
        target_version=OneCVersion.ONE_C_8_2,
        records=[{"item_id": "item-001"}],
    )

    result = validate_dry_run_export_package(package)

    assert result.valid is True


def test_package_cannot_be_marked_production_write() -> None:
    package = OneCDryRunExportPackage(
        package_id="pkg-003",
        package_type=OneCExportPackageType.PAYMENT_EXPORT,
        target_adapter="OneCFileExchangeAdapter",
        target_version=OneCVersion.ONE_C_8_3,
        production_write_allowed=True,
    )

    result = validate_dry_run_export_package(package)

    assert result.valid is False
    assert "production_write_allowed must be false" in result.errors


def test_package_requires_manual_approval() -> None:
    package = OneCDryRunExportPackage(
        package_id="pkg-004",
        package_type=OneCExportPackageType.ACCOUNTING_DOCUMENT_EXPORT,
        target_adapter="OneCFileExchangeAdapter",
        target_version=OneCVersion.ONE_C_8_3,
        manual_approval_required=False,
    )

    result = validate_dry_run_export_package(package)

    assert result.valid is False
    assert "manual_approval_required must be true" in result.errors