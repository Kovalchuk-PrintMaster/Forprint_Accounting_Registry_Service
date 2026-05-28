from forprint_accounting_registry_service.models.counterparty import (
    AddressType,
    CommunicationChannel,
    CommunicationChannelType,
    Counterparty,
    CounterpartyAddress,
    CounterpartyContact,
    CounterpartyRole,
    CounterpartyType,
    DeliveryProfile,
    PaymentTerms,
)


def test_counterparty_can_have_multiple_accounting_roles() -> None:
    counterparty = Counterparty(
        counterparty_type=CounterpartyType.COMPANY,
        name="ТОВ Тест",
        roles=[CounterpartyRole.CLIENT, CounterpartyRole.SUPPLIER],
        one_c_id="one-c-counterparty-001",
        one_c_code="000001",
        one_c_raw_name="ТОВ Тест з 1С",
    )

    assert CounterpartyRole.CLIENT in counterparty.roles
    assert CounterpartyRole.SUPPLIER in counterparty.roles
    assert counterparty.one_c_id == "one-c-counterparty-001"
    assert counterparty.one_c_code == "000001"
    assert counterparty.one_c_raw_name == "ТОВ Тест з 1С"


def test_counterparty_supports_contacts_and_communication_channels() -> None:
    contact = CounterpartyContact(
        full_name="Іван Іваненко",
        position="Бухгалтер",
        channels=[
            CommunicationChannel(
                channel_type=CommunicationChannelType.PHONE,
                value="+380501112233",
                is_primary=True,
                verified=True,
            ),
            CommunicationChannel(
                channel_type=CommunicationChannelType.TELEGRAM,
                value="@ivan_test",
                is_primary=False,
                verified=False,
            ),
            CommunicationChannel(
                channel_type=CommunicationChannelType.VIBER,
                value="+380501112233",
                is_primary=False,
                verified=False,
            ),
        ],
        is_primary=True,
    )

    counterparty = Counterparty(
        counterparty_type=CounterpartyType.COMPANY,
        name="ТОВ Контакт",
        roles=[CounterpartyRole.CLIENT],
        contacts=[contact],
    )

    assert counterparty.contacts[0].full_name == "Іван Іваненко"
    assert counterparty.contacts[0].channels[0].channel_type == CommunicationChannelType.PHONE
    assert counterparty.contacts[0].channels[1].channel_type == CommunicationChannelType.TELEGRAM
    assert counterparty.contacts[0].channels[2].channel_type == CommunicationChannelType.VIBER


def test_counterparty_supports_addresses_delivery_and_payment_terms() -> None:
    counterparty = Counterparty(
        counterparty_type=CounterpartyType.COMPANY,
        name="ТОВ Доставка",
        roles=[CounterpartyRole.CLIENT],
        addresses=[
            CounterpartyAddress(
                address_type=AddressType.LEGAL,
                value="м. Київ, вул. Тестова, 1",
                city="Київ",
            ),
            CounterpartyAddress(
                address_type=AddressType.NOVA_POSHTA_BRANCH,
                value="Нова пошта, відділення №1",
                city="Київ",
            ),
        ],
        delivery_profile=DeliveryProfile(
            preferred_carrier="nova_poshta",
            nova_poshta_city_ref="kyiv-ref",
            nova_poshta_warehouse_ref="warehouse-ref-1",
            delivery_payer="client",
            recipient_name="Іван Іваненко",
            recipient_phone="+380501112233",
        ),
        payment_terms=PaymentTerms(
            payment_type="prepayment",
            prepayment_percent=100.0,
            currency="UAH",
            vat_mode="with_vat",
        ),
    )

    assert counterparty.addresses[0].address_type == AddressType.LEGAL
    assert counterparty.addresses[1].address_type == AddressType.NOVA_POSHTA_BRANCH
    assert counterparty.delivery_profile is not None
    assert counterparty.delivery_profile.preferred_carrier == "nova_poshta"
    assert counterparty.payment_terms is not None
    assert counterparty.payment_terms.prepayment_percent == 100.0