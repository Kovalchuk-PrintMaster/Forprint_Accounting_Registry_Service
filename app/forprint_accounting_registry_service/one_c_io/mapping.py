"""
OneC mapping/default policy.

Purpose:
    Safely map raw 1C-like fields into staging/normalized payloads.

Boundary:
    Critical accounting values must never be guessed silently.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.types import (
    DefaultValueCategory,
    FieldCriticality,
)


class MappingIssueType(StrEnum):
    """Mapping issue categories."""

    UNMAPPED_FIELD = "unmapped_field"
    REQUIRED_FIELD_MISSING = "required_field_missing"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"
    BLOCKED_UNTIL_MAPPED = "blocked_until_mapped"


class FieldMappingDefinition(BaseModel):
    """One source-to-target field mapping definition."""

    source_field: str
    target_field: str
    required: bool = False
    criticality: FieldCriticality = FieldCriticality.NORMAL
    default_value: Any | None = None
    default_category: DefaultValueCategory | None = None


class MappingIssue(BaseModel):
    """One mapping issue found during safe normalization."""

    issue_type: MappingIssueType
    source_field: str | None = None
    target_field: str | None = None
    severity: str = "warning"
    message: str


class UnmappedFieldRecord(BaseModel):
    """Raw source field that has no mapping definition."""

    field_name: str
    value: Any


class FieldMappingResult(BaseModel):
    """Result of applying mapping/default policy."""

    mapped_payload: dict[str, Any] = Field(default_factory=dict)
    issues: list[MappingIssue] = Field(default_factory=list)
    unmapped_fields: list[UnmappedFieldRecord] = Field(default_factory=list)


def apply_mapping_policy(
    source_payload: dict[str, Any],
    definitions: list[FieldMappingDefinition],
    preserve_unknown_fields: bool = True,
) -> FieldMappingResult:
    """
    Apply explicit mapping/default rules.

    Critical missing fields become manual-review issues by default.
    Unknown fields are captured, not discarded silently.
    """
    result = FieldMappingResult()
    mapped_source_fields = {definition.source_field for definition in definitions}

    for definition in definitions:
        if definition.source_field in source_payload:
            result.mapped_payload[definition.target_field] = source_payload[
                definition.source_field
            ]
            continue

        if definition.default_value is not None and definition.default_category not in {
            DefaultValueCategory.MANUAL_REVIEW_REQUIRED,
            DefaultValueCategory.BLOCKED_UNTIL_MAPPED,
        }:
            result.mapped_payload[definition.target_field] = definition.default_value
            continue

        if definition.required:
            issue_type = MappingIssueType.REQUIRED_FIELD_MISSING
            severity = "error"

            if definition.criticality == FieldCriticality.CRITICAL:
                issue_type = MappingIssueType.MANUAL_REVIEW_REQUIRED
                severity = "critical"

            result.issues.append(
                MappingIssue(
                    issue_type=issue_type,
                    source_field=definition.source_field,
                    target_field=definition.target_field,
                    severity=severity,
                    message=(
                        "Required mapping field is missing and must be reviewed "
                        f"explicitly: {definition.source_field}"
                    ),
                )
            )

    if preserve_unknown_fields:
        for field_name, value in source_payload.items():
            if field_name not in mapped_source_fields:
                result.unmapped_fields.append(
                    UnmappedFieldRecord(field_name=field_name, value=value)
                )
                result.issues.append(
                    MappingIssue(
                        issue_type=MappingIssueType.UNMAPPED_FIELD,
                        source_field=field_name,
                        severity="info",
                        message=f"Unmapped source field captured: {field_name}",
                    )
                )

    return result