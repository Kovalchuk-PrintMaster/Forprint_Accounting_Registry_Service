"""
Mapping extracted 1C-like data into Accounting Registry staging.

Purpose:
    Convert raw extracts, directory snapshots, and report snapshots into
    OneCStagingRecord objects.

Boundary:
    Staging records remain accounting-only.
"""

from forprint_accounting_registry_service.one_c_io.directories import (
    OneCDirectorySnapshot,
    directory_snapshot_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.discovery import OneCRawExtractBatch
from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    FieldMappingResult,
    apply_mapping_policy,
)
from forprint_accounting_registry_service.one_c_io.reports import OneCReportSnapshot
from forprint_accounting_registry_service.storage.models import OneCStagingRecord


def raw_extract_batch_to_staging_records(
    batch: OneCRawExtractBatch,
) -> list[OneCStagingRecord]:
    """Convert raw extract batch to staging records."""
    records: list[OneCStagingRecord] = []

    for index, item in enumerate(batch.records, start=1):
        records.append(
            OneCStagingRecord(
                snapshot_id=batch.source_id,
                record_type=f"raw_extract:{batch.table_name}",
                source_row_number=index,
                raw_payload={
                    "source_name": batch.source_name,
                    "table_name": batch.table_name,
                    "record": item,
                },
                normalized_payload={},
            )
        )

    return records


def report_snapshot_to_staging_records(
    snapshot: OneCReportSnapshot,
) -> list[OneCStagingRecord]:
    """Convert report snapshot to staging records."""
    records: list[OneCStagingRecord] = []

    for row in snapshot.rows:
        records.append(
            OneCStagingRecord(
                snapshot_id=snapshot.snapshot_id,
                record_type=f"report:{snapshot.definition.category}",
                source_row_number=row.row_number,
                raw_payload={
                    "report_code": snapshot.definition.report_code,
                    "report_category": snapshot.definition.category,
                    "row": row.raw_values,
                    "accounting_only": True,
                },
                normalized_payload=row.normalized_values,
            )
        )

    return records


def directory_import_to_staging_records(
    snapshot: OneCDirectorySnapshot,
) -> list[OneCStagingRecord]:
    """Convert directory snapshot to staging records."""
    return directory_snapshot_to_staging_records(snapshot)


def apply_mapping_to_staging_payload(
    source_payload: dict[str, object],
    definitions: list[FieldMappingDefinition],
) -> FieldMappingResult:
    """Apply mapping policy before or during staging normalization."""
    return apply_mapping_policy(source_payload=source_payload, definitions=definitions)