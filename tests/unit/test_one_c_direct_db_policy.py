import pytest
from forprint_accounting_registry_service.one_c_io.adapters import (
    OneCDirectDbReadonlyAdapter,
    OneCFileExchangeAdapter,
)
from forprint_accounting_registry_service.one_c_io.policies import (
    OneCAdapterPolicy,
    OneCWritePolicyViolation,
    validate_live_write_is_forbidden,
)
from forprint_accounting_registry_service.one_c_io.types import (
    OneCChannel,
    OneCExportPackage,
    OneCVersion,
)


def test_direct_db_adapter_is_read_only_and_not_production_allowed() -> None:
    adapter = OneCDirectDbReadonlyAdapter()

    assert adapter.policy.read_only is True
    assert adapter.policy.production_allowed is False
    assert adapter.policy.writes_allowed is False
    assert adapter.policy.requires_test_copy is True


def test_live_write_is_forbidden_by_default() -> None:
    adapter = OneCFileExchangeAdapter()

    package = OneCExportPackage(
        package_id="dry-run-001",
        package_type="invoice_export",
        records=[{"invoice": "INV-001"}],
        dry_run=True,
    )

    validated = adapter.validate_export_package(package)

    assert validated.package_id == "dry-run-001"


def test_non_dry_run_export_is_blocked() -> None:
    adapter = OneCFileExchangeAdapter()

    package = OneCExportPackage(
        package_id="live-write-001",
        package_type="invoice_export",
        records=[{"invoice": "INV-001"}],
        dry_run=False,
    )

    with pytest.raises(ValueError, match="Only dry-run export packages"):
        adapter.validate_export_package(package)


def test_policy_rejects_adapter_that_allows_live_writes() -> None:
    unsafe_policy = OneCAdapterPolicy(
        adapter_name="UnsafeAdapter",
        version=OneCVersion.ONE_C_8_3,
        channel=OneCChannel.FILE_EXCHANGE,
        writes_allowed=True,
        dry_run_only=False,
    )

    with pytest.raises(OneCWritePolicyViolation):
        validate_live_write_is_forbidden(unsafe_policy)