"""
OneC sanitized export parsers.

Purpose:
    Parse sanitized manual/file exports into raw parsed batches.

Boundary:
    Parsed exports become accounting staging candidates only.
    They do not create CRM clients or Library product truth.
"""

from __future__ import annotations

import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.export_detection import detect_export_format
from forprint_accounting_registry_service.one_c_io.file_formats import OneCExportFormat
from forprint_accounting_registry_service.storage.models import OneCStagingRecord


class OneCExportParseIssue(BaseModel):
    """One export parse issue."""

    row_number: int | None = None
    message: str
    severity: str = "warning"


class OneCParsedExportRow(BaseModel):
    """One parsed export row."""

    row_number: int
    raw_values: dict[str, Any] = Field(default_factory=dict)
    unknown_columns: dict[str, Any] = Field(default_factory=dict)


class OneCParsedExportBatch(BaseModel):
    """Parsed sanitized export batch."""

    source_path: str
    export_format: OneCExportFormat
    target_kind: str = "generic_accounting_table_export"
    rows: list[OneCParsedExportRow] = Field(default_factory=list)
    real_1c_data: bool = False
    sanitized: bool = True
    production_allowed: bool = False


class OneCExportParserResult(BaseModel):
    """Parser result."""

    batch: OneCParsedExportBatch | None = None
    issues: list[OneCExportParseIssue] = Field(default_factory=list)
    supported: bool = True


def parse_one_c_export_file(
        path: Path, 
        target_kind: str = "generic_accounting_table_export"
) -> OneCExportParserResult:
    """Parse sanitized export file by detected format."""
    export_format = detect_export_format(path)

    if not path.exists():
        return OneCExportParserResult(
            batch=None,
            supported=False,
            issues=[OneCExportParseIssue(message=f"File not found: {path}", severity="error")],
        )

    if export_format == OneCExportFormat.JSON:
        return parse_json_export(path, target_kind)

    if export_format == OneCExportFormat.CSV:
        return parse_csv_export(path, target_kind)

    if export_format == OneCExportFormat.YAML:
        return parse_yaml_export(path, target_kind)

    if export_format == OneCExportFormat.XML:
        return parse_xml_export(path, target_kind)

    if export_format == OneCExportFormat.TXT_TABULAR_DUMP:
        return parse_txt_tabular_export(path, target_kind)

    return OneCExportParserResult(
        batch=None,
        supported=False,
        issues=[
            OneCExportParseIssue(
                message=f"Unsupported export format: {export_format}",
                severity="error",
            )
        ],
    )


def parse_json_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse JSON export fixture."""
    payload = json.loads(path.read_text(encoding="utf-8"))

    if isinstance(payload, dict):
        records = payload.get("records", [])
        sanitized = bool(payload.get("sanitized", True))
        production_allowed = bool(payload.get("production_allowed", False))
        real_1c_data = bool(payload.get("real_1c_data", False))
    elif isinstance(payload, list):
        records = payload
        sanitized = True
        production_allowed = False
        real_1c_data = False
    else:
        records = []
        sanitized = True
        production_allowed = False
        real_1c_data = False

    rows = [
        OneCParsedExportRow(row_number=index, raw_values=dict(record))
        for index, record in enumerate(records, start=1)
        if isinstance(record, dict)
    ]

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.JSON,
            target_kind=target_kind,
            rows=rows,
            sanitized=sanitized,
            production_allowed=production_allowed,
            real_1c_data=real_1c_data,
        )
    )


def parse_csv_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse CSV export fixture."""
    rows: list[OneCParsedExportRow] = []
    issues: list[OneCExportParseIssue] = []

    with path.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)

        if not reader.fieldnames:
            return OneCExportParserResult(
                batch=OneCParsedExportBatch(
                    source_path=str(path),
                    export_format=OneCExportFormat.CSV,
                    target_kind=target_kind,
                    rows=[],
                ),
                issues=[
                    OneCExportParseIssue(
                        message="CSV has no header",
                        severity="error",
                    )
                ],
            )

        for index, row in enumerate(reader, start=1):
            if None in row:
                issues.append(
                    OneCExportParseIssue(
                        row_number=index,
                        message="Malformed CSV row has extra columns",
                        severity="warning",
                    )
                )

            raw_values = {key: value for key, value in row.items() if key is not None}
            rows.append(OneCParsedExportRow(row_number=index, raw_values=raw_values))

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.CSV,
            target_kind=target_kind,
            rows=rows,
        ),
        issues=issues,
    )


def parse_yaml_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse YAML export fixture."""
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    records = payload.get("records", payload.get("items", payload.get("rows", [])))

    rows = [
        OneCParsedExportRow(row_number=index, raw_values=dict(record))
        for index, record in enumerate(records, start=1)
        if isinstance(record, dict)
    ]

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.YAML,
            target_kind=target_kind,
            rows=rows,
            sanitized=bool(payload.get("sanitized", True)),
            production_allowed=bool(payload.get("production_allowed", False)),
            real_1c_data=bool(payload.get("real_1c_data", False)),
        )
    )


def parse_xml_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse simple XML export if possible; return issue on malformed XML."""
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except ET.ParseError as exc:
        return OneCExportParserResult(
            batch=None,
            supported=False,
            issues=[
                OneCExportParseIssue(
                    message=f"Unsupported or malformed XML export: {exc}",
                    severity="error",
                )
            ],
        )

    rows: list[OneCParsedExportRow] = []

    for index, element in enumerate(root.findall(".//record"), start=1):
        raw_values = {child.tag: child.text for child in list(element)}
        rows.append(OneCParsedExportRow(row_number=index, raw_values=raw_values))

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.XML,
            target_kind=target_kind,
            rows=rows,
        )
    )


def parse_txt_tabular_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse simple tab-separated dump."""
    rows: list[OneCParsedExportRow] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    if not lines:
        return OneCExportParserResult(
            batch=OneCParsedExportBatch(
                source_path=str(path),
                export_format=OneCExportFormat.TXT_TABULAR_DUMP,
                target_kind=target_kind,
                rows=[],
            )
        )

    headers = lines[0].split("\t")

    for index, line in enumerate(lines[1:], start=1):
        values = line.split("\t")
        rows.append(
            OneCParsedExportRow(
                row_number=index,
                raw_values=dict(zip(headers, values, strict=False)),
            )
        )

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.TXT_TABULAR_DUMP,
            target_kind=target_kind,
            rows=rows,
        )
    )


def parsed_export_batch_to_staging_records(
    batch: OneCParsedExportBatch,
    snapshot_id: str,
) -> list[OneCStagingRecord]:
    """Convert parsed export rows to staging records."""
    return [
        OneCStagingRecord(
            snapshot_id=snapshot_id,
            record_type=f"parsed_export:{batch.target_kind}",
            source_row_number=row.row_number,
            raw_payload={
                "source_path": batch.source_path,
                "export_format": batch.export_format,
                "row": row.raw_values,
            },
            normalized_payload={},
        )
        for row in batch.rows
    ]