from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from sqlalchemy import inspect


def test_storage_database_can_be_initialized() -> None:
    engine = create_sqlite_engine(":memory:")

    init_storage(engine)

    table_names = set(inspect(engine).get_table_names())

    required_tables = {
        "one_c_raw_snapshots",
        "one_c_staging_records",
        "one_c_mapping_records",
        "one_c_import_jobs",
        "one_c_export_jobs",
        "accounting_reconciliation_jobs",
        "accounting_documents",
        "order_accounting_references",
        "invoice_accounting_references",
        "payment_accounting_references",
    }

    assert required_tables.issubset(table_names)