from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from forprint_accounting_registry_service.storage.models import (
    AccountingDocument,
    AccountingReconciliationJob,
    InvoiceAccountingReference,
    OneCExportJob,
    OneCImportJob,
    OneCMappingRecord,
    OneCRawSnapshot,
    OneCStagingRecord,
    OrderAccountingReference,
    PaymentAccountingReference,
)
from forprint_accounting_registry_service.storage.repository import (
    get_record_by_id,
    save_record,
)
from sqlmodel import Session


def create_test_session() -> Session:
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)
    return Session(engine)


def test_one_c_raw_snapshot_can_be_stored_and_read() -> None:
    with create_test_session() as session:
        snapshot = save_record(
            session,
            OneCRawSnapshot(
                snapshot_type="counterparties",
                source_name="one_c_manual_export",
                file_name="counterparties.csv",
                raw_metadata={"encoding": "utf-8"},
            ),
        )

        stored = get_record_by_id(session, OneCRawSnapshot, snapshot.id)

        assert stored is not None
        assert stored.snapshot_type == "counterparties"
        assert stored.raw_metadata["encoding"] == "utf-8"


def test_one_c_staging_record_can_be_stored_and_read() -> None:
    with create_test_session() as session:
        record = save_record(
            session,
            OneCStagingRecord(
                snapshot_id="snapshot-001",
                record_type="counterparty",
                source_row_number=1,
                one_c_id="one-c-001",
                raw_payload={"name": "ТОВ Тест"},
                normalized_payload={"name": "ТОВ Тест"},
            ),
        )

        stored = get_record_by_id(session, OneCStagingRecord, record.id)

        assert stored is not None
        assert stored.record_type == "counterparty"
        assert stored.raw_payload["name"] == "ТОВ Тест"


def test_one_c_mapping_record_can_be_stored_and_read() -> None:
    with create_test_session() as session:
        mapping = save_record(
            session,
            OneCMappingRecord(
                entity_type="accounting_counterparty_reference",
                internal_accounting_id="internal-001",
                one_c_id="one-c-001",
                one_c_code="000001",
                one_c_name="ТОВ Тест",
            ),
        )

        stored = get_record_by_id(session, OneCMappingRecord, mapping.id)

        assert stored is not None
        assert stored.internal_accounting_id == "internal-001"
        assert stored.one_c_code == "000001"


def test_import_export_and_reconciliation_jobs_can_be_created() -> None:
    with create_test_session() as session:
        import_job = save_record(
            session,
            OneCImportJob(
                source_name="manual_csv",
                snapshot_id="snapshot-001",
                records_total=10,
                job_metadata={"profile": "counterparties"},
            ),
        )
        export_job = save_record(
            session,
            OneCExportJob(
                export_profile="daily_accounting_export",
                records_total=5,
                job_metadata={"target": "one_c"},
            ),
        )
        reconciliation_job = save_record(
            session,
            AccountingReconciliationJob(
                reconciliation_scope="one_c_mapping",
                period_from="2026-01-01",
                period_to="2026-01-31",
                issues_count=0,
            ),
        )

        assert get_record_by_id(session, OneCImportJob, import_job.id) is not None
        assert get_record_by_id(session, OneCExportJob, export_job.id) is not None
        assert (
            get_record_by_id(session, AccountingReconciliationJob, reconciliation_job.id)
            is not None
        )


def test_accounting_document_and_invoice_payment_references_are_accounting_only() -> None:
    with create_test_session() as session:
        document = save_record(
            session,
            AccountingDocument(
                accounting_document_type="invoice",
                document_number="INV-001",
                document_state="draft",
                source_reference_id="external-order-001",
                payload={"note": "accounting shell only"},
            ),
        )
        invoice_ref = save_record(
            session,
            InvoiceAccountingReference(
                invoice_reference_id="invoice-ref-001",
                accounting_document_id=document.id,
                source_reference_id="external-order-001",
                invoice_state="draft",
                amount_total=1000.0,
                currency="UAH",
            ),
        )
        payment_ref = save_record(
            session,
            PaymentAccountingReference(
                payment_reference_id="payment-ref-001",
                invoice_reference_id=invoice_ref.invoice_reference_id,
                payment_state="created",
                amount_total=500.0,
                currency="UAH",
            ),
        )

        stored_invoice = get_record_by_id(session, InvoiceAccountingReference, invoice_ref.id)
        stored_payment = get_record_by_id(session, PaymentAccountingReference, payment_ref.id)

        assert stored_invoice is not None
        assert stored_invoice.source_reference_id == "external-order-001"
        assert stored_payment is not None
        assert stored_payment.payment_state == "created"


def test_order_accounting_reference_does_not_own_operational_workflow() -> None:
    with create_test_session() as session:
        order_reference = save_record(
            session,
            OrderAccountingReference(
                external_order_id="order-001",
                source_module="future_operational_registry",
                reference_kind="invoice_source_reference",
                description="Reference only, not workflow state.",
            ),
        )

        stored = get_record_by_id(session, OrderAccountingReference, order_reference.id)

        assert stored is not None
        assert stored.external_order_id == "order-001"
        assert stored.reference_kind == "invoice_source_reference"