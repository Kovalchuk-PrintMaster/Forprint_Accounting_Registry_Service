"""
Counterparty models.

Purpose:
    Закласти повноцінну accounting-only модель контрагента,
    а не CRM-картку клієнта.

Boundary:
    Ці моделі не є canonical CRM client profile.
    Вони можуть використовуватись тільки як:
    - imported 1C counterparty snapshot;
    - accounting reference;
    - invoice/payment party projection;
    - mapping helper.
"""

from enum import StrEnum

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.models.common import BaseRegistryRecord


class CounterpartyType(StrEnum):
    """Тип контрагента."""

    PERSON = "person"
    COMPANY = "company"
    PRIVATE_ENTREPRENEUR = "private_entrepreneur"
    OTHER = "other"


class CounterpartyRole(StrEnum):
    """Accounting/reference роль контрагента."""

    CLIENT = "client"
    SUPPLIER = "supplier"
    CONTRACTOR = "contractor"
    CARRIER = "carrier"
    SERVICE_ENGINEER = "service_engineer"
    PARTNER = "partner"
    LANDLORD = "landlord"
    OTHER = "other"


class CommunicationChannelType(StrEnum):
    """Тип каналу комунікації."""

    PHONE = "phone"
    EMAIL = "email"
    TELEGRAM = "telegram"
    VIBER = "viber"
    WHATSAPP = "whatsapp"
    WEBSITE = "website"
    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    OTHER = "other"


class AddressType(StrEnum):
    """Тип адреси."""

    LEGAL = "legal"
    ACTUAL = "actual"
    DELIVERY = "delivery"
    NOVA_POSHTA_BRANCH = "nova_poshta_branch"
    NOVA_POSHTA_POSTOMAT = "nova_poshta_postomat"
    WAREHOUSE = "warehouse"
    OTHER = "other"


class CommunicationChannel(BaseModel):
    """Один канал комунікації для accounting/reference projection."""

    channel_type: CommunicationChannelType
    value: str
    is_primary: bool = False
    verified: bool = False
    comment: str | None = None


class CounterpartyContact(BaseModel):
    """Контактна особа контрагента для accounting/reference projection."""

    full_name: str
    position: str | None = None
    channels: list[CommunicationChannel] = Field(default_factory=list)
    is_primary: bool = False
    comment: str | None = None


class CounterpartyAddress(BaseModel):
    """Адреса контрагента для accounting/reference projection."""

    address_type: AddressType
    value: str
    city: str | None = None
    region: str | None = None
    country: str = "Ukraine"
    comment: str | None = None


class DeliveryProfile(BaseModel):
    """Типовий accounting/reference профіль доставки."""

    preferred_carrier: str | None = None
    nova_poshta_city_ref: str | None = None
    nova_poshta_warehouse_ref: str | None = None
    delivery_payer: str | None = None
    recipient_name: str | None = None
    recipient_phone: str | None = None
    comment: str | None = None


class PaymentTerms(BaseModel):
    """Типові accounting/reference умови оплати."""

    payment_type: str | None = None
    prepayment_percent: float | None = None
    deferred_payment_days: int | None = None
    credit_limit: float | None = None
    price_group: str | None = None
    currency: str | None = "UAH"
    vat_mode: str | None = None
    comment: str | None = None


class Counterparty(BaseRegistryRecord):
    """Accounting-only картка контрагента / 1C projection."""

    counterparty_type: CounterpartyType
    name: str
    short_name: str | None = None
    tax_id: str | None = None

    roles: list[CounterpartyRole] = Field(default_factory=list)
    responsible_manager_id: str | None = None
    tags: list[str] = Field(default_factory=list)

    contacts: list[CounterpartyContact] = Field(default_factory=list)
    addresses: list[CounterpartyAddress] = Field(default_factory=list)

    delivery_profile: DeliveryProfile | None = None
    payment_terms: PaymentTerms | None = None

    one_c_id: str | None = None
    one_c_code: str | None = None
    one_c_raw_name: str | None = None