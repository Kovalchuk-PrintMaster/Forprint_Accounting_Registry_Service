
# Accounting Storage Boundaries

## Accounting-only storage

The storage layer may contain only accounting/1C-boundary data.

Allowed models include:

- `OneCRawSnapshot`
- `OneCStagingRecord`
- `OneCMappingRecord`
- `OneCImportJob`
- `OneCExportJob`
- `AccountingReconciliationJob`
- `AccountingDocument`
- `InvoiceAccountingReference`
- `PaymentAccountingReference`
- `OrderAccountingReference`

## Operational reference only

Accounting Registry may store order references such as:

- `external_order_id`
- `order_ref`
- `source_order_ref`
- `operational_entity_ref`

These are references only.

They are not order workflow ownership.

## Invoice/payment references

`InvoiceAccountingReference` and `PaymentAccountingReference` are accounting-only shells.

They do not implement:

- full invoice lifecycle;
- full payment lifecycle;
- real payment synchronization;
- CRM invoice command processing;
- Gateway invoice routing.

## Forbidden canonical models

Do not introduce canonical models named:

- `Client`
- `Customer`
- `Order`
- `Product`
- `Material`
- `Invoice`
- `Payment`

Unless the model name explicitly marks it as accounting-only, 1C snapshot, staging, or reference.

Examples of allowed names:

- `InvoiceAccountingReference`
- `PaymentAccountingReference`
- `OrderAccountingReference`
- `OneCNomenclatureSnapshot`
- `AccountingProductReference`