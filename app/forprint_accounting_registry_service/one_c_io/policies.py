"""
OneC I/O policy models.

Purpose:
    Keep 1C read/write strategy explicit and safe.

Boundary:
    Live writes are forbidden by default.
    Direct DB access is read-only and test-copy-only.
"""

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.types import (
    OneCAdapterCapability,
    OneCChannel,
    OneCVersion,
)


class OneCAdapterPolicy(BaseModel):
    """Safety policy attached to every 1C adapter placeholder."""

    adapter_name: str
    version: OneCVersion
    channel: OneCChannel
    capabilities: list[OneCAdapterCapability] = Field(default_factory=list)

    read_only: bool = True
    production_allowed: bool = False
    writes_allowed: bool = False
    requires_test_copy: bool = True
    dry_run_only: bool = True


class OneCWritePolicyViolation(RuntimeError):
    """Raised when a forbidden 1C write is requested."""


def validate_live_write_is_forbidden(policy: OneCAdapterPolicy) -> None:
    """Raise if adapter policy would allow live writes."""
    if policy.writes_allowed:
        raise OneCWritePolicyViolation(
            f"{policy.adapter_name} must not allow live writes in v0.3."
        )

    if not policy.dry_run_only:
        raise OneCWritePolicyViolation(
            f"{policy.adapter_name} must remain dry-run-only in v0.3."
        )


def build_direct_db_readonly_policy(
    version: OneCVersion = OneCVersion.UNKNOWN_FUTURE_VERSION,
) -> OneCAdapterPolicy:
    """Build safe policy for direct DB read-only exploration."""
    return OneCAdapterPolicy(
        adapter_name="OneCDirectDbReadonlyAdapter",
        version=version,
        channel=OneCChannel.DIRECT_DB_READONLY,
        capabilities=[OneCAdapterCapability.DIRECT_DB_READONLY_DISCOVERY],
        read_only=True,
        production_allowed=False,
        writes_allowed=False,
        requires_test_copy=True,
        dry_run_only=True,
    )