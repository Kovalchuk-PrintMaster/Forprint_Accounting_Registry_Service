# ForPrint Accounting Registry Service — check report

Overall status: **OK**

| Перевірка | Очікуваний результат | Статус | Час |
|---|---|---:|---:|
| Ruff lint | Немає lint-помилок у app/tests/scripts | OK | 0.03s |
| Pytest | Усі тести проходять | OK | 1.75s |
| Boundary, storage and OneC files | Boundary docs, storage docs, OneC docs, manifest and placeholders exist | OK | 0.00s |
| v0.5 implementation files | Sanitized source intake, export parser and pipeline files exist | OK | 0.00s |
| Module manifest validation | Manifest declares accounting role, owns, and must_not_own | OK | 0.01s |
| Placeholder contract validation | Local contracts are placeholders and non-canonical | OK | 0.02s |
| Storage model boundary validation | No canonical Client/Order/Product/Material/Warehouse/Production models | OK | 0.00s |
| OneC I/O boundary validation | No canonical Client/Order/Product/Material/Warehouse/Production models | OK | 0.00s |
| Fixture safety validation | Committed examples are sanitized, examples and non-production | OK | 0.01s |
| v0.5 test fixture validation | Sanitized parser/import fixtures exist | OK | 0.00s |
| Gitignore sandbox validation | local_sandbox and DB-like files are ignored | OK | 0.00s |
