"""
OneC placeholder adapters.

Purpose:
    Provide adapter discovery placeholders without real 1C integration.
"""

from collections.abc import Callable

from forprint_accounting_registry_service.one_c_io.base import OneCAdapterBase
from forprint_accounting_registry_service.one_c_io.policies import (
    OneCAdapterPolicy,
    build_direct_db_readonly_policy,
)
from forprint_accounting_registry_service.one_c_io.types import (
    OneCAdapterCapability,
    OneCChannel,
    OneCRawPayload,
    OneCVersion,
)


class OneCFileExchangeAdapter(OneCAdapterBase):
    """Placeholder adapter for file exchange strategy."""

    def __init__(self, version: OneCVersion = OneCVersion.ONE_C_8_3) -> None:
        super().__init__(
            OneCAdapterPolicy(
                adapter_name="OneCFileExchangeAdapter",
                version=version,
                channel=OneCChannel.FILE_EXCHANGE,
                capabilities=[
                    OneCAdapterCapability.READ_RAW_SNAPSHOT,
                    OneCAdapterCapability.DRY_RUN_EXPORT_PACKAGE,
                ],
                read_only=True,
                production_allowed=False,
                writes_allowed=False,
                requires_test_copy=False,
                dry_run_only=True,
            )
        )

    def read_raw_snapshot(self) -> OneCRawPayload:
        """Return empty safe raw payload placeholder."""
        return OneCRawPayload(
            source_name="file_exchange_placeholder",
            version=self.policy.version,
            channel=self.policy.channel,
            records=[],
            metadata={"fixture_status": "placeholder"},
        )


class OneCManualExportImportAdapter(OneCAdapterBase):
    """Placeholder adapter for manual export/import strategy."""

    def __init__(self, version: OneCVersion = OneCVersion.ONE_C_8_2) -> None:
        super().__init__(
            OneCAdapterPolicy(
                adapter_name="OneCManualExportImportAdapter",
                version=version,
                channel=OneCChannel.MANUAL_EXPORT_IMPORT,
                capabilities=[OneCAdapterCapability.READ_RAW_SNAPSHOT],
                read_only=True,
                production_allowed=False,
                writes_allowed=False,
                requires_test_copy=False,
                dry_run_only=True,
            )
        )

    def read_raw_snapshot(self) -> OneCRawPayload:
        """Return empty safe manual import payload placeholder."""
        return OneCRawPayload(
            source_name="manual_export_import_placeholder",
            version=self.policy.version,
            channel=self.policy.channel,
            records=[],
            metadata={"fixture_status": "placeholder"},
        )


class OneCDirectDbReadonlyAdapter(OneCAdapterBase):
    """Placeholder adapter for read-only direct DB exploration on test copies only."""

    def __init__(self, version: OneCVersion = OneCVersion.UNKNOWN_FUTURE_VERSION) -> None:
        super().__init__(build_direct_db_readonly_policy(version=version))

    def read_raw_snapshot(self) -> OneCRawPayload:
        """Return empty safe DB discovery payload placeholder."""
        return OneCRawPayload(
            source_name="direct_db_readonly_placeholder",
            version=self.policy.version,
            channel=self.policy.channel,
            records=[],
            metadata={
                "fixture_status": "placeholder",
                "requires_test_copy": True,
                "production_allowed": False,
            },
        )


AdapterFactory = Callable[[], OneCAdapterBase]


class OneCVersionedAdapterRegistry:
    """Version/channel adapter registry for discovery strategy."""

    def __init__(self) -> None:
        self._factories: dict[tuple[OneCVersion, OneCChannel], AdapterFactory] = {}

    def register(
        self,
        version: OneCVersion,
        channel: OneCChannel,
        factory: AdapterFactory,
    ) -> None:
        """Register adapter factory for version/channel pair."""
        self._factories[(version, channel)] = factory

    def get_adapter(
        self,
        version: OneCVersion,
        channel: OneCChannel,
    ) -> OneCAdapterBase:
        """Create adapter for version/channel pair."""
        key = (version, channel)
        if key not in self._factories:
            raise KeyError(f"No 1C adapter registered for {version}/{channel}")

        return self._factories[key]()


def build_default_adapter_registry() -> OneCVersionedAdapterRegistry:
    """Build default placeholder adapter registry."""
    registry = OneCVersionedAdapterRegistry()

    registry.register(
        OneCVersion.ONE_C_8_2,
        OneCChannel.MANUAL_EXPORT_IMPORT,
        lambda: OneCManualExportImportAdapter(version=OneCVersion.ONE_C_8_2),
    )
    registry.register(
        OneCVersion.ONE_C_8_3,
        OneCChannel.FILE_EXCHANGE,
        lambda: OneCFileExchangeAdapter(version=OneCVersion.ONE_C_8_3),
    )
    registry.register(
        OneCVersion.UNKNOWN_FUTURE_VERSION,
        OneCChannel.DIRECT_DB_READONLY,
        lambda: OneCDirectDbReadonlyAdapter(
            version=OneCVersion.UNKNOWN_FUTURE_VERSION
        ),
    )

    return registry