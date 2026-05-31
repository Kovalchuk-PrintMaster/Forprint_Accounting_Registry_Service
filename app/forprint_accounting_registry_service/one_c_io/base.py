"""
OneC adapter base classes.

Purpose:
    Define a safe adapter interface without real 1C integration.
"""

from abc import ABC, abstractmethod

from forprint_accounting_registry_service.one_c_io.policies import (
    OneCAdapterPolicy,
    validate_live_write_is_forbidden,
)
from forprint_accounting_registry_service.one_c_io.types import (
    OneCExportPackage,
    OneCRawPayload,
)


class OneCAdapterBase(ABC):
    """Base class for placeholder 1C adapters."""

    def __init__(self, policy: OneCAdapterPolicy) -> None:
        self.policy = policy
        validate_live_write_is_forbidden(policy)

    @abstractmethod
    def read_raw_snapshot(self) -> OneCRawPayload:
        """Read raw 1C-like data into a safe payload."""

    def validate_export_package(self, package: OneCExportPackage) -> OneCExportPackage:
        """Validate dry-run export package without writing to live 1C."""
        if not package.dry_run:
            raise ValueError("Only dry-run export packages are allowed in v0.3.")

        return package