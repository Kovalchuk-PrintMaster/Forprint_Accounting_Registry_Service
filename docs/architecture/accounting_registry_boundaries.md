# Accounting Registry Boundaries

## Purpose

This document defines the architectural boundary of `forprint_accounting_registry_service`.

The service is an Accounting Registry / 1C boundary / accounting truth service.

It is not CRM, not Operational Registry, not Library, not Integration Gateway, and not a general business database.

## Correct role

The service may own accounting truth for:

- invoices;
- payments;
- payment statuses;
- accounting documents;
- accounting document state;
- 1C raw snapshots;
- 1C staging records;
- 1C import batches;
- 1C export packages;
- 1C mapping records;
- accounting reconciliation reports;
- accounting reference projections;
- financial document state.

## Technical accounting objects

The service may also own technical accounting objects:

- snapshot file metadata;
- import job;
- export job;
- reconciliation job;
- mapping issue;
- accounting validation issue.

## Forbidden ownership

The service must not own canonical operational or catalog truth.

Forbidden canonical ownership includes:

- client registry;
- customer profile;
- customer interaction history;
- CRM contact history;
- sales pipeline;
- order registry;
- production order;
- operational task;
- production status;
- warehouse stock;
- warehouse reservation;
- warehouse writeoff;
- material catalog;
- product catalog;
- Calculator price logic;
- prepress file lifecycle;
- delivery workflow;
- CRM dashboard state;
- business workflow decisions;
- integration routing;
- architecture governance.

## Risky object rule

Objects such as `Counterparty`, `Product`, `Nomenclature`, or `OrderReference` are risky names.

They are allowed only when explicitly classified as:

- 1C raw snapshot;
- 1C staging record;
- imported accounting reference;
- accounting projection;
- mapping helper;
- temporary placeholder.

They must not become canonical CRM, Operational Registry, Library, Calculator, Warehouse, or Production objects.

## Current implementation interpretation

At the current stage, existing `Counterparty` and `Product`-like objects are treated only as accounting projections / imported 1C references / placeholders for future contract clarification.

They are not canonical CRM clients.

They are not canonical Library products.

They are not Operational Registry entities.

## Runtime communication rule

Runtime commands must later go through ForPrint Integration Gateway where command routing, validation, idempotency, and transport are needed.

This service may keep local placeholder contracts for tests and documentation only.

## Contract ownership rule

ForPrint Library is the future canonical source of contracts, schemas, semantic IDs, aliases, and catalog truth.

Local contract files in this service are placeholders only and must be marked as non-canonical.