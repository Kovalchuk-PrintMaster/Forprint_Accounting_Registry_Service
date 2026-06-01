"""
OneC schema probe.

Purpose:
    Probe real/sanitized test sources gracefully.

Boundary:
    Unsupported sources must return diagnostics instead of crashing.
"""

from pathlib import Path

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.discovery import (
    OneCSchemaDiscoveryReport,
    discover_schema_from_records,
)
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    ensure_not_production_source,
)


class OneCSchemaProbeResult(BaseModel):
    """Schema probe result."""

    source_id: str
    supported: bool
    status: str
    report: OneCSchemaDiscoveryReport | None = None
    diagnostics: list[str] = Field(default_factory=list)


def probe_sanitized_source_schema(
    source: OneCSandboxSource,
    fixture_tables: dict[str, list[dict[str, object]]] | None = None,
) -> OneCSchemaProbeResult:
    """Probe source schema from fixture tables or return unsupported diagnostics."""
    ensure_not_production_source(source)

    if fixture_tables is not None:
        return OneCSchemaProbeResult(
            source_id=source.source_id,
            supported=True,
            status="completed",
            report=discover_schema_from_records(
                source_id=source.source_id,
                adapter_name="OneCSchemaProbe",
                tables=fixture_tables,
            ),
        )

    path = Path(source.path)

    if not path.exists():
        return OneCSchemaProbeResult(
            source_id=source.source_id,
            supported=False,
            status="unsupported_source",
            diagnostics=[
                "Source path does not exist in local sandbox.",
                "Manual export or external parser is recommended.",
            ],
        )

    if path.suffix.lower() in {".1cd", ".dt", ".cf", ".db", ".sqlite", ".sqlite3"}:
        return OneCSchemaProbeResult(
            source_id=source.source_id,
            supported=False,
            status="unsupported_source",
            diagnostics=[
                "Binary/database-like source detected.",
                "No unsafe direct parser is implemented in v0.5.",
                "Manual export or external parser is recommended.",
            ],
        )

    return OneCSchemaProbeResult(
        source_id=source.source_id,
        supported=False,
        status="unsupported_source",
        diagnostics=["Source detected but no parser is available for schema probing."],
    )