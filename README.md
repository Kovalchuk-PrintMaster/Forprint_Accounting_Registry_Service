# ForPrint Accounting Registry Service

## Role

`forprint_accounting_registry_service` is an Accounting Registry / 1C boundary / accounting truth service.

It works within ForPrint System Blueprint boundaries.

It is not CRM.

It is not Operational Registry.

It is not ForPrint Library.

It is not Integration Gateway.

It is not Calculator.

It is not a general business database.

## Current status

boundary_correction_development

The current development phase is focused on safe architectural boundaries, documentation, manifest rules, placeholder contracts, and tests.

Do not expand broad functionality before boundaries are safe.

Owns

The service may own accounting truth for:

invoice;
payment;
payment status;
accounting document;
accounting document state;
financial document state;
1C raw snapshot;
1C staging record;
1C import batch;
1C export package;
1C mapping record;
accounting reconciliation report;
accounting reference projection.
May keep projections only

The service may keep accounting projections or imported 1C references for external objects.

Allowed examples:

AccountingCounterpartyReference
OneCCounterpartySnapshot
AccountingCounterpartyProjection
OneCNomenclatureSnapshot
AccountingProductReference
AccountingNomenclatureProjection
OrderAccountingReference
InvoiceSourceReference
ExternalOrderReference

These are not canonical CRM, Operational Registry, or Library objects.

Must not own

The service must not own:

client registry;
customer interaction history;
CRM contact history;
sales pipeline;
order registry;
production order;
operational task registry;
production status;
warehouse stock;
material catalog;
product catalog;
Calculator price logic;
prepress file lifecycle;
delivery workflow;
CRM dashboard state;
business workflow decisions;
integration routing;
architecture governance;
full 1C mirror;
general business database.
1C boundary

1C is an external accounting reality.

1C is not the owner of the whole ForPrint system.

The service may import 1C snapshots, keep staging records, map 1C objects to internal accounting references, and prepare accounting reconciliation/export packages.

Contract policy

Local contract files in this repository are placeholders only.

Canonical contracts must be owned by ForPrint Library in the future.

Runtime commands should later go through ForPrint Integration Gateway where validation, idempotency, routing, and transport are required.

Development commands
make install
make lint
make test
make check
make check-report
make run
Health check
curl http://127.0.0.1:8015/health
Boundary docs
docs/architecture/accounting_registry_boundaries.md
docs/architecture/one_c_boundary.md
docs/architecture/accounting_vs_operational_registry.md
docs/development/model_naming_rules.md

## Check report

The project has an extended boundary check report.

Run:

make check-report

Generated reports:

reports/accounting_registry_check_report.json
reports/accounting_registry_check_report.md

The report validates:

Ruff lint;
pytest;
required boundary files;
module manifest boundary markers;
placeholder contract non-canonical status.

## v0.2 storage foundation

Current approved v0.2 direction:

Accounting Registry v0.2 — OneC Snapshot / Staging / Mapping Foundation

Allowed storage objects:

OneCRawSnapshot
OneCStagingRecord
OneCMappingRecord
OneCImportJob
OneCExportJob
AccountingReconciliationJob
AccountingDocument
InvoiceAccountingReference
PaymentAccountingReference
OrderAccountingReference

This is a lightweight SQLModel/SQLite-compatible foundation for local development and tests.

It is not a production DB strategy yet.

It is not CRM.

It is not Operational Registry.

It is not ForPrint Library.

It is not a full 1C mirror.


## v0.3 OneC I/O Adapter Discovery Pack

Current approved v0.3 direction:

Accounting Registry v0.3 — OneC I/O Adapter Discovery Pack

This is not real 1C integration.

This layer defines:

OneC adapter boundary;
version/channel strategy;
read/write policy;
test copy policy;
mapping/default policy;
placeholder adapters.

Implemented placeholder adapters:

OneCFileExchangeAdapter
OneCManualExportImportAdapter
OneCDirectDbReadonlyAdapter
OneCVersionedAdapterRegistry

Strictly forbidden in v0.3:

real live 1C connection;
real 1C write;
direct DB write;
production sync;
automatic posting;
full invoice lifecycle;
full payment lifecycle;
CRM integration;
Gateway runtime integration;
Library contract registry integration.

## v0.4 OneC Sandbox Direct I/O and Report Extraction Pack

Current approved v0.4 direction:

Accounting Registry v0.4 — OneC Sandbox Direct I/O, Report Extraction and Directory Exchange Pack