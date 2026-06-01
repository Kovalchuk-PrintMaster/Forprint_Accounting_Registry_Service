# python scripts/one_c_discover_source.py

"""
Safe local OneC source discovery smoke runner.

Default:
    read-only, no production, no write.
"""

from pathlib import Path

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.schema_probe import (
    probe_sanitized_source_schema,
)


def run_discovery(path: Path) -> str:
    """Run safe source discovery diagnostic."""
    source = OneCSandboxSource(
        source_id="cli-source",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path=str(path),
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
        sanitized=True,
        production_allowed=False,
    )
    result = probe_sanitized_source_schema(source)
    return result.status


def main() -> int:
    """CLI entrypoint."""
    status = run_discovery(Path("tests/fixtures/one_c/exports/counterparties.json"))
    print(f"OneC discovery status: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())