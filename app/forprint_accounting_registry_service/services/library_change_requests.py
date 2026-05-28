"""
Library Change Request service.

Purpose:
    Підготувати логіку створення заявки до Library.

Important:
    Реальна доставка заявки має йти через майбутній погоджений
    Blueprint-approved flow. На цьому етапі ми тільки формуємо command object.
"""

from forprint_accounting_registry_service.models.library_change_request import (
    LibraryChangeRequest,
    LibraryChangeRequestStatus,
    SubmitLibraryChangeRequestCommand,
)


def prepare_submit_command(request: LibraryChangeRequest) -> SubmitLibraryChangeRequestCommand:
    """Готує команду на подання заявки."""
    request.request_status = LibraryChangeRequestStatus.SUBMITTED
    return SubmitLibraryChangeRequestCommand(request=request)