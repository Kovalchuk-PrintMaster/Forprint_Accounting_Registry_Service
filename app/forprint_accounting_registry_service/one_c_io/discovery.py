"""
OneC schema/file discovery models.

Purpose:
    Provide fixture-driven schema/table/field discovery output for v0.4.

Boundary:
    Discovered 1C-like names are not canonical ForPrint contracts.
"""

from typing import Any

from pydantic import BaseModel, Field


class OneCFieldDiscovery(BaseModel):
    """Discovered field information."""

    field_name: str
    sample_type: str
    sample_value: Any | None = None


class OneCTableDiscovery(BaseModel):
    """Discovered table/collection information."""

    table_name: str
    fields: list[OneCFieldDiscovery] = Field(default_factory=list)
    records_count: int = 0


class OneCSchemaDiscoveryReport(BaseModel):
    """Schema discovery report for a sandbox/test source."""

    source_id: str
    adapter_name: str
    tables: list[OneCTableDiscovery] = Field(default_factory=list)
    canonical_truth: bool = False
    notes: str = "Discovery output only. Not canonical contract truth."


class OneCRawExtractBatch(BaseModel):
    """Raw extracted batch from sandbox/test source."""

    source_id: str
    source_name: str
    table_name: str
    records: list[dict[str, Any]] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


def discover_schema_from_records(
    source_id: str,
    adapter_name: str,
    tables: dict[str, list[dict[str, Any]]],
) -> OneCSchemaDiscoveryReport:
    """Create schema discovery report from fixture-like tables."""
    discovered_tables: list[OneCTableDiscovery] = []

    for table_name, records in tables.items():
        field_names: dict[str, Any | None] = {}

        for record in records:
            for field_name, value in record.items():
                field_names.setdefault(field_name, value)

        fields = [
            OneCFieldDiscovery(
                field_name=field_name,
                sample_type=type(sample_value).__name__,
                sample_value=sample_value,
            )
            for field_name, sample_value in field_names.items()
        ]

        discovered_tables.append(
            OneCTableDiscovery(
                table_name=table_name,
                fields=fields,
                records_count=len(records),
            )
        )

    return OneCSchemaDiscoveryReport(
        source_id=source_id,
        adapter_name=adapter_name,
        tables=discovered_tables,
    )


def create_raw_extract_batch(
    source_id: str,
    source_name: str,
    table_name: str,
    records: list[dict[str, Any]],
) -> OneCRawExtractBatch:
    """Create raw extract batch preserving source records."""
    return OneCRawExtractBatch(
        source_id=source_id,
        source_name=source_name,
        table_name=table_name,
        records=records,
        metadata={"preserve_raw_values": True},
    )