"""
OneC export format detection.

Purpose:
    Detect sanitized manual/file export format where possible.
"""

from pathlib import Path

from forprint_accounting_registry_service.one_c_io.file_formats import OneCExportFormat


def detect_export_format(path: Path) -> OneCExportFormat:
    """Detect export format by file extension."""
    suffix = path.suffix.lower()

    if suffix == ".json":
        return OneCExportFormat.JSON
    if suffix == ".csv":
        return OneCExportFormat.CSV
    if suffix == ".xml":
        return OneCExportFormat.XML
    if suffix in {".yaml", ".yml"}:
        return OneCExportFormat.YAML
    if suffix in {".txt", ".dump"}:
        return OneCExportFormat.TXT_TABULAR_DUMP

    return OneCExportFormat.UNKNOWN_RAW_TEXT