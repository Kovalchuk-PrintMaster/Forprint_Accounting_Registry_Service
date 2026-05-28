"""
Common models.

Purpose:
    Спільні базові типи для обліково-реєстрового сервісу.
"""

from datetime import UTC, datetime
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class RecordStatus(StrEnum):
    """Життєвий статус запису."""

    DRAFT = "draft"
    ACTIVE = "active"
    ARCHIVED = "archived"
    BLOCKED = "blocked"


class SourceSystem(StrEnum):
    """Джерело походження даних."""

    ONE_C = "one_c"
    MANUAL = "manual"
    IMPORT = "import"
    GATEWAY = "gateway"
    CRM = "crm"
    LIBRARY = "library"


def utc_now() -> datetime:
    """Повертає поточний UTC datetime."""
    return datetime.now(UTC)


class BaseRegistryRecord(BaseModel):
    """Базова модель реєстрового запису."""

    id: UUID = Field(default_factory=uuid4)
    status: RecordStatus = RecordStatus.ACTIVE
    source_system: SourceSystem = SourceSystem.MANUAL
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime | None = None