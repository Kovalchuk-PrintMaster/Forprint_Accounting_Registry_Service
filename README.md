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

```text
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

---
## Check report

The project has an extended boundary check report.

Run:

```bash
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

---

