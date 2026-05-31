# OneC I/O Strategy

## Purpose

This document defines the v0.3 OneC I/O adapter discovery strategy.

This is not a full production 1C integration.

## Goal

The goal is to define safe adapter boundaries for future 1C interaction.

Allowed discovery directions:

- file exchange adapter;
- manual export/import adapter;
- direct DB read-only adapter for local/test/sanitized copies only;
- future 1C 8.3 HTTP/OData adapter if available;
- future version-specific adapters.

## Conceptual flow

```text
OneCConnector / OneCAdapter
  ↓
raw 1C source data
  ↓
OneCRawSnapshot
  ↓
OneCStagingRecord
  ↓
mapping/default policy
  ↓
AccountingDocument / InvoiceAccountingReference / PaymentAccountingReference
Boundary

Accounting Registry may store accounting/1C-boundary data only.

It must not become:

CRM;
Operational Registry;
Library;
Gateway;
Calculator;
warehouse service;
product catalog truth;
client registry;
full 1C mirror.