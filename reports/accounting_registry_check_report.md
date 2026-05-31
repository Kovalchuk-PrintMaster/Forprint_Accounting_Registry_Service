# ForPrint Accounting Registry Service — check report

Overall status: **OK**

| Перевірка | Очікуваний результат | Статус | Час |
|---|---|---:|---:|
| Ruff lint | Немає lint-помилок у app/tests/scripts | OK | 0.04s |
| Pytest | Усі тести проходять | OK | 1.43s |
| Boundary and storage files | Boundary docs, storage docs, manifest, and placeholders exist | OK | 0.00s |
| Module manifest validation | Manifest declares accounting role, owns, and must_not_own | OK | 0.01s |
| Placeholder contract validation | Local contracts are placeholders and non-canonical | OK | 0.01s |
| Storage model boundary validation | No canonical Client/Order/Product/Material/Invoice/Payment models | OK | 0.00s |
| OneC I/O boundary validation | No canonical Client/Order/Product/Material/Warehouse/Production models | OK | 0.00s |
