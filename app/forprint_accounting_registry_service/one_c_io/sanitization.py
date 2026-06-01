"""
OneC sanitization policy.

Purpose:
    Treat every real/test 1C-like source as dangerous until it is explicitly marked sanitized.

Boundary:
    This module does not sanitize real production data automatically.
    It only validates metadata and safety flags.
"""

from enum import StrEnum

from pydantic import BaseModel


class OneCSanitizationStatus(StrEnum):
    """Sanitization status for local/test 1C-like sources."""

    UNKNOWN = "unknown"
    SANITIZED = "sanitized"
    NOT_SANITIZED = "not_sanitized"
    SYNTHETIC = "synthetic"
    ANONYMIZED_SAMPLE = "anonymized_sample"


class OneCSanitizationError(RuntimeError):
    """Raised when a source is not safe for v0.5 processing."""


class OneCSanitizationMetadata(BaseModel):
    """Sanitization metadata for committed examples or local test sources."""

    status: OneCSanitizationStatus = OneCSanitizationStatus.UNKNOWN
    real_1c_data: bool = False
    sanitized: bool = False
    production_allowed: bool = False
    notes: str | None = None


def assert_source_is_sanitized(metadata: OneCSanitizationMetadata) -> None:
    """Reject unsanitized or production-allowed source metadata."""
    if metadata.production_allowed:
        raise OneCSanitizationError("Production sources are forbidden in v0.5.")

    if metadata.real_1c_data and metadata.status not in {
        OneCSanitizationStatus.SANITIZED,
        OneCSanitizationStatus.ANONYMIZED_SAMPLE,
    }:
        raise OneCSanitizationError("Real 1C-like data must be sanitized/anonymized.")

    if not metadata.sanitized and metadata.status not in {
        OneCSanitizationStatus.SYNTHETIC,
        OneCSanitizationStatus.SANITIZED,
        OneCSanitizationStatus.ANONYMIZED_SAMPLE,
    }:
        raise OneCSanitizationError("Source is not marked as sanitized.")