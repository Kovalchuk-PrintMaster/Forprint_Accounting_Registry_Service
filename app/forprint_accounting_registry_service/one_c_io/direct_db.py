"""
OneC sandbox direct DB/file inspector.

Purpose:
    Provide a safe fixture-driven direct DB/file inspection boundary.

Boundary:
    This does not connect to live 1C.
    This does not write to 1C.
"""

from forprint_accounting_registry_service.one_c_io.discovery import (
    OneCRawExtractBatch,
    OneCSchemaDiscoveryReport,
    create_raw_extract_batch,
    discover_schema_from_records,
)
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    ensure_not_production_source,
)


class OneCSandboxDirectDbInspector:
    """Sandbox/test-copy-only direct DB/file inspection boundary."""

    def __init__(self, source: OneCSandboxSource) -> None:
        ensure_not_production_source(source)
        self.source = source

    def discover_schema_from_fixture(
        self,
        tables: dict[str, list[dict[str, object]]],
    ) -> OneCSchemaDiscoveryReport:
        """Create schema discovery report from sanitized fixture tables."""
        return discover_schema_from_records(
            source_id=self.source.source_id,
            adapter_name="OneCSandboxDirectDbInspector",
            tables=tables,
        )

    def extract_raw_batch_from_fixture(
        self,
        table_name: str,
        records: list[dict[str, object]],
    ) -> OneCRawExtractBatch:
        """Create raw extract batch from sanitized fixture rows."""
        return create_raw_extract_batch(
            source_id=self.source.source_id,
            source_name=self.source.path,
            table_name=table_name,
            records=records,
        )