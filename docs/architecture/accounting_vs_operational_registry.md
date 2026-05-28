
# Accounting Registry vs Operational Registry

## Accounting Registry

Accounting Registry is responsible for financial and accounting truth.

It owns:

- invoice;
- payment;
- payment status;
- accounting document;
- financial document state;
- 1C raw snapshot;
- 1C staging record;
- 1C mapping record;
- accounting reconciliation report;
- accounting export/import package.

## Operational Registry

Operational Registry is responsible for operational truth.

It owns:

- canonical client identity;
- orders;
- tasks;
- operational statuses;
- production/order lifecycle state;
- operational history;
- production status;
- delivery workflow;
- customer interaction history.

## Separation rule

`forprint_accounting_registry_service` must not implement `forprint_operational_registry` inside itself.

Until Operational Registry exists, Accounting Registry may store references such as:

- `external_order_id`;
- `order_ref`;
- `source_order_ref`;
- `operational_entity_ref`.

These fields must be treated only as read-only references, external references, future Operational Registry references, or temporary projections.

## Forbidden inside Accounting Registry

Accounting Registry must not own:

- canonical order workflow;
- production order state;
- task assignment;
- customer communication history;
- delivery workflow;
- CRM dashboard state.

## Invoice source reference

Allowed accounting reference examples:

- `OrderAccountingReference`;
- `InvoiceSourceReference`;
- `ExternalOrderReference`.

Forbidden:

- canonical `Order` model;
- order workflow owner;
- production status owner.