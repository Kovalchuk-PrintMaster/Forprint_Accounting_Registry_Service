# OneC Adapter Boundary

## Purpose

This document defines the adapter boundary for future 1C I/O.

## Adapter rule

Every adapter must declare:

- adapter name;
- 1C version marker;
- channel;
- capabilities;
- read-only flag;
- production allowed flag;
- writes allowed flag;
- requires test copy flag;
- dry-run-only flag.

## Placeholder adapters

Allowed v0.3 placeholders:

- `OneCFileExchangeAdapter`
- `OneCManualExportImportAdapter`
- `OneCDirectDbReadonlyAdapter`
- `OneCVersionedAdapterRegistry`

## Forbidden

Adapters must not implement:

- real live 1C connection;
- real 1C write;
- direct DB write;
- production sync;
- automatic posting;
- invoice posting;
- payment posting;
- schema changes in 1C.