"""
OneC sandbox source manager.

Purpose:
    Manage local/test/sanitized 1C-like sources for v0.4 discovery.

Boundary:
    Sources are non-production by default.
    Destructive tests require disposable source + explicit flag.
"""

from enum import StrEnum

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.types import (
    OneCChannel,
    OneCVersion,
)


class OneCSourceKind(StrEnum):
    """Allowed source kinds for 1C sandbox/discovery inputs."""

    FILE_DATABASE_COPY = "file_database_copy"
    SQL_DUMP_COPY = "sql_dump_copy"
    MANUAL_EXPORT_FOLDER = "manual_export_folder"
    FILE_EXCHANGE_FOLDER = "file_exchange_folder"
    JSON_FIXTURE = "json_fixture"
    CSV_FIXTURE = "csv_fixture"
    XML_FIXTURE = "xml_fixture"
    UNKNOWN_SANDBOX_SOURCE = "unknown_sandbox_source"


class OneCSourceSafetyLevel(StrEnum):
    """Safety level of a local 1C-like source."""

    READONLY_FIXTURE = "readonly_fixture"
    SANDBOX_READONLY = "sandbox_readonly"
    SANDBOX_DISPOSABLE = "sandbox_disposable"
    DESTRUCTIVE_TEST_COPY = "destructive_test_copy"
    PRODUCTION_FORBIDDEN = "production_forbidden"


class OneCSandboxSource(BaseModel):
    """One local/test/sanitized 1C source declaration."""

    source_id: str
    source_kind: OneCSourceKind
    path: str
    safety_level: OneCSourceSafetyLevel

    version: OneCVersion = OneCVersion.UNKNOWN_FUTURE_VERSION
    channel: OneCChannel = OneCChannel.FILE_EXCHANGE

    disposable: bool = False
    write_tests_allowed: bool = False
    sanitized: bool = True
    production_allowed: bool = False

    metadata: dict[str, str | bool | int | float | None] = Field(default_factory=dict)


class OneCSourceSafetyError(RuntimeError):
    """Raised when a sandbox source violates safety policy."""


def ensure_not_production_source(source: OneCSandboxSource) -> None:
    """Reject production-like sources."""
    if source.production_allowed:
        raise OneCSourceSafetyError(
            f"Production source is forbidden for v0.4: {source.source_id}"
        )


def ensure_destructive_test_allowed(
    source: OneCSandboxSource,
    allow_destructive_flag: bool,
) -> None:
    """Validate destructive sandbox write requirements."""
    ensure_not_production_source(source)

    if not allow_destructive_flag:
        raise OneCSourceSafetyError("Destructive test flag is disabled.")

    if not source.disposable:
        raise OneCSourceSafetyError("Destructive tests require disposable source.")

    if not source.write_tests_allowed:
        raise OneCSourceSafetyError("Source does not allow write tests.")

    if source.safety_level not in {
        OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        OneCSourceSafetyLevel.DESTRUCTIVE_TEST_COPY,
    }:
        raise OneCSourceSafetyError(
            f"Unsafe source level for destructive test: {source.safety_level}"
        )