# OneC Test Copy Policy

## Purpose

This document defines the policy for 1C discovery experiments.

## Allowed

Discovery may be performed on:

- test copy;
- local sandbox copy;
- sanitized data sample;
- read-only exported files;
- manually exported snapshots.

## Forbidden

Do not use v0.3 code for:

- uncontrolled live production read;
- live production write;
- direct DB write;
- changing 1C schema;
- automatic posting;
- production synchronization.

## Direct DB adapter

If direct DB exploration is used, the adapter must be named:

OneCDirectDbReadonlyAdapter

Required policy flags:

read_only: true
production_allowed: false
writes_allowed: false
requires_test_copy: true