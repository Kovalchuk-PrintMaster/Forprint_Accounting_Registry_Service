# python scripts/one_c_parse_export.py

"""
Safe local OneC export parser smoke runner.

Default:
    parses sanitized fixture only.
"""

from pathlib import Path

from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
)


def parse_export(path: Path) -> int:
    """Parse sanitized export and return number of rows."""
    result = parse_one_c_export_file(path)
    if result.batch is None:
        return 0
    return len(result.batch.rows)


def main() -> int:
    """CLI entrypoint."""
    rows_count = parse_export(Path("tests/fixtures/one_c/exports/counterparties.json"))
    print(f"Parsed rows: {rows_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())