from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.source_manifest import (
    OneCSourceManifest,
)


def test_source_manifest_can_be_serialized_and_read() -> None:
    source = OneCSandboxSource(
        source_id="fixture-001",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="examples/one_c/raw_exports/counterparties_example.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
    )
    manifest = OneCSourceManifest()
    manifest.add_source(source)

    restored = OneCSourceManifest.from_json_string(manifest.to_json_string())

    assert restored.production_allowed is False
    assert restored.real_1c_data is False
    assert restored.get_source("fixture-001") is not None