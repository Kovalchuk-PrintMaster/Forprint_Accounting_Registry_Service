from forprint_accounting_registry_service.models.product import (
    AttributeType,
    Product,
    ProductAttribute,
    ProductDomain,
    ProductLifecycleStatus,
)


def test_product_supports_configurable_attributes() -> None:
    product = Product(
        name="Візитка",
        domain=ProductDomain.PRINT,
        attributes=[
            ProductAttribute(
                code="paper",
                name="Папір",
                attribute_type=AttributeType.ENUM,
                required=True,
                configurable=True,
                affects_price=True,
                affects_production=True,
                allowed_values=["300 г", "350 г"],
            )
        ],
    )

    assert product.domain == ProductDomain.PRINT
    assert product.attributes[0].affects_price is True
    assert product.attributes[0].affects_production is True


def test_product_supports_broad_advertising_information_domains() -> None:
    digital_product = Product(
        name="Digital рекламний банер",
        domain=ProductDomain.DIGITAL,
        lifecycle_status=ProductLifecycleStatus.PLANNED,
        category_code="digital_ad_banner",
        unit="item",
    )

    assert digital_product.domain == ProductDomain.DIGITAL
    assert digital_product.lifecycle_status == ProductLifecycleStatus.PLANNED
    assert digital_product.category_code == "digital_ad_banner"


def test_product_keeps_one_c_mapping_fields_as_accounting_projection() -> None:
    product = Product(
        name="Банер 440 г з 1С",
        domain=ProductDomain.PRINT,
        lifecycle_status=ProductLifecycleStatus.ACTIVE,
        one_c_id="one-c-nomenclature-001",
        one_c_code="BNR-440",
        one_c_raw_name="Банер 440 3.2 Китай",
    )

    assert product.one_c_id == "one-c-nomenclature-001"
    assert product.one_c_code == "BNR-440"
    assert product.one_c_raw_name == "Банер 440 3.2 Китай"


def test_product_attribute_can_be_non_configurable_internal_reference() -> None:
    product = Product(
        name="Облікова номенклатурна позиція",
        domain=ProductDomain.PRINT,
        attributes=[
            ProductAttribute(
                code="one_c_code",
                name="Код 1С",
                attribute_type=AttributeType.TEXT,
                required=False,
                configurable=False,
                visible_to_client=False,
                visible_to_manager=True,
                affects_price=False,
                affects_production=False,
            )
        ],
    )

    assert product.attributes[0].configurable is False
    assert product.attributes[0].visible_to_client is False
    assert product.attributes[0].affects_price is False