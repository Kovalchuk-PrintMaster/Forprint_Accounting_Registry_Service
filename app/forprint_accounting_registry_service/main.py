# Run:
# python -m uvicorn forprint_accounting_registry_service.main:app \
#   --app-dir app --host 0.0.0.0 --port 8015 --reload

"""
Script name:
    main.py

Description:
    FastAPI entrypoint for ForPrint Accounting Registry Service.

Purpose:
    Дає мінімальну health-check точку для перевірки, що сервіс піднімається.

Used by:
    - локальний запуск;
    - майбутній health-check;
    - smoke tests.
"""

from fastapi import FastAPI

from forprint_accounting_registry_service.core.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.service_title,
    version=settings.service_version,
)


@app.get("/health")
def health() -> dict[str, str]:
    """Повертає базовий статус сервісу."""
    return {
        "status": "ok",
        "service": settings.service_name,
        "title": settings.service_title,
        "version": settings.service_version,
    }