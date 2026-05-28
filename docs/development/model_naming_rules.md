# Model Naming Rules

## Purpose

This document protects `forprint_accounting_registry_service` from architectural drift.

Generic business names can accidentally make this module look like CRM, Operational Registry, or Library.

## Counterparty naming

Avoid generic names unless clearly documented as accounting-only:

- `Client`
- `Customer`
- `Counterparty`

Preferred names:

- `AccountingCounterpartyReference`
- `OneCCounterpartySnapshot`
- `AccountingCounterpartyProjection`

Allowed role:

- imported 1C counterparty snapshot;
- accounting reference;
- invoice/payment party projection;
- mapping helper between 1C and internal IDs.

Forbidden role:

- CRM client profile;
- canonical client identity;
- customer communication history;
- sales pipeline record.

## Product / Nomenclature naming

Avoid generic names unless clearly documented as accounting projection / 1C snapshot:

- `Product`
- `Material`
- `ProductTemplate`
- `CatalogItem`

Preferred names:

- `OneCNomenclatureSnapshot`
- `AccountingNomenclatureReference`
- `AccountingProductProjection`
- `InvoiceLineNomenclatureReference`

Allowed role:

- imported 1C nomenclature snapshot;
- accounting reference for invoice lines;
- external accounting mapping helper;
- financial document line reference.

Forbidden role:

- ForPrint Library product catalog truth;
- Calculator product configuration truth;
- production product definition;
- material catalog truth.

## Order naming

Do not create a canonical `Order` model in Accounting Registry.

Preferred names:

- `OrderAccountingReference`
- `InvoiceSourceReference`
- `ExternalOrderReference`

Allowed role:

- accounting reference to an operational order;
- external order ID;
- invoice source reference;
- payment source reference.

Forbidden role:

- canonical order;
- order workflow owner;
- production order state;
- operational task owner.

## Contract naming

Local contracts in this service must be marked as placeholders.

Required marker:

```yaml
fixture_status: placeholder
canonical_contract_truth: forprint_library_future

This service must not become the canonical source of contract truth.


---
