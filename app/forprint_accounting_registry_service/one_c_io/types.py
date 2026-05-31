"""
OneC I/O shared types.

Purpose:
    Shared enums and payload models for safe 1C adapter discovery.

Boundary:
    These types do not implement real 1C integration.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class OneCVersion(StrEnum):
    """Supported or planned 1C/BAS-like version markers."""

    ONE_C_8_2 = "one_c_8_2"
    ONE_C_8_3 = "one_c_8_3"
    UNKNOWN_FUTURE_VERSION = "unknown_future_version"


class OneCChannel(StrEnum):
    """Supported or planned 1C I/O channels."""

    FILE_EXCHANGE = "file_exchange"
    MANUAL_EXPORT_IMPORT = "manual_export_import"
    DIRECT_DB_READONLY = "direct_db_readonly"
    HTTP_ODATA_FUTURE = "http_odata_future"


class OneCAdapterCapability(StrEnum):
    """Declared placeholder adapter capabilities."""

    READ_RAW_SNAPSHOT = "read_raw_snapshot"
    DRY_RUN_EXPORT_PACKAGE = "dry_run_export_package"
    DIRECT_DB_READONLY_DISCOVERY = "direct_db_readonly_discovery"


class DefaultValueCategory(StrEnum):
    """Allowed default value categories for mapping policy."""

    SYSTEM_DEFAULT = "system_default"
    CONFIGURED_DEFAULT = "configured_default"
    SOURCE_DEFAULT = "source_default"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"
    BLOCKED_UNTIL_MAPPED = "blocked_until_mapped"


class FieldCriticality(StrEnum):
    """Accounting field criticality."""

    LOW = "low"
    NORMAL = "normal"
    CRITICAL = "critical"


class OneCRawPayload(BaseModel):
    """Raw 1C-like payload read by placeholder adapters."""

    source_name: str
    version: OneCVersion
    channel: OneCChannel
    records: list[dict[str, Any]] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class OneCExportPackage(BaseModel):
    """Dry-run export package model for future 1C writes."""

    package_id: str
    package_type: str
    records: list[dict[str, Any]] = Field(default_factory=list)
    dry_run: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)