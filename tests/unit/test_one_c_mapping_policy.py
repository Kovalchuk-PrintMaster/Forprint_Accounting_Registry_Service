from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    MappingIssueType,
    apply_mapping_policy,
)
from forprint_accounting_registry_service.one_c_io.types import (
    DefaultValueCategory,
    FieldCriticality,
)


def test_mapping_policy_maps_known_fields() -> None:
    result = apply_mapping_policy(
        source_payload={"Код": "000001", "Назва": "ТОВ Тест"},
        definitions=[
            FieldMappingDefinition(source_field="Код", target_field="one_c_code"),
            FieldMappingDefinition(source_field="Назва", target_field="name"),
        ],
    )

    assert result.mapped_payload["one_c_code"] == "000001"
    assert result.mapped_payload["name"] == "ТОВ Тест"
    assert result.unmapped_fields == []


def test_mapping_policy_records_unmapped_fields() -> None:
    result = apply_mapping_policy(
        source_payload={
            "Код": "000001",
            "НевідомеПоле": "extra",
        },
        definitions=[
            FieldMappingDefinition(source_field="Код", target_field="one_c_code")
        ],
    )

    assert result.mapped_payload["one_c_code"] == "000001"
    assert result.unmapped_fields[0].field_name == "НевідомеПоле"
    assert result.issues[0].issue_type == MappingIssueType.UNMAPPED_FIELD


def test_critical_missing_field_requires_manual_review() -> None:
    result = apply_mapping_policy(
        source_payload={"Назва": "ТОВ Тест"},
        definitions=[
            FieldMappingDefinition(
                source_field="Код",
                target_field="one_c_code",
                required=True,
                criticality=FieldCriticality.CRITICAL,
                default_category=DefaultValueCategory.MANUAL_REVIEW_REQUIRED,
            )
        ],
    )

    assert result.mapped_payload == {}
    assert result.issues[0].issue_type == MappingIssueType.MANUAL_REVIEW_REQUIRED
    assert result.issues[0].severity == "critical"


def test_non_critical_missing_required_field_is_explicit_issue() -> None:
    result = apply_mapping_policy(
        source_payload={},
        definitions=[
            FieldMappingDefinition(
                source_field="Назва",
                target_field="name",
                required=True,
                criticality=FieldCriticality.NORMAL,
            )
        ],
    )

    assert result.issues[0].issue_type == MappingIssueType.REQUIRED_FIELD_MISSING


def test_configured_default_can_be_applied_explicitly() -> None:
    result = apply_mapping_policy(
        source_payload={},
        definitions=[
            FieldMappingDefinition(
                source_field="Валюта",
                target_field="currency",
                default_value="UAH",
                default_category=DefaultValueCategory.CONFIGURED_DEFAULT,
            )
        ],
    )

    assert result.mapped_payload["currency"] == "UAH"