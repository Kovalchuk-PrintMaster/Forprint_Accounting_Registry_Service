from forprint_accounting_registry_service.models.library_change_request import (
    LibraryChangeRequest,
    LibraryChangeRequestStatus,
    LibraryChangeRequestType,
)
from forprint_accounting_registry_service.services.library_change_requests import (
    prepare_submit_command,
)


def test_prepare_library_change_request_submit_command() -> None:
    request = LibraryChangeRequest(
        request_type=LibraryChangeRequestType.DOCUMENT_TEMPLATE_REQUEST,
        title="Новий податковий звіт",
        revision="2026.01",
        reason="Потрібен новий бланк для подання звітності.",
        proposed_code="tax_report_2026_01",
        payload_schema={
            "type": "object",
            "required": ["period", "amount"],
        },
        example_payload={
            "period": "2026-01",
            "amount": 1000.0,
        },
    )

    command = prepare_submit_command(request)

    assert command.target == "orchestrator"
    assert command.request.request_status == LibraryChangeRequestStatus.SUBMITTED
    assert command.request.requested_by_module == "forprint_accounting_registry_service"
    assert command.request.proposed_code == "tax_report_2026_01"


def test_library_change_request_starts_as_draft_by_default() -> None:
    request = LibraryChangeRequest(
        request_type=LibraryChangeRequestType.CONTRACT_SCHEMA_REQUEST,
        title="Accounting invoice request contract",
        reason="Потрібен placeholder-контракт для майбутньої інтеграції.",
    )

    assert request.request_status == LibraryChangeRequestStatus.DRAFT
    assert request.requested_by_module == "forprint_accounting_registry_service"
    assert request.payload_schema == {}
    assert request.example_payload == {}


def test_library_change_request_supports_report_form_request_type() -> None:
    request = LibraryChangeRequest(
        request_type=LibraryChangeRequestType.REPORT_FORM_REQUEST,
        title="Форма фінансового summary-звіту",
        reason="Потрібна форма звіту для облікового summary.",
    )

    assert request.request_type == LibraryChangeRequestType.REPORT_FORM_REQUEST