"""
External mapping models.

Purpose:
    Зберігати відповідність між внутрішніми accounting сутностями
    та зовнішніми системами, насамперед 1С.

Boundary:
    Mapping не робить 1С власником усієї системи.
    Це лише технічний accounting bridge.
"""

from enum import StrEnum

from forprint_accounting_registry_service.models.common import BaseRegistryRecord


class ExternalSystem(StrEnum):
    """Зовнішня система."""

    ONE_C = "one_c"
    NOVA_POSHTA = "nova_poshta"
    BANK = "bank"
    OTHER = "other"


class EntityType(StrEnum):
    """Тип сутності."""

    COUNTERPARTY = "counterparty"
    PRODUCT = "product"
    MATERIAL = "material"
    WAREHOUSE = "warehouse"
    DOCUMENT = "document"
    OTHER = "other"


class ExternalMapping(BaseRegistryRecord):
    """Mapping внутрішнього accounting ID до зовнішньої системи."""

    entity_type: EntityType
    internal_id: str

    external_system: ExternalSystem
    external_id: str
    external_code: str | None = None
    external_name: str | None = None

    comment: str | None = None