"""
Mapping issue storage models.

Purpose:
    Persist mapping issues found while importing sanitized 1C-like exports into staging.

Boundary:
    These records are accounting import/mapping diagnostics only.
    They are not CRM, Library, Operational Registry, or product catalog truth.
"""

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, SQLModel


def utc_now() -> datetime:
    """Return UTC datetime."""
    return datetime.now(UTC)


def generate_id() -> str:
    """Generate stable string UUID."""
    return str(uuid4())


class MappingIssueStatus(StrEnum):
    """Mapping issue lifecycle status."""

    NEW = "new"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"
    BLOCKED_UNTIL_MAPPED = "blocked_until_mapped"
    RESOLVED = "resolved"
    IGNORED = "ignored"


class MappingIssueStorage(SQLModel, table=True):
    """Persisted mapping issue."""

    __tablename__ = "mapping_issues"

    id: str = Field(default_factory=generate_id, primary_key=True)
    issue_type: str
    status: MappingIssueStatus = MappingIssueStatus.NEW
    severity: str = "warning"

    raw_snapshot_id: str | None = None
    staging_record_id: str | None = None
    source_field: str | None = None
    target_field: str | None = None
    message: str

    payload: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )
    created_at: datetime = Field(default_factory=utc_now)
    resolved_at: datetime | None = None


class UnmappedFieldRecordStorage(SQLModel, table=True):
    """Persisted unmapped source field."""

    __tablename__ = "unmapped_field_records"

    id: str = Field(default_factory=generate_id, primary_key=True)
    mapping_issue_id: str | None = None
    staging_record_id: str | None = None
    field_name: str
    raw_value: Any | None = Field(default=None, sa_column=Column(JSON, nullable=True))
    created_at: datetime = Field(default_factory=utc_now)


class RequiredFieldMissingIssueStorage(SQLModel, table=True):
    """Persisted required missing field issue."""

    __tablename__ = "required_field_missing_issues"

    id: str = Field(default_factory=generate_id, primary_key=True)
    mapping_issue_id: str | None = None
    staging_record_id: str | None = None
    source_field: str
    target_field: str
    critical: bool = False
    created_at: datetime = Field(default_factory=utc_now)


class FieldTypeMismatchIssueStorage(SQLModel, table=True):
    """Persisted field type mismatch issue."""

    __tablename__ = "field_type_mismatch_issues"

    id: str = Field(default_factory=generate_id, primary_key=True)
    mapping_issue_id: str | None = None
    staging_record_id: str | None = None
    field_name: str
    expected_type: str
    actual_type: str
    raw_value: Any | None = Field(default=None, sa_column=Column(JSON, nullable=True))
    created_at: datetime = Field(default_factory=utc_now)


class DefaultValueDecisionStorage(SQLModel, table=True):
    """Persisted default value decision."""

    __tablename__ = "default_value_decisions"

    id: str = Field(default_factory=generate_id, primary_key=True)
    staging_record_id: str | None = None
    target_field: str
    default_category: str
    default_value: Any | None = Field(default=None, sa_column=Column(JSON, nullable=True))
    approved: bool = False
    created_at: datetime = Field(default_factory=utc_now)