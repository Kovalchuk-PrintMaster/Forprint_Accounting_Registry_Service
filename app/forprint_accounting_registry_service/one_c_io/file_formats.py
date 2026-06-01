"""
OneC export file format types.

Purpose:
    Describe supported sanitized manual/file export formats.
"""

from enum import StrEnum


class OneCExportFormat(StrEnum):
    """Supported parser format markers."""

    JSON = "json"
    CSV = "csv"
    XML = "xml"
    YAML = "yaml"
    TXT_TABULAR_DUMP = "txt_tabular_dump"
    UNKNOWN_RAW_TEXT = "unknown_raw_text"
    UNSUPPORTED = "unsupported"