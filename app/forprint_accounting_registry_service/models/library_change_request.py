"""
Library Change Request models.

Purpose:
    Якщо сервісу потрібен новий бланк, контракт, довідник або форма звіту,
    він створює заявку до ForPrint Library через майбутній погоджений flow.

Boundary:
    Accounting Registry Service може ініціювати заявку,
    але не затверджує глобальні Library стандарти.
"""

from enum import StrEnum

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.models.common import BaseRegistryRecord


class LibraryChangeRequestType(StrEnum):
    """Тип заявки до Library."""

    DOCUMENT_TEMPLATE_REQUEST = "document_template_request"
    DICTIONARY_EXTENSION_REQUEST = "dictionary_extension_request"
    CONTRACT_SCHEMA_REQUEST = "contract_schema_request"
    REPORT_FORM_REQUEST = "report_form_request"


class LibraryChangeRequestStatus(StrEnum):
    """Статус заявки."""

    DRAFT = "draft"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    RETURNED_FOR_REVISION = "returned_for_revision"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    ARCHIVED = "archived"


class LibraryChangeRequest(BaseRegistryRecord):
    """Заявка на розгляд у ForPrint Library."""

    request_type: LibraryChangeRequestType
    title: str
    reason: str

    revision: str | None = None
    requested_by_module: str = "forprint_accounting_registry_service"
    request_status: LibraryChangeRequestStatus = LibraryChangeRequestStatus.DRAFT

    proposed_code: str | None = None
    payload_schema: dict[str, object] = Field(default_factory=dict)
    example_payload: dict[str, object] = Field(default_factory=dict)
    reviewer_comment: str | None = None


class SubmitLibraryChangeRequestCommand(BaseModel):
    """Команда на подання заявки через майбутній погоджений route."""

    request: LibraryChangeRequest
    target: str = "orchestrator"