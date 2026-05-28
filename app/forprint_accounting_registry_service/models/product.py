"""
Product / nomenclature accounting projection models.

Purpose:
    Описати accounting-only номенклатурну проекцію, а не Library product catalog truth.

Boundary:
    Ці моделі не є canonical ForPrint Library catalog.
    Вони можуть використовуватись тільки як:
    - imported 1C nomenclature snapshot;
    - accounting reference for invoice lines;
    - external accounting mapping helper;
    - financial document line reference.
"""

from enum import StrEnum

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.models.common import BaseRegistryRecord


class ProductDomain(StrEnum):
    """Домен accounting/reference продукту."""

    PRINT = "print"
    DIGITAL = "digital"
    OUTDOOR = "outdoor"
    SOUVENIR = "souvenir"
    TEXTILE = "textile"
    DESIGN_SERVICE = "design_service"
    WEB_SERVICE = "web_service"
    ADVERTISING_SERVICE = "advertising_service"
    OTHER = "other"


class ProductLifecycleStatus(StrEnum):
    """Життєвий статус accounting/reference продукту."""

    DRAFT = "draft"
    ACTIVE = "active"
    PLANNED = "planned"
    TEMPLATE = "template"
    ARCHIVED = "archived"


class AttributeType(StrEnum):
    """Тип атрибуту accounting/reference продукту."""

    TEXT = "text"
    NUMBER = "number"
    DECIMAL = "decimal"
    BOOLEAN = "boolean"
    ENUM = "enum"
    DIMENSION = "dimension"
    FILE = "file"


class ProductAttribute(BaseModel):
    """Один атрибут accounting/reference продукту."""

    code: str
    name: str
    attribute_type: AttributeType

    required: bool = False
    configurable: bool = True
    visible_to_client: bool = False
    visible_to_manager: bool = True

    affects_price: bool = False
    affects_production: bool = False
    allowed_values: list[str] = Field(default_factory=list)


class Product(BaseRegistryRecord):
    """Accounting-only продукт / номенклатурна проекція / 1C reference."""

    name: str
    domain: ProductDomain
    lifecycle_status: ProductLifecycleStatus = ProductLifecycleStatus.DRAFT

    category_code: str | None = None
    unit: str | None = None
    attributes: list[ProductAttribute] = Field(default_factory=list)

    one_c_id: str | None = None
    one_c_code: str | None = None
    one_c_raw_name: str | None = None