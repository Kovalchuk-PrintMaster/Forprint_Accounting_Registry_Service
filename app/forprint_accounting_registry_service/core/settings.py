"""
Settings module.

Purpose:
    Централізовано зберігати базові налаштування сервісу.

Notes:
    На цьому етапі налаштування мінімальні.
    Пізніше можна додати читання config/service.yaml та .env.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class ServiceSettings(BaseSettings):
    """Базові налаштування сервісу."""

    model_config = SettingsConfigDict(env_prefix="FORPRINT_ACCOUNTING_REGISTRY_")

    service_name: str = "forprint_accounting_registry_service"
    service_title: str = "ForPrint Accounting Registry Service"
    service_version: str = "0.1.0"
    environment: str = "local"


@lru_cache
def get_settings() -> ServiceSettings:
    """Повертає кешований об'єкт налаштувань."""
    return ServiceSettings()