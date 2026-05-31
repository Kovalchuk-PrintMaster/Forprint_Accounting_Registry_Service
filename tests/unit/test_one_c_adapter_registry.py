from forprint_accounting_registry_service.one_c_io.adapters import (
    OneCDirectDbReadonlyAdapter,
    OneCFileExchangeAdapter,
    OneCManualExportImportAdapter,
    build_default_adapter_registry,
)
from forprint_accounting_registry_service.one_c_io.types import (
    OneCChannel,
    OneCVersion,
)


def test_adapter_registry_supports_one_c_8_2_placeholder() -> None:
    registry = build_default_adapter_registry()

    adapter = registry.get_adapter(
        OneCVersion.ONE_C_8_2,
        OneCChannel.MANUAL_EXPORT_IMPORT,
    )

    assert isinstance(adapter, OneCManualExportImportAdapter)
    assert adapter.policy.version == OneCVersion.ONE_C_8_2


def test_adapter_registry_supports_one_c_8_3_placeholder() -> None:
    registry = build_default_adapter_registry()

    adapter = registry.get_adapter(
        OneCVersion.ONE_C_8_3,
        OneCChannel.FILE_EXCHANGE,
    )

    assert isinstance(adapter, OneCFileExchangeAdapter)
    assert adapter.policy.version == OneCVersion.ONE_C_8_3


def test_adapter_registry_supports_unknown_future_direct_db_placeholder() -> None:
    registry = build_default_adapter_registry()

    adapter = registry.get_adapter(
        OneCVersion.UNKNOWN_FUTURE_VERSION,
        OneCChannel.DIRECT_DB_READONLY,
    )

    assert isinstance(adapter, OneCDirectDbReadonlyAdapter)
    assert adapter.policy.requires_test_copy is True