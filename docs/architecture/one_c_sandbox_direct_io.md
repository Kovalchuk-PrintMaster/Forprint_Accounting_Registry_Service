# OneC Sandbox Direct I/O

## Purpose

This document defines safe v0.4 sandbox direct I/O discovery.

## Allowed

- local disposable test copy;
- sandbox copy;
- sanitized fixture database;
- temporary project-local ignored directory;
- read-only exploration;
- schema discovery output;
- raw extract fixtures.

## Forbidden

- live production 1C connection;
- live production 1C write;
- direct DB write into production;
- automatic posting;
- production synchronization;
- changing production 1C schema;
- committing real 1C database files to Git.

## Default mode

```text
read-only
dry-run only
no production allowed
no destructive write
Local sandbox paths
local_sandbox/one_c_databases/
local_sandbox/one_c_exports/
local_sandbox/one_c_tmp/