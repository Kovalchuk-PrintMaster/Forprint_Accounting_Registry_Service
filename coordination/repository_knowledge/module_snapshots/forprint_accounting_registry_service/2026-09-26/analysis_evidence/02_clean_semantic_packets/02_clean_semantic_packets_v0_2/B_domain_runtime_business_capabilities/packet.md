# Accounting Registry Service â€” Packet B

## Domain / Runtime / Business Capabilities

## Status

`CLEAN_EVIDENCE_PACKET_READY_FOR_SEMANTIC_ANALYSIS`

## Purpose

Reconstruct actual accounting models, persistence and 1C I/O/runtime capabilities, including invoices/payments/receivables/reconciliation-related behavior.

## Extraction quality

- virtual environments excluded: `true`
- generated `*.egg-info`/`*.dist-info` excluded: `true`
- `tmp/**` excluded from semantic corpus: `true`
- full clean module corpus preserved separately: `true`
- clean module files in this packet: `114`
- Blueprint context files in this packet: `13`

## Authority

`analysis_only`; `action_now:none`.

Current-state divergence is evidence, not authorization to repair the module.

## Current module sources

- `app/forprint_accounting_registry_service/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/adapters/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/adapters/one_c/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/api/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/contracts/incoming/accounting_export_requested.v1.schema.json` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/contracts/outgoing/library_change_request_submitted.v1.schema.json` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/core/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/core/settings.py` â€” tracked, status ``, 955 bytes, SHA256 `ab2f1cb45f004b806f5cca574c893db872b24316800a694776b3b909483a3bfb`
- `app/forprint_accounting_registry_service/main.py` â€” tracked, status ``, 1004 bytes, SHA256 `fedb7b1a7a4a5028367a60a738168103ab04ff51b67828c36a1070fc6f6d3457`
- `app/forprint_accounting_registry_service/models/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/models/common.py` â€” tracked, status ``, 1132 bytes, SHA256 `b66ce5ebee9472b59293fc386595c2ed24ce1d5f64d25a3aef664661e553ec2a`
- `app/forprint_accounting_registry_service/models/counterparty.py` â€” tracked, status ``, 4133 bytes, SHA256 `967a35d152b49d175af348865402e7e11dbf5b577251ec74953f8f2aeb73d2ee`
- `app/forprint_accounting_registry_service/models/library_change_request.py` â€” tracked, status ``, 2058 bytes, SHA256 `5d58c3d909763e456a93ad52880e6bfc25c494e016eb0db84739497985ddc4cb`
- `app/forprint_accounting_registry_service/models/mapping.py` â€” tracked, status ``, 1234 bytes, SHA256 `f11107a5f1d6c5e1286f552efb21af33713c0e308e03df3daca4ce1661d2bb80`
- `app/forprint_accounting_registry_service/models/product.py` â€” tracked, status ``, 2440 bytes, SHA256 `fd917ad38e6198104cb2bf8b8dcb7bf716cb8486baa909d74f860aa07462683b`
- `app/forprint_accounting_registry_service/one_c_io/__init__.py` â€” tracked, status ``, 44 bytes, SHA256 `79b5eef3fff78e8cd956b1f9742275b4be5d45988c7e7c9ae482c315f0454cb0`
- `app/forprint_accounting_registry_service/one_c_io/adapters.py` â€” tracked, status ``, 5201 bytes, SHA256 `0d304692c0d7c644a6a7ddfdcb85e54cf09baed4af8a65b9f28a270259859d13`
- `app/forprint_accounting_registry_service/one_c_io/base.py` â€” tracked, status ``, 1038 bytes, SHA256 `707c52ecbef47b7c45049c1f2783804e8d27acfde765753f709765d581b58110`
- `app/forprint_accounting_registry_service/one_c_io/direct_db.py` â€” tracked, status ``, 1598 bytes, SHA256 `a4fb30545bbfd7666440b1f3e175029479f3ed44fb36ad6c5300377505bf2d47`
- `app/forprint_accounting_registry_service/one_c_io/directories.py` â€” tracked, status ``, 3514 bytes, SHA256 `c246649bbaf61f3c3e57f6dcf84d7a9ac75324da22884ac54366ad062757d972`
- `app/forprint_accounting_registry_service/one_c_io/discovery.py` â€” tracked, status ``, 2794 bytes, SHA256 `0ae3ce68c9561b6065954fd20d6d4043fee7255413da8e1a157cedcb11233a5b`
- `app/forprint_accounting_registry_service/one_c_io/export_detection.py` â€” tracked, status ``, 758 bytes, SHA256 `fa494eca6fc66debd9210f83462375393faf49520f312ab799c52bf8619a195b`
- `app/forprint_accounting_registry_service/one_c_io/export_packages.py` â€” tracked, status ``, 2033 bytes, SHA256 `d192c1950d46c9cadfaccd0b8e5746db91af4c6d1d59c2c3be8586cea55615a2`
- `app/forprint_accounting_registry_service/one_c_io/export_parsers.py` â€” tracked, status ``, 9482 bytes, SHA256 `706c44b744757c7e3ea3be658ab0eddf45e1e8a4283c061556d4a7ce50bff0ac`
- `app/forprint_accounting_registry_service/one_c_io/file_formats.py` â€” tracked, status ``, 398 bytes, SHA256 `cb12d5275234e08319d7063703b8447df91cc343d6bb2d0abc70d6af590f1b31`
- `app/forprint_accounting_registry_service/one_c_io/import_pipeline.py` â€” tracked, status ``, 6785 bytes, SHA256 `de309910f32053c6b72fd78f5a878ef562968c0679c8dbca039214c3f64630ba`
- `app/forprint_accounting_registry_service/one_c_io/mapping.py` â€” tracked, status ``, 4162 bytes, SHA256 `635183a9e6395a6b018d4c69d397a972afa669d6e2858208405546c15f461b01`
- `app/forprint_accounting_registry_service/one_c_io/policies.py` â€” tracked, status ``, 1906 bytes, SHA256 `9b37037b639485177e3a31b1cb595716e951091c449afadeb470936ae2f533ab`
- `app/forprint_accounting_registry_service/one_c_io/reports.py` â€” tracked, status ``, 2739 bytes, SHA256 `a124ed9767a55417055d7f831c081078e74a68c885db1a75ab6fdecc7cb8c152`
- `app/forprint_accounting_registry_service/one_c_io/sandbox_sources.py` â€” tracked, status ``, 2898 bytes, SHA256 `8240fe2922427fbc87c601be9da6faa34ec3fceca41d1d71617adc8a9c7fd454`
- `app/forprint_accounting_registry_service/one_c_io/sandbox_write.py` â€” tracked, status ``, 5623 bytes, SHA256 `b2687b324e4d5bc54b4271c50c9bb3a175b73229ffbd6d608287bcc55444932a`
- `app/forprint_accounting_registry_service/one_c_io/sanitization.py` â€” tracked, status ``, 1799 bytes, SHA256 `30e652ecd4d0f1d0839b3093685ee6af03fbb950d94607565c6cb1811a59918f`
- `app/forprint_accounting_registry_service/one_c_io/schema_probe.py` â€” tracked, status ``, 2504 bytes, SHA256 `3bfe37e8303e0ee6ddd664bfd4f298be1f8c071914340604600cb05cdbb4ddcc`
- `app/forprint_accounting_registry_service/one_c_io/source_manifest.py` â€” tracked, status ``, 1212 bytes, SHA256 `67c222ea6ea05d5e1201b3bcda906c37f523a0d6d3513481e86878e14c3c6c9f`
- `app/forprint_accounting_registry_service/one_c_io/staging.py` â€” tracked, status ``, 2900 bytes, SHA256 `bb2543ae4ec57e02ba1359576616e709c7236491d09cfa529db306700e8baa99`
- `app/forprint_accounting_registry_service/one_c_io/test_database_registry.py` â€” tracked, status ``, 6360 bytes, SHA256 `788b5b279c3aff8ad3a68d2f51d0db954dc52d5ac9e60e754dce01361d2904f2`
- `app/forprint_accounting_registry_service/one_c_io/types.py` â€” tracked, status ``, 2023 bytes, SHA256 `9fa7284f6a2df7a09a602e12af7617cdabfe652109f9221888438919469ba4a6`
- `app/forprint_accounting_registry_service/repositories/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/repositories/mapping_issues.py` â€” tracked, status ``, 1847 bytes, SHA256 `f3a634cac304ce3b06aeb7203f593abd0dc0a6b2dfc384ce5b3d5a48f810b06c`
- `app/forprint_accounting_registry_service/services/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/services/library_change_requests.py` â€” tracked, status ``, 845 bytes, SHA256 `876498080dd6a19d97e7fadd4d89b3bec4e2694507874cbc7dc46b0e900b8173`
- `app/forprint_accounting_registry_service/services/mapping_issue_registry.py` â€” tracked, status ``, 2157 bytes, SHA256 `b644e98c0b542767d84b6155b2800a5dae51e8d8003ba396473103aa6bf4db58`
- `app/forprint_accounting_registry_service/services/one_c_snapshot.py` â€” tracked, status ``, 989 bytes, SHA256 `7c39531685b8bd4687672f83e11d3440f573679a2fc3fc1a30fd4cfd1c6c1786`
- `app/forprint_accounting_registry_service/storage/__init__.py` â€” tracked, status ``, 0 bytes, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `app/forprint_accounting_registry_service/storage/database.py` â€” tracked, status ``, 1355 bytes, SHA256 `2dae0ee02317fb1b69744d5fe356fb9315c9741fd5b446cfeed2521816c28c62`
- `app/forprint_accounting_registry_service/storage/mapping_models.py` â€” tracked, status ``, 3524 bytes, SHA256 `1dfe68bb802cd0e4fa200c2a16e23b897d738819eae8d5d21b25242e905c20b2`
- `app/forprint_accounting_registry_service/storage/models.py` â€” tracked, status ``, 6354 bytes, SHA256 `c51187c7be8f12821473bd3e69846f7424725900d3721baa295c62e0ce247579`
- `app/forprint_accounting_registry_service/storage/repository.py` â€” tracked, status ``, 767 bytes, SHA256 `bd978c66f7f885fb46a390c30ecfec6b28961163912b580257bdf36e36715ba7`
- `contracts/placeholders/accounting.finance_summary.v1.yaml` â€” tracked, status ``, 892 bytes, SHA256 `0d890fb1fb13fc51147717cd67429bc3d09c8befc4f595b68fd283618080b6e2`
- `contracts/placeholders/accounting.invoice_request.v1.yaml` â€” tracked, status ``, 944 bytes, SHA256 `c4128427b60abea719412657fa1b1f2b1a92813a08c961cf8ed0e13304ba2331`
- `contracts/placeholders/accounting.one_c_import_result.v1.yaml` â€” tracked, status ``, 798 bytes, SHA256 `18a05ddd60dec734c989417d0d613a40ed5389341c7f17729ba5196669fb0eb1`
- `contracts/placeholders/accounting.payment_status_reference.v1.yaml` â€” tracked, status ``, 853 bytes, SHA256 `2964d3b6687eb84c4444a4871f54614cf290110e8a1d84b2e5f9d15fb8f530bd`
- `docs/architecture/accounting_registry_boundaries.md` â€” tracked, status ``, 2806 bytes, SHA256 `3f3617513eb5e87bf978267a76a13c7181e6644a9282e122b8f75917306b89df`
- `docs/architecture/accounting_storage_boundaries.md` â€” tracked, status ``, 1366 bytes, SHA256 `cf8e267d7eca7e69605584bb6152739ef4d6755591feebedbb3fcc3bd5524aff`
- `docs/architecture/accounting_storage_foundation.md` â€” tracked, status ``, 1576 bytes, SHA256 `02e576eba354080a3f686be04d2e8190f52301ec58199bbd64aac70a09131a91`
- `docs/architecture/accounting_vs_operational_registry.md` â€” tracked, status ``, 1601 bytes, SHA256 `a0609ebdef07e257df75fdd3b812b4ead396d39ffd42c883d5fd92177eb3651e`
- `docs/architecture/one_c_adapter_boundary.md` â€” tracked, status ``, 716 bytes, SHA256 `a6a9c56cc0de39a1b9e19556e0a69d8a95e7056c78c0725673c5bbe4937375c6`
- `docs/architecture/one_c_boundary.md` â€” tracked, status ``, 1466 bytes, SHA256 `75e8914886ff07f41e9807e64e1904ec442edbe26c324785929735b0eb3a4ae5`
- `docs/architecture/one_c_directory_exchange.md` â€” tracked, status ``, 1852 bytes, SHA256 `9722ee7b31bf764ae91fbaca96a3cb710cd70ce954a5c4fd8c5cfc2787137127`
- `docs/architecture/one_c_io_strategy.md` â€” tracked, status ``, 940 bytes, SHA256 `23fcca43368d4b3c013205f3737d85884ebcf518bd57655f98da49942f402846`
- `docs/architecture/one_c_mapping_policy.md` â€” tracked, status ``, 868 bytes, SHA256 `e915ba58c8cf8770c30289210450d721f55a4ebac129c34e0b5a3a6ec63c4e36`
- `docs/architecture/one_c_read_write_policy.md` â€” tracked, status ``, 1016 bytes, SHA256 `5b11d7ec6d16d4a521b5ee3d7ad9feacac3ada6eca3c7a5b86bf140cceb95222`
- `docs/architecture/one_c_report_extraction.md` â€” tracked, status ``, 717 bytes, SHA256 `9695586e7f7072f42bd229fd3915ce76cb4867ea11e92fe2d5c91f30e36f5768`
- `docs/architecture/one_c_sandbox_direct_io.md` â€” tracked, status ``, 746 bytes, SHA256 `7cb9ab54866de031b33b53e528129d6120b057fd66fcfd7df4dc27215ee77b4e`
- `docs/architecture/one_c_snapshot_staging_flow.md` â€” tracked, status ``, 1047 bytes, SHA256 `90de55ae9982f8fe236a47d59c4b9823fe7c088bde7d7ee7fe0be35e6b03cbdb`
- `docs/architecture/one_c_test_copy_policy.md` â€” tracked, status ``, 686 bytes, SHA256 `4145e15e63c635fe6a5bdddbdd70aa8dbaaa82c6fecee2d3ca73f3fa61acc882`
- `docs/architecture/one_c_version_strategy.md` â€” tracked, status ``, 669 bytes, SHA256 `976bc3603dc16d761a625ac168895ffcfe46d67b0d7f24d2ba802bf0eb56c71a`
- `examples/one_c/directories/counterparty_directory.yaml` â€” tracked, status ``, 356 bytes, SHA256 `853ca1b75f8e25898ea7324e644888d126e73fab6250289983b4c2ff22f7379d`
- `examples/one_c/export_packages/invoice_dry_run_export.yaml` â€” tracked, status ``, 258 bytes, SHA256 `9fbeaff43ea3cb385c706f147d91cf2c788a6e145921c58e9a59d0a93f5141b3`
- `examples/one_c/raw_exports/counterparties_example.json` â€” tracked, status ``, 354 bytes, SHA256 `61ba0978aaf39493c40434071c3f1158bfa5b29c6648cb13788e2499afc1c268`
- `examples/one_c/reports/payment_register_snapshot.yaml` â€” tracked, status ``, 196 bytes, SHA256 `0b370009f490994a94d8aa0c4b29103f4c1bb1eb96bafd02782522289a01d3c0`
- `examples/one_c/write_experiments/write_experiment_example.yaml` â€” tracked, status ``, 137 bytes, SHA256 `56a65a873b2695069892599f9f6581017e3f9c82f374ade2f6fb4251f44b9646`
- `forprint_module_manifest.yaml` â€” tracked, status ``, 3078 bytes, SHA256 `b67d5923a9fb372e2ee9c88b19659d9f10cb63fbea90892d5abb7466dd5ade39`
- `pyproject.toml` â€” tracked, status ``, 979 bytes, SHA256 `b7a4c7803b144809bb59f5ba3966bb0b45b6e7359cbe7e8e19ccdd7254387fb1`
- `reports/accounting_registry_check_report.json` â€” tracked, status ``, 2592 bytes, SHA256 `b9ac676527f93db268c0e4360d5fa771411cbdb072d567ac92cb7ae941041fc4`
- `reports/accounting_registry_check_report.md` â€” tracked, status ``, 1302 bytes, SHA256 `b530d857564b4df302f96c13e09b960c751e8cee2901d9e93f57f2cb343294d8`
- `reports/accounting_registry_module_status.json` â€” tracked, status ``, 198 bytes, SHA256 `3c5559c8563775dca41d3523c4c6c1abdba76da07bb13da7868314cba2054ebc`
- `scripts/one_c_discover_source.py` â€” tracked, status ``, 1107 bytes, SHA256 `577f2610e79274937bfb371ac5c05bc7bc3b4310ad51b034f32a11e9b3534990`
- `scripts/one_c_parse_export.py` â€” tracked, status ``, 737 bytes, SHA256 `4102b06e8cd060655f8a14213209d96e4bec7fa05986603d17cf9cc511942493`
- `scripts/one_c_run_import_pipeline.py` â€” tracked, status ``, 1883 bytes, SHA256 `3d28d0a08db607772efa098adb315494991a972143ce1ba2bb000f93e8095847`
- `tests/fixtures/one_c/databases/synthetic_test_db.txt` â€” tracked, status ``, 81 bytes, SHA256 `836a9abf4d39161a8634f799b2605ad4f494e8a01a96052ba95496a7e5d0fe8b`
- `tests/fixtures/one_c/exports/counterparties.csv` â€” tracked, status ``, 112 bytes, SHA256 `f1ec71ab464e152c43447ea75a43d1264f52375d347bcc064b1780d1b1fddc34`
- `tests/fixtures/one_c/exports/counterparties.json` â€” tracked, status ``, 302 bytes, SHA256 `8ca7a318a1b96a5fe7e6eaa9346b004129d0713400b1c7885966b3e2314d373b`
- `tests/fixtures/one_c/exports/counterparties.xml` â€” tracked, status ``, 191 bytes, SHA256 `e5d57b0692172dde92533b1c3c1c7f32bbcc08b27d5abde444ae9b7ec59be74c`
- `tests/fixtures/one_c/exports/payment_register.yaml` â€” tracked, status ``, 157 bytes, SHA256 `028f2a9e77aa2f59f68cd0de9da7817494235f7a71553694c89c13f7a80f33ed`
- `tests/unit/test_counterparty_model.py` â€” tracked, status ``, 4056 bytes, SHA256 `8da760bc4463049e5302d7b72bee0647c9d46356e46352db0aefdb1f413d3b0f`
- `tests/unit/test_mapping_issue_persistence.py` â€” tracked, status ``, 2883 bytes, SHA256 `cc7e2dfc144dc0e6cb277f781bdcb817db325729dd6f97db209ad3b0c29b28ed`
- `tests/unit/test_mapping_issue_registry_service.py` â€” tracked, status ``, 1226 bytes, SHA256 `dd6d1394d8e641f31c80a0bbb166a33d312d1fb7403a2589e3c2732a0e38ba1b`
- `tests/unit/test_one_c_adapter_registry.py` â€” tracked, status ``, 1378 bytes, SHA256 `6221261546bbe3e3fade4e6ab2f7dce6f85adba433ed30be16b6938416cc395f`
- `tests/unit/test_one_c_developer_cli.py` â€” tracked, status ``, 810 bytes, SHA256 `3e7535f7a4712a78f6e5f579c95a8104b081409c768fbbda827dadc700ccf228`
- `tests/unit/test_one_c_direct_db_discovery.py` â€” tracked, status ``, 2157 bytes, SHA256 `a4847a62deb88f0c77075ab7a660805942716509bdc4613786077f83b27d0cd1`
- `tests/unit/test_one_c_direct_db_policy.py` â€” tracked, status ``, 1936 bytes, SHA256 `4bb69d9c4c6a4494fff084d69648a57f83f841bbf3e792d5cd3126aa0c46561c`
- `tests/unit/test_one_c_directories.py` â€” tracked, status ``, 1857 bytes, SHA256 `92852b2cd78ab78e51c4787dbde514e3154ce419f9eb37b7bdcc372ea84667b3`
- `tests/unit/test_one_c_directory_practical_import.py` â€” tracked, status ``, 1815 bytes, SHA256 `0eed2df94407458d5083645690af26740552e0bf0b537971cdff4e2c0910be36`
- `tests/unit/test_one_c_export_packages.py` â€” tracked, status ``, 2109 bytes, SHA256 `f1502aad7921712ea9880859f26f1b8e62a5edf1b5ac3f956615f7f245000130`
- `tests/unit/test_one_c_export_parsers.py` â€” tracked, status ``, 2050 bytes, SHA256 `3ca80fa1c508e74864d9be75949555b33de116f533ecca89980feb9ef90b920e`
- `tests/unit/test_one_c_fixtures.py` â€” tracked, status ``, 1208 bytes, SHA256 `aa22aa17e12287ebd73a1630b28e18cb6c2b2bbcbd96583dc9f883d23aca8076`
- `tests/unit/test_one_c_import_pipeline.py` â€” tracked, status ``, 3255 bytes, SHA256 `33ff0caeaa2d339659cd01dd133dad8037b3bd1c8bb0bfd6d8205fffefe6df63`
- `tests/unit/test_one_c_io_boundaries.py` â€” tracked, status ``, 1604 bytes, SHA256 `e89d077e9dd7132b451b25618f9160f3a5e1e92868717c8fcf24752952d38654`
- `tests/unit/test_one_c_mapping_policy.py` â€” tracked, status ``, 2962 bytes, SHA256 `0e0f4d9e751d41f07113c1c895ef121636072b26158707ba4403b2f1cad05df5`
- `tests/unit/test_one_c_report_practical_extraction.py` â€” tracked, status ``, 1311 bytes, SHA256 `9670732f9c303c72d809ea33315a3aa81ccb75515b7652294b6450ed1113c436`
- `tests/unit/test_one_c_reports.py` â€” tracked, status ``, 2613 bytes, SHA256 `e0b18b0d590464ddc3f1f2c7fd1b8a95431222a7d74d19dc9d82cc4344ab7b05`
- `tests/unit/test_one_c_sandbox_sources.py` â€” tracked, status ``, 2001 bytes, SHA256 `9e9f90efd7f64c0aeb562c6801d325dc1fbad84d8ee12ae2148ba2ae98e44022`
- `tests/unit/test_one_c_sandbox_write.py` â€” tracked, status ``, 3099 bytes, SHA256 `fa25d252e377a7843d1b279615d7a06ff32c88ba1899cda2f5366d55a4645e4f`
- `tests/unit/test_one_c_sandbox_write_hardening.py` â€” tracked, status ``, 3181 bytes, SHA256 `fd4e4ae89b9e5573aa588e5ffad6e6ebf0a0da7681800aae748b19ca3ee8acd2`
- `tests/unit/test_one_c_sanitization_and_test_db_registry.py` â€” tracked, status ``, 3170 bytes, SHA256 `ea5f92b77077beb6a3280a26d2367d23bfa5150b59756c6e52aadcfe0376acac`
- `tests/unit/test_one_c_schema_probe.py` â€” tracked, status ``, 1787 bytes, SHA256 `bc17d23b00654803bb55dc2c6b88dfec663057c178a9407cf50a9899b4cfb0af`
- `tests/unit/test_one_c_snapshot.py` â€” tracked, status ``, 1826 bytes, SHA256 `3747942b9428dd72e28e02608d90c1cbb8b34363763a28f1c69babced0c01be0`
- `tests/unit/test_one_c_source_manifest.py` â€” tracked, status ``, 862 bytes, SHA256 `8ad5e39115e4b82e7a92927183631d213b85c5580d7e74a9ae3b2f0055ffbd88`
- `tests/unit/test_one_c_staging_mapping.py` â€” tracked, status ``, 3130 bytes, SHA256 `6cbded4e70931953c0804b9c0a8d5ddb9d33bf62e274e69d55fa2e4fe0825bbc`
- `tests/unit/test_product_model.py` â€” tracked, status ``, 2772 bytes, SHA256 `87571711d1999288e338b216f5598b18edcedeb5950bf76195e1d4a37bef0992`
- `tests/unit/test_storage_boundaries.py` â€” tracked, status ``, 1566 bytes, SHA256 `cc4f0f2a7e9f87fc506bbc3d3c456edb1a6bf473b770fee1e86f8742470afac6`
- `tests/unit/test_storage_database.py` â€” tracked, status ``, 763 bytes, SHA256 `0d904e97e536a6f53ff48d0d4067d69314e6d0022523569c553fb7b34fdaa5c8`
- `tests/unit/test_storage_records.py` â€” tracked, status ``, 6396 bytes, SHA256 `4f63dbc2d37fadb49d8b866bf81c7c441745cc5bfb8c420ff41ecef346a2eacd`

## Relevant Git history

- `7315a7a6bd0a8f4e08385bdbd676edaf8aa25bb5	2026-06-10	Add Accounting Registry governance alignment`
- `95d4a55de3f5ac647d74df8672e2f234ec559a5c	2026-06-01	Add Accounting Registry sanitized OneC import pipeline`
- `ab48ef1a8b45157bbc199531f5a90660038b5890	2026-05-31	Add Accounting Registry OneC sandbox IO and report extraction layer`
- `009dfefa98031ec78b8ef77bed09a0d43b9c3c16	2026-05-31	Add Accounting Registry OneC IO adapter strategy`
- `ec46ef1e82bdc42415f0bb497c98dc2582801b78	2026-05-29	Add Accounting Registry OneC staging storage foundation`
- `2e98a3a78d9d69119e00c35d1a8c078a4e2866f4	2026-05-28	Add Accounting Registry boundary corrections`

## Blueprint anchors

- `coordination/human_intent/modules/forprint_accounting_registry_service.yaml` â€” 4849 bytes, SHA256 `e7dfccee8b5c7eb641000fce43dd01d835a8af0c7d5dc5930d67ce129f31abdb`
- `coordination/module_policy/forprint_accounting_registry_service/goods_receipt_automation_target_state_v0_1_20260826.md` â€” 1827 bytes, SHA256 `dac053bd4efebeb5ce71325d447db2e7dac09090b41b23848503b2beab468c30`
- `coordination/module_policy/forprint_accounting_registry_service/module_policy.md` â€” 1322 bytes, SHA256 `c046b321858ea0008659ff3edf3e67e91d57c430e5a95b5dd11ee5e9be7a5d52`
- `coordination/roadmaps/details/forprint_system_blueprint/accounts_receivable_collection_direction_v0_1.md` â€” 2530 bytes, SHA256 `39be8a528eda77172adaf5b092a63efbbf6365fa8a04ef38e2066fe343c0e745`
- `coordination/roadmaps/details/forprint_system_blueprint/evening_architecture_module_amendments_v0_1/forprint_accounting_registry_service.md` â€” 465 bytes, SHA256 `f18aaed4bf3c50beb8fad9168e5ed7c26c1605bac16f1d72f5ed84dc4a013132`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_full_horizon_target_states_v0_1.md` â€” 44395 bytes, SHA256 `01bc35e630c4a42c3f360aa658c4d67a0d008fd23551bc62904a59163c71861a`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_full_horizon_target_states_v0_1.yaml` â€” 65183 bytes, SHA256 `cbfca4b97c739e9b13ec1ed31afd7d32834923a87d8caa756eb4c1355fc50486`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_module_roadmap_approval_matrix_v0_1.md` â€” 49699 bytes, SHA256 `2efa675aac3ac5b5c1b95d5261a4a5c5040917ea771286ad4ae4358a9dfef4ad`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_module_roadmap_approval_matrix_v0_1.yaml` â€” 147483 bytes, SHA256 `5305f0d74cbef25eb533909c80df14fbb4e134a17cace603cd1e97b07cded8fd`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_rebuild_inputs/2026-08-27__forprint_accounting_registry_service__revision1_owner_review_v0_1.md` â€” 4281 bytes, SHA256 `919e285c5a2785c39b3c646ad1e1bbe911921385f75eb5b96fb2fe17f9f39275`
- `coordination/roadmaps/details/forprint_system_blueprint/portfolio_rebuild_seeds/forprint_accounting_registry_service.yaml` â€” 2241 bytes, SHA256 `9cc382436c7df2a11568a950cbe013989762c797d642b97c1679edb1780063e4`
- `machine/data_objects.yaml` â€” 22617 bytes, SHA256 `8c84d9eb1276d3091699766210f48a7ebd5affb8ea490c2ad4b9093be673cde7`
- `machine/modules.yaml` â€” 13841 bytes, SHA256 `f38886cc0e49960726788d968f7f30c5bcdb83d369f93702f6c4bc1cc3e319f6`

## Full current source bodies


### MODULE SOURCE â€” app/forprint_accounting_registry_service/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/adapters/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/adapters/one_c/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/api/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/contracts/incoming/accounting_export_requested.v1.schema.json

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```json

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/contracts/outgoing/library_change_request_submitted.v1.schema.json

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```json

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/core/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/core/settings.py

`SHA256=ab2f1cb45f004b806f5cca574c893db872b24316800a694776b3b909483a3bfb`

```py
"""
Settings module.

Purpose:
    Централізовано зберігати базові налаштування сервісу.

Notes:
    На цьому етапі налаштування мінімальні.
    Пізніше можна додати читання config/service.yaml та .env.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class ServiceSettings(BaseSettings):
    """Базові налаштування сервісу."""

    model_config = SettingsConfigDict(env_prefix="FORPRINT_ACCOUNTING_REGISTRY_")

    service_name: str = "forprint_accounting_registry_service"
    service_title: str = "ForPrint Accounting Registry Service"
    service_version: str = "0.1.0"
    environment: str = "local"


@lru_cache
def get_settings() -> ServiceSettings:
    """Повертає кешований об'єкт налаштувань."""
    return ServiceSettings()
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/main.py

`SHA256=fedb7b1a7a4a5028367a60a738168103ab04ff51b67828c36a1070fc6f6d3457`

```py
# Run:
# python -m uvicorn forprint_accounting_registry_service.main:app \
#   --app-dir app --host 0.0.0.0 --port 8015 --reload

"""
Script name:
    main.py

Description:
    FastAPI entrypoint for ForPrint Accounting Registry Service.

Purpose:
    Дає мінімальну health-check точку для перевірки, що сервіс піднімається.

Used by:
    - локальний запуск;
    - майбутній health-check;
    - smoke tests.
"""

from fastapi import FastAPI

from forprint_accounting_registry_service.core.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.service_title,
    version=settings.service_version,
)


@app.get("/health")
def health() -> dict[str, str]:
    """Повертає базовий статус сервісу."""
    return {
        "status": "ok",
        "service": settings.service_name,
        "title": settings.service_title,
        "version": settings.service_version,
    }
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/models/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/models/common.py

`SHA256=b66ce5ebee9472b59293fc386595c2ed24ce1d5f64d25a3aef664661e553ec2a`

```py
"""
Common models.

Purpose:
    Спільні базові типи для обліково-реєстрового сервісу.
"""

from datetime import UTC, datetime
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class RecordStatus(StrEnum):
    """Життєвий статус запису."""

    DRAFT = "draft"
    ACTIVE = "active"
    ARCHIVED = "archived"
    BLOCKED = "blocked"


class SourceSystem(StrEnum):
    """Джерело походження даних."""

    ONE_C = "one_c"
    MANUAL = "manual"
    IMPORT = "import"
    GATEWAY = "gateway"
    CRM = "crm"
    LIBRARY = "library"


def utc_now() -> datetime:
    """Повертає поточний UTC datetime."""
    return datetime.now(UTC)


class BaseRegistryRecord(BaseModel):
    """Базова модель реєстрового запису."""

    id: UUID = Field(default_factory=uuid4)
    status: RecordStatus = RecordStatus.ACTIVE
    source_system: SourceSystem = SourceSystem.MANUAL
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime | None = None
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/models/counterparty.py

`SHA256=967a35d152b49d175af348865402e7e11dbf5b577251ec74953f8f2aeb73d2ee`

```py
"""
Counterparty models.

Purpose:
    Закласти повноцінну accounting-only модель контрагента,
    а не CRM-картку клієнта.

Boundary:
    Ці моделі не є canonical CRM client profile.
    Вони можуть використовуватись тільки як:
    - imported 1C counterparty snapshot;
    - accounting reference;
    - invoice/payment party projection;
    - mapping helper.
"""

from enum import StrEnum

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.models.common import BaseRegistryRecord


class CounterpartyType(StrEnum):
    """Тип контрагента."""

    PERSON = "person"
    COMPANY = "company"
    PRIVATE_ENTREPRENEUR = "private_entrepreneur"
    OTHER = "other"


class CounterpartyRole(StrEnum):
    """Accounting/reference роль контрагента."""

    CLIENT = "client"
    SUPPLIER = "supplier"
    CONTRACTOR = "contractor"
    CARRIER = "carrier"
    SERVICE_ENGINEER = "service_engineer"
    PARTNER = "partner"
    LANDLORD = "landlord"
    OTHER = "other"


class CommunicationChannelType(StrEnum):
    """Тип каналу комунікації."""

    PHONE = "phone"
    EMAIL = "email"
    TELEGRAM = "telegram"
    VIBER = "viber"
    WHATSAPP = "whatsapp"
    WEBSITE = "website"
    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    OTHER = "other"


class AddressType(StrEnum):
    """Тип адреси."""

    LEGAL = "legal"
    ACTUAL = "actual"
    DELIVERY = "delivery"
    NOVA_POSHTA_BRANCH = "nova_poshta_branch"
    NOVA_POSHTA_POSTOMAT = "nova_poshta_postomat"
    WAREHOUSE = "warehouse"
    OTHER = "other"


class CommunicationChannel(BaseModel):
    """Один канал комунікації для accounting/reference projection."""

    channel_type: CommunicationChannelType
    value: str
    is_primary: bool = False
    verified: bool = False
    comment: str | None = None


class CounterpartyContact(BaseModel):
    """Контактна особа контрагента для accounting/reference projection."""

    full_name: str
    position: str | None = None
    channels: list[CommunicationChannel] = Field(default_factory=list)
    is_primary: bool = False
    comment: str | None = None


class CounterpartyAddress(BaseModel):
    """Адреса контрагента для accounting/reference projection."""

    address_type: AddressType
    value: str
    city: str | None = None
    region: str | None = None
    country: str = "Ukraine"
    comment: str | None = None


class DeliveryProfile(BaseModel):
    """Типовий accounting/reference профіль доставки."""

    preferred_carrier: str | None = None
    nova_poshta_city_ref: str | None = None
    nova_poshta_warehouse_ref: str | None = None
    delivery_payer: str | None = None
    recipient_name: str | None = None
    recipient_phone: str | None = None
    comment: str | None = None


class PaymentTerms(BaseModel):
    """Типові accounting/reference умови оплати."""

    payment_type: str | None = None
    prepayment_percent: float | None = None
    deferred_payment_days: int | None = None
    credit_limit: float | None = None
    price_group: str | None = None
    currency: str | None = "UAH"
    vat_mode: str | None = None
    comment: str | None = None


class Counterparty(BaseRegistryRecord):
    """Accounting-only картка контрагента / 1C projection."""

    counterparty_type: CounterpartyType
    name: str
    short_name: str | None = None
    tax_id: str | None = None

    roles: list[CounterpartyRole] = Field(default_factory=list)
    responsible_manager_id: str | None = None
    tags: list[str] = Field(default_factory=list)

    contacts: list[CounterpartyContact] = Field(default_factory=list)
    addresses: list[CounterpartyAddress] = Field(default_factory=list)

    delivery_profile: DeliveryProfile | None = None
    payment_terms: PaymentTerms | None = None

    one_c_id: str | None = None
    one_c_code: str | None = None
    one_c_raw_name: str | None = None
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/models/library_change_request.py

`SHA256=5d58c3d909763e456a93ad52880e6bfc25c494e016eb0db84739497985ddc4cb`

```py
"""
Library Change Request models.

Purpose:
    Якщо сервісу потрібен новий бланк, контракт, довідник або форма звіту,
    він створює заявку до ForPrint Library через майбутній погоджений flow.

Boundary:
    Accounting Registry Service може ініціювати заявку,
    але не затверджує глобальні Library стандарти.
"""

from enum import StrEnum

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.models.common import BaseRegistryRecord


class LibraryChangeRequestType(StrEnum):
    """Тип заявки до Library."""

    DOCUMENT_TEMPLATE_REQUEST = "document_template_request"
    DICTIONARY_EXTENSION_REQUEST = "dictionary_extension_request"
    CONTRACT_SCHEMA_REQUEST = "contract_schema_request"
    REPORT_FORM_REQUEST = "report_form_request"


class LibraryChangeRequestStatus(StrEnum):
    """Статус заявки."""

    DRAFT = "draft"
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    RETURNED_FOR_REVISION = "returned_for_revision"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    ARCHIVED = "archived"


class LibraryChangeRequest(BaseRegistryRecord):
    """Заявка на розгляд у ForPrint Library."""

    request_type: LibraryChangeRequestType
    title: str
    reason: str

    revision: str | None = None
    requested_by_module: str = "forprint_accounting_registry_service"
    request_status: LibraryChangeRequestStatus = LibraryChangeRequestStatus.DRAFT

    proposed_code: str | None = None
    payload_schema: dict[str, object] = Field(default_factory=dict)
    example_payload: dict[str, object] = Field(default_factory=dict)
    reviewer_comment: str | None = None


class SubmitLibraryChangeRequestCommand(BaseModel):
    """Команда на подання заявки через майбутній погоджений route."""

    request: LibraryChangeRequest
    target: str = "orchestrator"
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/models/mapping.py

`SHA256=f11107a5f1d6c5e1286f552efb21af33713c0e308e03df3daca4ce1661d2bb80`

```py
"""
External mapping models.

Purpose:
    Зберігати відповідність між внутрішніми accounting сутностями
    та зовнішніми системами, насамперед 1С.

Boundary:
    Mapping не робить 1С власником усієї системи.
    Це лише технічний accounting bridge.
"""

from enum import StrEnum

from forprint_accounting_registry_service.models.common import BaseRegistryRecord


class ExternalSystem(StrEnum):
    """Зовнішня система."""

    ONE_C = "one_c"
    NOVA_POSHTA = "nova_poshta"
    BANK = "bank"
    OTHER = "other"


class EntityType(StrEnum):
    """Тип сутності."""

    COUNTERPARTY = "counterparty"
    PRODUCT = "product"
    MATERIAL = "material"
    WAREHOUSE = "warehouse"
    DOCUMENT = "document"
    OTHER = "other"


class ExternalMapping(BaseRegistryRecord):
    """Mapping внутрішнього accounting ID до зовнішньої системи."""

    entity_type: EntityType
    internal_id: str

    external_system: ExternalSystem
    external_id: str
    external_code: str | None = None
    external_name: str | None = None

    comment: str | None = None
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/models/product.py

`SHA256=fd917ad38e6198104cb2bf8b8dcb7bf716cb8486baa909d74f860aa07462683b`

```py
"""
Product / nomenclature accounting projection models.

Purpose:
    Описати accounting-only номенклатурну проекцію, а не Library product catalog truth.

Boundary:
    Ці моделі не є canonical ForPrint Library catalog.
    Вони можуть використовуватись тільки як:
    - imported 1C nomenclature snapshot;
    - accounting reference for invoice lines;
    - external accounting mapping helper;
    - financial document line reference.
"""

from enum import StrEnum

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.models.common import BaseRegistryRecord


class ProductDomain(StrEnum):
    """Домен accounting/reference продукту."""

    PRINT = "print"
    DIGITAL = "digital"
    OUTDOOR = "outdoor"
    SOUVENIR = "souvenir"
    TEXTILE = "textile"
    DESIGN_SERVICE = "design_service"
    WEB_SERVICE = "web_service"
    ADVERTISING_SERVICE = "advertising_service"
    OTHER = "other"


class ProductLifecycleStatus(StrEnum):
    """Життєвий статус accounting/reference продукту."""

    DRAFT = "draft"
    ACTIVE = "active"
    PLANNED = "planned"
    TEMPLATE = "template"
    ARCHIVED = "archived"


class AttributeType(StrEnum):
    """Тип атрибуту accounting/reference продукту."""

    TEXT = "text"
    NUMBER = "number"
    DECIMAL = "decimal"
    BOOLEAN = "boolean"
    ENUM = "enum"
    DIMENSION = "dimension"
    FILE = "file"


class ProductAttribute(BaseModel):
    """Один атрибут accounting/reference продукту."""

    code: str
    name: str
    attribute_type: AttributeType

    required: bool = False
    configurable: bool = True
    visible_to_client: bool = False
    visible_to_manager: bool = True

    affects_price: bool = False
    affects_production: bool = False
    allowed_values: list[str] = Field(default_factory=list)


class Product(BaseRegistryRecord):
    """Accounting-only продукт / номенклатурна проекція / 1C reference."""

    name: str
    domain: ProductDomain
    lifecycle_status: ProductLifecycleStatus = ProductLifecycleStatus.DRAFT

    category_code: str | None = None
    unit: str | None = None
    attributes: list[ProductAttribute] = Field(default_factory=list)

    one_c_id: str | None = None
    one_c_code: str | None = None
    one_c_raw_name: str | None = None
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/__init__.py

`SHA256=79b5eef3fff78e8cd956b1f9742275b4be5d45988c7e7c9ae482c315f0454cb0`

```py
"""Safe 1C I/O adapter discovery package."""
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/adapters.py

`SHA256=0d304692c0d7c644a6a7ddfdcb85e54cf09baed4af8a65b9f28a270259859d13`

```py
"""
OneC placeholder adapters.

Purpose:
    Provide adapter discovery placeholders without real 1C integration.
"""

from collections.abc import Callable

from forprint_accounting_registry_service.one_c_io.base import OneCAdapterBase
from forprint_accounting_registry_service.one_c_io.policies import (
    OneCAdapterPolicy,
    build_direct_db_readonly_policy,
)
from forprint_accounting_registry_service.one_c_io.types import (
    OneCAdapterCapability,
    OneCChannel,
    OneCRawPayload,
    OneCVersion,
)


class OneCFileExchangeAdapter(OneCAdapterBase):
    """Placeholder adapter for file exchange strategy."""

    def __init__(self, version: OneCVersion = OneCVersion.ONE_C_8_3) -> None:
        super().__init__(
            OneCAdapterPolicy(
                adapter_name="OneCFileExchangeAdapter",
                version=version,
                channel=OneCChannel.FILE_EXCHANGE,
                capabilities=[
                    OneCAdapterCapability.READ_RAW_SNAPSHOT,
                    OneCAdapterCapability.DRY_RUN_EXPORT_PACKAGE,
                ],
                read_only=True,
                production_allowed=False,
                writes_allowed=False,
                requires_test_copy=False,
                dry_run_only=True,
            )
        )

    def read_raw_snapshot(self) -> OneCRawPayload:
        """Return empty safe raw payload placeholder."""
        return OneCRawPayload(
            source_name="file_exchange_placeholder",
            version=self.policy.version,
            channel=self.policy.channel,
            records=[],
            metadata={"fixture_status": "placeholder"},
        )


class OneCManualExportImportAdapter(OneCAdapterBase):
    """Placeholder adapter for manual export/import strategy."""

    def __init__(self, version: OneCVersion = OneCVersion.ONE_C_8_2) -> None:
        super().__init__(
            OneCAdapterPolicy(
                adapter_name="OneCManualExportImportAdapter",
                version=version,
                channel=OneCChannel.MANUAL_EXPORT_IMPORT,
                capabilities=[OneCAdapterCapability.READ_RAW_SNAPSHOT],
                read_only=True,
                production_allowed=False,
                writes_allowed=False,
                requires_test_copy=False,
                dry_run_only=True,
            )
        )

    def read_raw_snapshot(self) -> OneCRawPayload:
        """Return empty safe manual import payload placeholder."""
        return OneCRawPayload(
            source_name="manual_export_import_placeholder",
            version=self.policy.version,
            channel=self.policy.channel,
            records=[],
            metadata={"fixture_status": "placeholder"},
        )


class OneCDirectDbReadonlyAdapter(OneCAdapterBase):
    """Placeholder adapter for read-only direct DB exploration on test copies only."""

    def __init__(self, version: OneCVersion = OneCVersion.UNKNOWN_FUTURE_VERSION) -> None:
        super().__init__(build_direct_db_readonly_policy(version=version))

    def read_raw_snapshot(self) -> OneCRawPayload:
        """Return empty safe DB discovery payload placeholder."""
        return OneCRawPayload(
            source_name="direct_db_readonly_placeholder",
            version=self.policy.version,
            channel=self.policy.channel,
            records=[],
            metadata={
                "fixture_status": "placeholder",
                "requires_test_copy": True,
                "production_allowed": False,
            },
        )


AdapterFactory = Callable[[], OneCAdapterBase]


class OneCVersionedAdapterRegistry:
    """Version/channel adapter registry for discovery strategy."""

    def __init__(self) -> None:
        self._factories: dict[tuple[OneCVersion, OneCChannel], AdapterFactory] = {}

    def register(
        self,
        version: OneCVersion,
        channel: OneCChannel,
        factory: AdapterFactory,
    ) -> None:
        """Register adapter factory for version/channel pair."""
        self._factories[(version, channel)] = factory

    def get_adapter(
        self,
        version: OneCVersion,
        channel: OneCChannel,
    ) -> OneCAdapterBase:
        """Create adapter for version/channel pair."""
        key = (version, channel)
        if key not in self._factories:
            raise KeyError(f"No 1C adapter registered for {version}/{channel}")

        return self._factories[key]()


def build_default_adapter_registry() -> OneCVersionedAdapterRegistry:
    """Build default placeholder adapter registry."""
    registry = OneCVersionedAdapterRegistry()

    registry.register(
        OneCVersion.ONE_C_8_2,
        OneCChannel.MANUAL_EXPORT_IMPORT,
        lambda: OneCManualExportImportAdapter(version=OneCVersion.ONE_C_8_2),
    )
    registry.register(
        OneCVersion.ONE_C_8_3,
        OneCChannel.FILE_EXCHANGE,
        lambda: OneCFileExchangeAdapter(version=OneCVersion.ONE_C_8_3),
    )
    registry.register(
        OneCVersion.UNKNOWN_FUTURE_VERSION,
        OneCChannel.DIRECT_DB_READONLY,
        lambda: OneCDirectDbReadonlyAdapter(
            version=OneCVersion.UNKNOWN_FUTURE_VERSION
        ),
    )

    return registry
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/base.py

`SHA256=707c52ecbef47b7c45049c1f2783804e8d27acfde765753f709765d581b58110`

```py
"""
OneC adapter base classes.

Purpose:
    Define a safe adapter interface without real 1C integration.
"""

from abc import ABC, abstractmethod

from forprint_accounting_registry_service.one_c_io.policies import (
    OneCAdapterPolicy,
    validate_live_write_is_forbidden,
)
from forprint_accounting_registry_service.one_c_io.types import (
    OneCExportPackage,
    OneCRawPayload,
)


class OneCAdapterBase(ABC):
    """Base class for placeholder 1C adapters."""

    def __init__(self, policy: OneCAdapterPolicy) -> None:
        self.policy = policy
        validate_live_write_is_forbidden(policy)

    @abstractmethod
    def read_raw_snapshot(self) -> OneCRawPayload:
        """Read raw 1C-like data into a safe payload."""

    def validate_export_package(self, package: OneCExportPackage) -> OneCExportPackage:
        """Validate dry-run export package without writing to live 1C."""
        if not package.dry_run:
            raise ValueError("Only dry-run export packages are allowed in v0.3.")

        return package
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/direct_db.py

`SHA256=a4fb30545bbfd7666440b1f3e175029479f3ed44fb36ad6c5300377505bf2d47`

```py
"""
OneC sandbox direct DB/file inspector.

Purpose:
    Provide a safe fixture-driven direct DB/file inspection boundary.

Boundary:
    This does not connect to live 1C.
    This does not write to 1C.
"""

from forprint_accounting_registry_service.one_c_io.discovery import (
    OneCRawExtractBatch,
    OneCSchemaDiscoveryReport,
    create_raw_extract_batch,
    discover_schema_from_records,
)
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    ensure_not_production_source,
)


class OneCSandboxDirectDbInspector:
    """Sandbox/test-copy-only direct DB/file inspection boundary."""

    def __init__(self, source: OneCSandboxSource) -> None:
        ensure_not_production_source(source)
        self.source = source

    def discover_schema_from_fixture(
        self,
        tables: dict[str, list[dict[str, object]]],
    ) -> OneCSchemaDiscoveryReport:
        """Create schema discovery report from sanitized fixture tables."""
        return discover_schema_from_records(
            source_id=self.source.source_id,
            adapter_name="OneCSandboxDirectDbInspector",
            tables=tables,
        )

    def extract_raw_batch_from_fixture(
        self,
        table_name: str,
        records: list[dict[str, object]],
    ) -> OneCRawExtractBatch:
        """Create raw extract batch from sanitized fixture rows."""
        return create_raw_extract_batch(
            source_id=self.source.source_id,
            source_name=self.source.path,
            table_name=table_name,
            records=records,
        )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/directories.py

`SHA256=c246649bbaf61f3c3e57f6dcf84d7a9ac75324da22884ac54366ad062757d972`

```py
"""
OneC directory import/export models.

Purpose:
    Handle accounting directory snapshots from 1C-like sources.

Boundary:
    Directory data is accounting reference/projection only.
    It is not CRM client registry or Library catalog truth.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.storage.models import OneCStagingRecord


class OneCDirectoryKind(StrEnum):
    """Supported accounting directory kinds."""

    COUNTERPARTY_ACCOUNTING_REFERENCES = "counterparty_accounting_references"
    NOMENCLATURE_ACCOUNTING_REFERENCES = "nomenclature_accounting_references"
    ACCOUNTING_DOCUMENT_REFERENCES = "accounting_document_references"
    PAYMENT_STATUS_REFERENCES = "payment_status_references"
    UNIT_CODE_REFERENCES = "unit_code_references"
    TAX_CODE_REFERENCES = "tax_code_references"


class OneCDirectoryItemSnapshot(BaseModel):
    """One directory item snapshot."""

    item_id: str
    raw_payload: dict[str, Any] = Field(default_factory=dict)
    normalized_payload: dict[str, Any] = Field(default_factory=dict)
    accounting_reference_only: bool = True


class OneCDirectorySnapshot(BaseModel):
    """Accounting directory snapshot."""

    snapshot_id: str
    directory_kind: OneCDirectoryKind
    source_name: str
    items: list[OneCDirectoryItemSnapshot] = Field(default_factory=list)
    real_1c_data: bool = False
    sanitized: bool = True
    production_allowed: bool = False


class OneCDirectoryImportBatch(BaseModel):
    """Directory import batch shell."""

    batch_id: str
    snapshot_id: str
    directory_kind: OneCDirectoryKind
    items_count: int
    status: str = "created"


class OneCDirectoryExportPackage(BaseModel):
    """Dry-run directory export package."""

    package_id: str
    directory_kind: OneCDirectoryKind
    records: list[dict[str, Any]] = Field(default_factory=list)
    dry_run: bool = True
    production_write_allowed: bool = False
    manual_approval_required: bool = True


class OneCDirectoryMappingIssue(BaseModel):
    """Directory mapping issue."""

    item_id: str
    field_name: str | None = None
    message: str
    severity: str = "warning"


def build_directory_import_batch(
    snapshot: OneCDirectorySnapshot,
) -> OneCDirectoryImportBatch:
    """Create import batch from directory snapshot."""
    return OneCDirectoryImportBatch(
        batch_id=f"directory-import-{snapshot.snapshot_id}",
        snapshot_id=snapshot.snapshot_id,
        directory_kind=snapshot.directory_kind,
        items_count=len(snapshot.items),
    )


def directory_snapshot_to_staging_records(
    snapshot: OneCDirectorySnapshot,
) -> list[OneCStagingRecord]:
    """Map directory snapshot into OneCStagingRecord objects."""
    records: list[OneCStagingRecord] = []

    for index, item in enumerate(snapshot.items, start=1):
        records.append(
            OneCStagingRecord(
                snapshot_id=snapshot.snapshot_id,
                record_type=f"directory:{snapshot.directory_kind}",
                source_row_number=index,
                one_c_id=item.item_id,
                raw_payload={
                    "source_name": snapshot.source_name,
                    "directory_kind": snapshot.directory_kind,
                    "item": item.raw_payload,
                    "accounting_reference_only": True,
                },
                normalized_payload=item.normalized_payload,
            )
        )

    return records
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/discovery.py

`SHA256=0ae3ce68c9561b6065954fd20d6d4043fee7255413da8e1a157cedcb11233a5b`

```py
"""
OneC schema/file discovery models.

Purpose:
    Provide fixture-driven schema/table/field discovery output for v0.4.

Boundary:
    Discovered 1C-like names are not canonical ForPrint contracts.
"""

from typing import Any

from pydantic import BaseModel, Field


class OneCFieldDiscovery(BaseModel):
    """Discovered field information."""

    field_name: str
    sample_type: str
    sample_value: Any | None = None


class OneCTableDiscovery(BaseModel):
    """Discovered table/collection information."""

    table_name: str
    fields: list[OneCFieldDiscovery] = Field(default_factory=list)
    records_count: int = 0


class OneCSchemaDiscoveryReport(BaseModel):
    """Schema discovery report for a sandbox/test source."""

    source_id: str
    adapter_name: str
    tables: list[OneCTableDiscovery] = Field(default_factory=list)
    canonical_truth: bool = False
    notes: str = "Discovery output only. Not canonical contract truth."


class OneCRawExtractBatch(BaseModel):
    """Raw extracted batch from sandbox/test source."""

    source_id: str
    source_name: str
    table_name: str
    records: list[dict[str, Any]] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


def discover_schema_from_records(
    source_id: str,
    adapter_name: str,
    tables: dict[str, list[dict[str, Any]]],
) -> OneCSchemaDiscoveryReport:
    """Create schema discovery report from fixture-like tables."""
    discovered_tables: list[OneCTableDiscovery] = []

    for table_name, records in tables.items():
        field_names: dict[str, Any | None] = {}

        for record in records:
            for field_name, value in record.items():
                field_names.setdefault(field_name, value)

        fields = [
            OneCFieldDiscovery(
                field_name=field_name,
                sample_type=type(sample_value).__name__,
                sample_value=sample_value,
            )
            for field_name, sample_value in field_names.items()
        ]

        discovered_tables.append(
            OneCTableDiscovery(
                table_name=table_name,
                fields=fields,
                records_count=len(records),
            )
        )

    return OneCSchemaDiscoveryReport(
        source_id=source_id,
        adapter_name=adapter_name,
        tables=discovered_tables,
    )


def create_raw_extract_batch(
    source_id: str,
    source_name: str,
    table_name: str,
    records: list[dict[str, Any]],
) -> OneCRawExtractBatch:
    """Create raw extract batch preserving source records."""
    return OneCRawExtractBatch(
        source_id=source_id,
        source_name=source_name,
        table_name=table_name,
        records=records,
        metadata={"preserve_raw_values": True},
    )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/export_detection.py

`SHA256=fa494eca6fc66debd9210f83462375393faf49520f312ab799c52bf8619a195b`

```py
"""
OneC export format detection.

Purpose:
    Detect sanitized manual/file export format where possible.
"""

from pathlib import Path

from forprint_accounting_registry_service.one_c_io.file_formats import OneCExportFormat


def detect_export_format(path: Path) -> OneCExportFormat:
    """Detect export format by file extension."""
    suffix = path.suffix.lower()

    if suffix == ".json":
        return OneCExportFormat.JSON
    if suffix == ".csv":
        return OneCExportFormat.CSV
    if suffix == ".xml":
        return OneCExportFormat.XML
    if suffix in {".yaml", ".yml"}:
        return OneCExportFormat.YAML
    if suffix in {".txt", ".dump"}:
        return OneCExportFormat.TXT_TABULAR_DUMP

    return OneCExportFormat.UNKNOWN_RAW_TEXT
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/export_packages.py

`SHA256=d192c1950d46c9cadfaccd0b8e5746db91af4c6d1d59c2c3be8586cea55615a2`

```py
"""
Dry-run 1C export package hardening.

Purpose:
    Validate future accounting export packages without live 1C writes.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.mapping import MappingIssue
from forprint_accounting_registry_service.one_c_io.types import OneCVersion


class OneCExportPackageType(StrEnum):
    """Allowed dry-run export package types."""

    INVOICE_EXPORT = "invoice_export"
    PAYMENT_EXPORT = "payment_export"
    DIRECTORY_EXPORT = "directory_export"
    ACCOUNTING_DOCUMENT_EXPORT = "accounting_document_export"


class OneCDryRunExportPackage(BaseModel):
    """Dry-run export package for future 1C adapter writes."""

    package_id: str
    package_type: OneCExportPackageType
    target_adapter: str
    target_version: OneCVersion
    records: list[dict[str, Any]] = Field(default_factory=list)

    dry_run_only: bool = True
    production_write_allowed: bool = False
    manual_approval_required: bool = True
    mapping_issues: list[MappingIssue] = Field(default_factory=list)


class OneCExportPackageValidationResult(BaseModel):
    """Validation result for dry-run export package."""

    package_id: str
    valid: bool
    errors: list[str] = Field(default_factory=list)


def validate_dry_run_export_package(
    package: OneCDryRunExportPackage,
) -> OneCExportPackageValidationResult:
    """Validate dry-run export package safety."""
    errors: list[str] = []

    if not package.dry_run_only:
        errors.append("dry_run_only must be true")

    if package.production_write_allowed:
        errors.append("production_write_allowed must be false")

    if not package.manual_approval_required:
        errors.append("manual_approval_required must be true")

    if not package.target_adapter:
        errors.append("target_adapter is required")

    return OneCExportPackageValidationResult(
        package_id=package.package_id,
        valid=not errors,
        errors=errors,
    )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/export_parsers.py

`SHA256=706c44b744757c7e3ea3be658ab0eddf45e1e8a4283c061556d4a7ce50bff0ac`

```py
"""
OneC sanitized export parsers.

Purpose:
    Parse sanitized manual/file exports into raw parsed batches.

Boundary:
    Parsed exports become accounting staging candidates only.
    They do not create CRM clients or Library product truth.
"""

from __future__ import annotations

import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.export_detection import detect_export_format
from forprint_accounting_registry_service.one_c_io.file_formats import OneCExportFormat
from forprint_accounting_registry_service.storage.models import OneCStagingRecord


class OneCExportParseIssue(BaseModel):
    """One export parse issue."""

    row_number: int | None = None
    message: str
    severity: str = "warning"


class OneCParsedExportRow(BaseModel):
    """One parsed export row."""

    row_number: int
    raw_values: dict[str, Any] = Field(default_factory=dict)
    unknown_columns: dict[str, Any] = Field(default_factory=dict)


class OneCParsedExportBatch(BaseModel):
    """Parsed sanitized export batch."""

    source_path: str
    export_format: OneCExportFormat
    target_kind: str = "generic_accounting_table_export"
    rows: list[OneCParsedExportRow] = Field(default_factory=list)
    real_1c_data: bool = False
    sanitized: bool = True
    production_allowed: bool = False


class OneCExportParserResult(BaseModel):
    """Parser result."""

    batch: OneCParsedExportBatch | None = None
    issues: list[OneCExportParseIssue] = Field(default_factory=list)
    supported: bool = True


def parse_one_c_export_file(
        path: Path, 
        target_kind: str = "generic_accounting_table_export"
) -> OneCExportParserResult:
    """Parse sanitized export file by detected format."""
    export_format = detect_export_format(path)

    if not path.exists():
        return OneCExportParserResult(
            batch=None,
            supported=False,
            issues=[OneCExportParseIssue(message=f"File not found: {path}", severity="error")],
        )

    if export_format == OneCExportFormat.JSON:
        return parse_json_export(path, target_kind)

    if export_format == OneCExportFormat.CSV:
        return parse_csv_export(path, target_kind)

    if export_format == OneCExportFormat.YAML:
        return parse_yaml_export(path, target_kind)

    if export_format == OneCExportFormat.XML:
        return parse_xml_export(path, target_kind)

    if export_format == OneCExportFormat.TXT_TABULAR_DUMP:
        return parse_txt_tabular_export(path, target_kind)

    return OneCExportParserResult(
        batch=None,
        supported=False,
        issues=[
            OneCExportParseIssue(
                message=f"Unsupported export format: {export_format}",
                severity="error",
            )
        ],
    )


def parse_json_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse JSON export fixture."""
    payload = json.loads(path.read_text(encoding="utf-8"))

    if isinstance(payload, dict):
        records = payload.get("records", [])
        sanitized = bool(payload.get("sanitized", True))
        production_allowed = bool(payload.get("production_allowed", False))
        real_1c_data = bool(payload.get("real_1c_data", False))
    elif isinstance(payload, list):
        records = payload
        sanitized = True
        production_allowed = False
        real_1c_data = False
    else:
        records = []
        sanitized = True
        production_allowed = False
        real_1c_data = False

    rows = [
        OneCParsedExportRow(row_number=index, raw_values=dict(record))
        for index, record in enumerate(records, start=1)
        if isinstance(record, dict)
    ]

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.JSON,
            target_kind=target_kind,
            rows=rows,
            sanitized=sanitized,
            production_allowed=production_allowed,
            real_1c_data=real_1c_data,
        )
    )


def parse_csv_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse CSV export fixture."""
    rows: list[OneCParsedExportRow] = []
    issues: list[OneCExportParseIssue] = []

    with path.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)

        if not reader.fieldnames:
            return OneCExportParserResult(
                batch=OneCParsedExportBatch(
                    source_path=str(path),
                    export_format=OneCExportFormat.CSV,
                    target_kind=target_kind,
                    rows=[],
                ),
                issues=[
                    OneCExportParseIssue(
                        message="CSV has no header",
                        severity="error",
                    )
                ],
            )

        for index, row in enumerate(reader, start=1):
            if None in row:
                issues.append(
                    OneCExportParseIssue(
                        row_number=index,
                        message="Malformed CSV row has extra columns",
                        severity="warning",
                    )
                )

            raw_values = {key: value for key, value in row.items() if key is not None}
            rows.append(OneCParsedExportRow(row_number=index, raw_values=raw_values))

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.CSV,
            target_kind=target_kind,
            rows=rows,
        ),
        issues=issues,
    )


def parse_yaml_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse YAML export fixture."""
    payload = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    records = payload.get("records", payload.get("items", payload.get("rows", [])))

    rows = [
        OneCParsedExportRow(row_number=index, raw_values=dict(record))
        for index, record in enumerate(records, start=1)
        if isinstance(record, dict)
    ]

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.YAML,
            target_kind=target_kind,
            rows=rows,
            sanitized=bool(payload.get("sanitized", True)),
            production_allowed=bool(payload.get("production_allowed", False)),
            real_1c_data=bool(payload.get("real_1c_data", False)),
        )
    )


def parse_xml_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse simple XML export if possible; return issue on malformed XML."""
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except ET.ParseError as exc:
        return OneCExportParserResult(
            batch=None,
            supported=False,
            issues=[
                OneCExportParseIssue(
                    message=f"Unsupported or malformed XML export: {exc}",
                    severity="error",
                )
            ],
        )

    rows: list[OneCParsedExportRow] = []

    for index, element in enumerate(root.findall(".//record"), start=1):
        raw_values = {child.tag: child.text for child in list(element)}
        rows.append(OneCParsedExportRow(row_number=index, raw_values=raw_values))

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.XML,
            target_kind=target_kind,
            rows=rows,
        )
    )


def parse_txt_tabular_export(path: Path, target_kind: str) -> OneCExportParserResult:
    """Parse simple tab-separated dump."""
    rows: list[OneCParsedExportRow] = []
    lines = path.read_text(encoding="utf-8").splitlines()

    if not lines:
        return OneCExportParserResult(
            batch=OneCParsedExportBatch(
                source_path=str(path),
                export_format=OneCExportFormat.TXT_TABULAR_DUMP,
                target_kind=target_kind,
                rows=[],
            )
        )

    headers = lines[0].split("\t")

    for index, line in enumerate(lines[1:], start=1):
        values = line.split("\t")
        rows.append(
            OneCParsedExportRow(
                row_number=index,
                raw_values=dict(zip(headers, values, strict=False)),
            )
        )

    return OneCExportParserResult(
        batch=OneCParsedExportBatch(
            source_path=str(path),
            export_format=OneCExportFormat.TXT_TABULAR_DUMP,
            target_kind=target_kind,
            rows=rows,
        )
    )


def parsed_export_batch_to_staging_records(
    batch: OneCParsedExportBatch,
    snapshot_id: str,
) -> list[OneCStagingRecord]:
    """Convert parsed export rows to staging records."""
    return [
        OneCStagingRecord(
            snapshot_id=snapshot_id,
            record_type=f"parsed_export:{batch.target_kind}",
            source_row_number=row.row_number,
            raw_payload={
                "source_path": batch.source_path,
                "export_format": batch.export_format,
                "row": row.raw_values,
            },
            normalized_payload={},
        )
        for row in batch.rows
    ]
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/file_formats.py

`SHA256=cb12d5275234e08319d7063703b8447df91cc343d6bb2d0abc70d6af590f1b31`

```py
"""
OneC export file format types.

Purpose:
    Describe supported sanitized manual/file export formats.
"""

from enum import StrEnum


class OneCExportFormat(StrEnum):
    """Supported parser format markers."""

    JSON = "json"
    CSV = "csv"
    XML = "xml"
    YAML = "yaml"
    TXT_TABULAR_DUMP = "txt_tabular_dump"
    UNKNOWN_RAW_TEXT = "unknown_raw_text"
    UNSUPPORTED = "unsupported"
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/import_pipeline.py

`SHA256=de309910f32053c6b72fd78f5a878ef562968c0679c8dbca039214c3f64630ba`

```py
"""
OneC sandbox import pipeline.

Purpose:
    Offline pipeline from sanitized export/test source to raw snapshot, staging,
    mapping issues, and import summary.

Boundary:
    No live 1C connection.
    No production sync.
    No foreign-domain ownership.
"""

from datetime import UTC, datetime
from pathlib import Path
from uuid import uuid4

from pydantic import BaseModel, Field
from sqlmodel import Session

from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
    parsed_export_batch_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    apply_mapping_policy,
)
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    ensure_not_production_source,
)
from forprint_accounting_registry_service.one_c_io.sanitization import (
    OneCSanitizationMetadata,
    OneCSanitizationStatus,
    assert_source_is_sanitized,
)
from forprint_accounting_registry_service.services.mapping_issue_registry import (
    persist_mapping_result,
)
from forprint_accounting_registry_service.storage.models import OneCRawSnapshot


class OneCImportPipelineStatus(str):
    """Pipeline status constants."""

    COMPLETED = "completed"
    COMPLETED_WITH_WARNINGS = "completed_with_warnings"
    BLOCKED_BY_MAPPING_ISSUES = "blocked_by_mapping_issues"
    UNSUPPORTED_SOURCE = "unsupported_source"
    FAILED = "failed"


class OneCImportPipelineResult(BaseModel):
    """Import pipeline result summary."""

    pipeline_run_id: str = Field(default_factory=lambda: str(uuid4()))
    source_id: str
    source_kind: str
    raw_snapshot_count: int = 0
    staging_record_count: int = 0
    mapping_issue_count: int = 0
    blocked_record_count: int = 0
    manual_review_required_count: int = 0
    status: str
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class OneCSandboxImportPipeline:
    """Offline sanitized source import pipeline."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def run_file_export_import(
        self,
        source: OneCSandboxSource,
        export_path: Path,
        mapping_definitions: list[FieldMappingDefinition],
        target_kind: str = "generic_accounting_table_export",
    ) -> OneCImportPipelineResult:
        """Run sanitized export import into raw snapshot/staging/mapping diagnostics."""
        try:
            ensure_not_production_source(source)
            assert_source_is_sanitized(
                OneCSanitizationMetadata(
                    status=(OneCSanitizationStatus.SANITIZED 
                            if source.sanitized 
                            else OneCSanitizationStatus.NOT_SANITIZED
                    ),
                    real_1c_data=True,
                    sanitized=source.sanitized,
                    production_allowed=source.production_allowed,
                )
            )
        except Exception as exc:  # noqa: BLE001
            return OneCImportPipelineResult(
                source_id=source.source_id,
                source_kind=source.source_kind,
                status=OneCImportPipelineStatus.FAILED,
                errors=[str(exc)],
            )

        parser_result = parse_one_c_export_file(export_path, target_kind=target_kind)

        if not parser_result.supported or parser_result.batch is None:
            return OneCImportPipelineResult(
                source_id=source.source_id,
                source_kind=source.source_kind,
                status=OneCImportPipelineStatus.UNSUPPORTED_SOURCE,
                errors=[issue.message for issue in parser_result.issues],
            )

        snapshot = OneCRawSnapshot(
            snapshot_type=f"file_export:{target_kind}",
            source_name=source.source_id,
            file_name=export_path.name,
            file_path=str(export_path),
            status="stored",
            raw_metadata={
                "source_kind": source.source_kind,
                "export_format": parser_result.batch.export_format,
                "sanitized": parser_result.batch.sanitized,
                "production_allowed": parser_result.batch.production_allowed,
            },
        )
        self.session.add(snapshot)
        self.session.commit()
        self.session.refresh(snapshot)

        staging_records = parsed_export_batch_to_staging_records(
            parser_result.batch,
            snapshot_id=snapshot.id,
        )

        mapping_issue_count = 0
        manual_review_count = 0
        blocked_count = 0

        for staging_record, parsed_row in zip(
                                            staging_records, 
                                            parser_result.batch.rows, 
                                            strict=False
        ):
            mapping_result = apply_mapping_policy(
                source_payload=parsed_row.raw_values,
                definitions=mapping_definitions,
            )
            staging_record.normalized_payload = mapping_result.mapped_payload
            self.session.add(staging_record)
            self.session.commit()
            self.session.refresh(staging_record)

            stored_issues = persist_mapping_result(
                self.session,
                mapping_result,
                staging_record_id=staging_record.id,
                raw_snapshot_id=snapshot.id,
            )
            mapping_issue_count += len(stored_issues)
            manual_review_count += sum(
                1 for issue in stored_issues if issue.status == "manual_review_required"
            )
            blocking_statuses = {
                "manual_review_required",
                "blocked_until_mapped",
            }
            blocked_count += sum(
                1 for issue in stored_issues if issue.status in blocking_statuses
            )

        status = OneCImportPipelineStatus.COMPLETED
        if mapping_issue_count:
            status = OneCImportPipelineStatus.COMPLETED_WITH_WARNINGS
        if blocked_count:
            status = OneCImportPipelineStatus.BLOCKED_BY_MAPPING_ISSUES

        return OneCImportPipelineResult(
            source_id=source.source_id,
            source_kind=source.source_kind,
            raw_snapshot_count=1,
            staging_record_count=len(staging_records),
            mapping_issue_count=mapping_issue_count,
            blocked_record_count=blocked_count,
            manual_review_required_count=manual_review_count,
            status=status,
            warnings=[issue.message for issue in parser_result.issues],
        )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/mapping.py

`SHA256=635183a9e6395a6b018d4c69d397a972afa669d6e2858208405546c15f461b01`

```py
"""
OneC mapping/default policy.

Purpose:
    Safely map raw 1C-like fields into staging/normalized payloads.

Boundary:
    Critical accounting values must never be guessed silently.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.types import (
    DefaultValueCategory,
    FieldCriticality,
)


class MappingIssueType(StrEnum):
    """Mapping issue categories."""

    UNMAPPED_FIELD = "unmapped_field"
    REQUIRED_FIELD_MISSING = "required_field_missing"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"
    BLOCKED_UNTIL_MAPPED = "blocked_until_mapped"


class FieldMappingDefinition(BaseModel):
    """One source-to-target field mapping definition."""

    source_field: str
    target_field: str
    required: bool = False
    criticality: FieldCriticality = FieldCriticality.NORMAL
    default_value: Any | None = None
    default_category: DefaultValueCategory | None = None


class MappingIssue(BaseModel):
    """One mapping issue found during safe normalization."""

    issue_type: MappingIssueType
    source_field: str | None = None
    target_field: str | None = None
    severity: str = "warning"
    message: str


class UnmappedFieldRecord(BaseModel):
    """Raw source field that has no mapping definition."""

    field_name: str
    value: Any


class FieldMappingResult(BaseModel):
    """Result of applying mapping/default policy."""

    mapped_payload: dict[str, Any] = Field(default_factory=dict)
    issues: list[MappingIssue] = Field(default_factory=list)
    unmapped_fields: list[UnmappedFieldRecord] = Field(default_factory=list)


def apply_mapping_policy(
    source_payload: dict[str, Any],
    definitions: list[FieldMappingDefinition],
    preserve_unknown_fields: bool = True,
) -> FieldMappingResult:
    """
    Apply explicit mapping/default rules.

    Critical missing fields become manual-review issues by default.
    Unknown fields are captured, not discarded silently.
    """
    result = FieldMappingResult()
    mapped_source_fields = {definition.source_field for definition in definitions}

    for definition in definitions:
        if definition.source_field in source_payload:
            result.mapped_payload[definition.target_field] = source_payload[
                definition.source_field
            ]
            continue

        if definition.default_value is not None and definition.default_category not in {
            DefaultValueCategory.MANUAL_REVIEW_REQUIRED,
            DefaultValueCategory.BLOCKED_UNTIL_MAPPED,
        }:
            result.mapped_payload[definition.target_field] = definition.default_value
            continue

        if definition.required:
            issue_type = MappingIssueType.REQUIRED_FIELD_MISSING
            severity = "error"

            if definition.criticality == FieldCriticality.CRITICAL:
                issue_type = MappingIssueType.MANUAL_REVIEW_REQUIRED
                severity = "critical"

            result.issues.append(
                MappingIssue(
                    issue_type=issue_type,
                    source_field=definition.source_field,
                    target_field=definition.target_field,
                    severity=severity,
                    message=(
                        "Required mapping field is missing and must be reviewed "
                        f"explicitly: {definition.source_field}"
                    ),
                )
            )

    if preserve_unknown_fields:
        for field_name, value in source_payload.items():
            if field_name not in mapped_source_fields:
                result.unmapped_fields.append(
                    UnmappedFieldRecord(field_name=field_name, value=value)
                )
                result.issues.append(
                    MappingIssue(
                        issue_type=MappingIssueType.UNMAPPED_FIELD,
                        source_field=field_name,
                        severity="info",
                        message=f"Unmapped source field captured: {field_name}",
                    )
                )

    return result
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/policies.py

`SHA256=9b37037b639485177e3a31b1cb595716e951091c449afadeb470936ae2f533ab`

```py
"""
OneC I/O policy models.

Purpose:
    Keep 1C read/write strategy explicit and safe.

Boundary:
    Live writes are forbidden by default.
    Direct DB access is read-only and test-copy-only.
"""

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.types import (
    OneCAdapterCapability,
    OneCChannel,
    OneCVersion,
)


class OneCAdapterPolicy(BaseModel):
    """Safety policy attached to every 1C adapter placeholder."""

    adapter_name: str
    version: OneCVersion
    channel: OneCChannel
    capabilities: list[OneCAdapterCapability] = Field(default_factory=list)

    read_only: bool = True
    production_allowed: bool = False
    writes_allowed: bool = False
    requires_test_copy: bool = True
    dry_run_only: bool = True


class OneCWritePolicyViolation(RuntimeError):
    """Raised when a forbidden 1C write is requested."""


def validate_live_write_is_forbidden(policy: OneCAdapterPolicy) -> None:
    """Raise if adapter policy would allow live writes."""
    if policy.writes_allowed:
        raise OneCWritePolicyViolation(
            f"{policy.adapter_name} must not allow live writes in v0.3."
        )

    if not policy.dry_run_only:
        raise OneCWritePolicyViolation(
            f"{policy.adapter_name} must remain dry-run-only in v0.3."
        )


def build_direct_db_readonly_policy(
    version: OneCVersion = OneCVersion.UNKNOWN_FUTURE_VERSION,
) -> OneCAdapterPolicy:
    """Build safe policy for direct DB read-only exploration."""
    return OneCAdapterPolicy(
        adapter_name="OneCDirectDbReadonlyAdapter",
        version=version,
        channel=OneCChannel.DIRECT_DB_READONLY,
        capabilities=[OneCAdapterCapability.DIRECT_DB_READONLY_DISCOVERY],
        read_only=True,
        production_allowed=False,
        writes_allowed=False,
        requires_test_copy=True,
        dry_run_only=True,
    )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/reports.py

`SHA256=a124ed9767a55417055d7f831c081078e74a68c885db1a75ab6fdecc7cb8c152`

```py
"""
OneC report extraction interface.

Purpose:
    Represent accounting report-like snapshots extracted from 1C-like data.

Boundary:
    These are Accounting Registry report snapshots.
    They are not CRM dashboards or Operational Registry reports.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.mapping import MappingIssue


class OneCReportCategory(StrEnum):
    """Supported placeholder report categories."""

    COUNTERPARTY_BALANCE_SNAPSHOT = "counterparty_balance_snapshot"
    INVOICE_REGISTER_SNAPSHOT = "invoice_register_snapshot"
    PAYMENT_REGISTER_SNAPSHOT = "payment_register_snapshot"
    SALES_TURNOVER_SNAPSHOT = "sales_turnover_snapshot"
    MUTUAL_SETTLEMENT_SNAPSHOT = "mutual_settlement_snapshot"
    NOMENCLATURE_TURNOVER_SNAPSHOT = "nomenclature_turnover_snapshot"


class OneCReportDefinition(BaseModel):
    """One report definition placeholder."""

    report_code: str
    category: OneCReportCategory
    title: str
    accounting_only: bool = True


class OneCReportRequest(BaseModel):
    """Request for report extraction from fixture/test data."""

    request_id: str
    report_code: str
    period_from: str | None = None
    period_to: str | None = None
    source_name: str | None = None


class OneCReportRow(BaseModel):
    """One report row preserving raw values."""

    row_number: int
    raw_values: dict[str, Any] = Field(default_factory=dict)
    normalized_values: dict[str, Any] = Field(default_factory=dict)


class OneCReportSnapshot(BaseModel):
    """Extracted accounting report snapshot."""

    snapshot_id: str
    definition: OneCReportDefinition
    request: OneCReportRequest
    rows: list[OneCReportRow] = Field(default_factory=list)
    real_1c_data: bool = False
    sanitized: bool = True
    production_allowed: bool = False


class OneCReportExtractionResult(BaseModel):
    """Report extraction result with optional mapping issues."""

    snapshot: OneCReportSnapshot
    mapping_issues: list[MappingIssue] = Field(default_factory=list)
    status: str = "created"


def generate_report_snapshot_from_fixture(
    snapshot_id: str,
    definition: OneCReportDefinition,
    request: OneCReportRequest,
    rows: list[dict[str, Any]],
) -> OneCReportSnapshot:
    """Create report snapshot from sanitized fixture rows."""
    return OneCReportSnapshot(
        snapshot_id=snapshot_id,
        definition=definition,
        request=request,
        rows=[
            OneCReportRow(
                row_number=index,
                raw_values=row,
                normalized_values={},
            )
            for index, row in enumerate(rows, start=1)
        ],
    )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/sandbox_sources.py

`SHA256=8240fe2922427fbc87c601be9da6faa34ec3fceca41d1d71617adc8a9c7fd454`

```py
"""
OneC sandbox source manager.

Purpose:
    Manage local/test/sanitized 1C-like sources for v0.4 discovery.

Boundary:
    Sources are non-production by default.
    Destructive tests require disposable source + explicit flag.
"""

from enum import StrEnum

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.types import (
    OneCChannel,
    OneCVersion,
)


class OneCSourceKind(StrEnum):
    """Allowed source kinds for 1C sandbox/discovery inputs."""

    FILE_DATABASE_COPY = "file_database_copy"
    SQL_DUMP_COPY = "sql_dump_copy"
    MANUAL_EXPORT_FOLDER = "manual_export_folder"
    FILE_EXCHANGE_FOLDER = "file_exchange_folder"
    JSON_FIXTURE = "json_fixture"
    CSV_FIXTURE = "csv_fixture"
    XML_FIXTURE = "xml_fixture"
    UNKNOWN_SANDBOX_SOURCE = "unknown_sandbox_source"


class OneCSourceSafetyLevel(StrEnum):
    """Safety level of a local 1C-like source."""

    READONLY_FIXTURE = "readonly_fixture"
    SANDBOX_READONLY = "sandbox_readonly"
    SANDBOX_DISPOSABLE = "sandbox_disposable"
    DESTRUCTIVE_TEST_COPY = "destructive_test_copy"
    PRODUCTION_FORBIDDEN = "production_forbidden"


class OneCSandboxSource(BaseModel):
    """One local/test/sanitized 1C source declaration."""

    source_id: str
    source_kind: OneCSourceKind
    path: str
    safety_level: OneCSourceSafetyLevel

    version: OneCVersion = OneCVersion.UNKNOWN_FUTURE_VERSION
    channel: OneCChannel = OneCChannel.FILE_EXCHANGE

    disposable: bool = False
    write_tests_allowed: bool = False
    sanitized: bool = True
    production_allowed: bool = False

    metadata: dict[str, str | bool | int | float | None] = Field(default_factory=dict)


class OneCSourceSafetyError(RuntimeError):
    """Raised when a sandbox source violates safety policy."""


def ensure_not_production_source(source: OneCSandboxSource) -> None:
    """Reject production-like sources."""
    if source.production_allowed:
        raise OneCSourceSafetyError(
            f"Production source is forbidden for v0.4: {source.source_id}"
        )


def ensure_destructive_test_allowed(
    source: OneCSandboxSource,
    allow_destructive_flag: bool,
) -> None:
    """Validate destructive sandbox write requirements."""
    ensure_not_production_source(source)

    if not allow_destructive_flag:
        raise OneCSourceSafetyError("Destructive test flag is disabled.")

    if not source.disposable:
        raise OneCSourceSafetyError("Destructive tests require disposable source.")

    if not source.write_tests_allowed:
        raise OneCSourceSafetyError("Source does not allow write tests.")

    if source.safety_level not in {
        OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        OneCSourceSafetyLevel.DESTRUCTIVE_TEST_COPY,
    }:
        raise OneCSourceSafetyError(
            f"Unsafe source level for destructive test: {source.safety_level}"
        )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/sandbox_write.py

`SHA256=b2687b324e4d5bc54b4271c50c9bb3a175b73229ffbd6d608287bcc55444932a`

```py
"""
OneC sandbox-only write experiment boundary.

Purpose:
    Prepare write plans and safety checks for disposable local test copies only.

Boundary:
    No live 1C write.
    No production write.
    No automatic posting.
    No mutation of original source fixture in tests.
"""

from enum import StrEnum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceSafetyError,
    ensure_destructive_test_allowed,
)
from forprint_accounting_registry_service.one_c_io.test_database_registry import (
    OneCWorkingCopyManifest,
    calculate_file_checksum,
)


class OneCWriteOperationType(StrEnum):
    """Allowed write operation preview types."""

    UPSERT_DIRECTORY_ITEM = "upsert_directory_item"
    CREATE_ACCOUNTING_DOCUMENT = "create_accounting_document"
    UPDATE_ACCOUNTING_REFERENCE = "update_accounting_reference"


class OneCWriteOperation(BaseModel):
    """One write operation preview."""

    operation_type: OneCWriteOperationType
    target_name: str
    payload: dict[str, Any] = Field(default_factory=dict)


class OneCWritePlan(BaseModel):
    """Write plan for sandbox experiment."""

    plan_id: str
    operations: list[OneCWriteOperation] = Field(default_factory=list)
    dry_run: bool = True
    manual_approval_required: bool = True


class OneCWriteSafetyCheck(BaseModel):
    """Write safety check result."""

    passed: bool
    message: str


class OneCWriteExperimentResult(BaseModel):
    """Sandbox write experiment result."""

    experiment_id: str
    plan_id: str
    applied: bool = False
    safety_checks: list[OneCWriteSafetyCheck] = Field(default_factory=list)
    result_metadata: dict[str, Any] = Field(default_factory=dict)


def run_sandbox_write_experiment(
    source: OneCSandboxSource,
    plan: OneCWritePlan,
    allow_destructive_flag: bool = False,
    working_copy: OneCWorkingCopyManifest | None = None,
) -> OneCWriteExperimentResult:
    """
    Run sandbox write experiment boundary.

    This does not mutate real source data.
    If non-dry-run is ever simulated, it requires working copy manifest.
    """
    safety_checks: list[OneCWriteSafetyCheck] = []

    try:
        ensure_destructive_test_allowed(
            source=source,
            allow_destructive_flag=allow_destructive_flag,
        )
    except OneCSourceSafetyError as exc:
        safety_checks.append(OneCWriteSafetyCheck(passed=False, message=str(exc)))
        return OneCWriteExperimentResult(
            experiment_id=f"experiment-{plan.plan_id}",
            plan_id=plan.plan_id,
            applied=False,
            safety_checks=safety_checks,
            result_metadata={"blocked": True},
        )

    if not plan.dry_run and working_copy is None:
        safety_checks.append(
            OneCWriteSafetyCheck(
                passed=False,
                message="Non-dry-run sandbox write requires working copy manifest.",
            )
        )
        return OneCWriteExperimentResult(
            experiment_id=f"experiment-{plan.plan_id}",
            plan_id=plan.plan_id,
            applied=False,
            safety_checks=safety_checks,
            result_metadata={"blocked": True, "missing_working_copy": True},
        )

    if working_copy is not None:
        if working_copy.original_source_path == working_copy.working_copy_path:
            safety_checks.append(
                OneCWriteSafetyCheck(
                    passed=False,
                    message="Working copy must be separate from original source.",
                )
            )
            return OneCWriteExperimentResult(
                experiment_id=f"experiment-{plan.plan_id}",
                plan_id=plan.plan_id,
                applied=False,
                safety_checks=safety_checks,
                result_metadata={"blocked": True, "same_original_and_working_copy": True},
            )

    if plan.dry_run:
        safety_checks.append(
            OneCWriteSafetyCheck(
                passed=True,
                message="Dry-run write plan validated without mutation.",
            )
        )
        return OneCWriteExperimentResult(
            experiment_id=f"experiment-{plan.plan_id}",
            plan_id=plan.plan_id,
            applied=False,
            safety_checks=safety_checks,
            result_metadata={"dry_run": True},
        )

    original_checksum_before = None
    original_checksum_after = None

    if working_copy and working_copy.original_source_path:
        original_path = Path(working_copy.original_source_path)
        if original_path.exists():
            original_checksum_before = calculate_file_checksum(original_path).value
            original_checksum_after = calculate_file_checksum(original_path).value

    safety_checks.append(
        OneCWriteSafetyCheck(
            passed=True,
            message="Disposable sandbox write experiment allowed on working copy only.",
        )
    )
    return OneCWriteExperimentResult(
        experiment_id=f"experiment-{plan.plan_id}",
        plan_id=plan.plan_id,
        applied=True,
        safety_checks=safety_checks,
        result_metadata={
            "disposable_source": True,
            "working_copy": working_copy.working_copy_path if working_copy else None,
            "original_checksum_before": original_checksum_before,
            "original_checksum_after": original_checksum_after,
            "original_source_unchanged": original_checksum_before == original_checksum_after,
        },
    )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/sanitization.py

`SHA256=30e652ecd4d0f1d0839b3093685ee6af03fbb950d94607565c6cb1811a59918f`

```py
"""
OneC sanitization policy.

Purpose:
    Treat every real/test 1C-like source as dangerous until it is explicitly marked sanitized.

Boundary:
    This module does not sanitize real production data automatically.
    It only validates metadata and safety flags.
"""

from enum import StrEnum

from pydantic import BaseModel


class OneCSanitizationStatus(StrEnum):
    """Sanitization status for local/test 1C-like sources."""

    UNKNOWN = "unknown"
    SANITIZED = "sanitized"
    NOT_SANITIZED = "not_sanitized"
    SYNTHETIC = "synthetic"
    ANONYMIZED_SAMPLE = "anonymized_sample"


class OneCSanitizationError(RuntimeError):
    """Raised when a source is not safe for v0.5 processing."""


class OneCSanitizationMetadata(BaseModel):
    """Sanitization metadata for committed examples or local test sources."""

    status: OneCSanitizationStatus = OneCSanitizationStatus.UNKNOWN
    real_1c_data: bool = False
    sanitized: bool = False
    production_allowed: bool = False
    notes: str | None = None


def assert_source_is_sanitized(metadata: OneCSanitizationMetadata) -> None:
    """Reject unsanitized or production-allowed source metadata."""
    if metadata.production_allowed:
        raise OneCSanitizationError("Production sources are forbidden in v0.5.")

    if metadata.real_1c_data and metadata.status not in {
        OneCSanitizationStatus.SANITIZED,
        OneCSanitizationStatus.ANONYMIZED_SAMPLE,
    }:
        raise OneCSanitizationError("Real 1C-like data must be sanitized/anonymized.")

    if not metadata.sanitized and metadata.status not in {
        OneCSanitizationStatus.SYNTHETIC,
        OneCSanitizationStatus.SANITIZED,
        OneCSanitizationStatus.ANONYMIZED_SAMPLE,
    }:
        raise OneCSanitizationError("Source is not marked as sanitized.")
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/schema_probe.py

`SHA256=3bfe37e8303e0ee6ddd664bfd4f298be1f8c071914340604600cb05cdbb4ddcc`

```py
"""
OneC schema probe.

Purpose:
    Probe real/sanitized test sources gracefully.

Boundary:
    Unsupported sources must return diagnostics instead of crashing.
"""

from pathlib import Path

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.discovery import (
    OneCSchemaDiscoveryReport,
    discover_schema_from_records,
)
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    ensure_not_production_source,
)


class OneCSchemaProbeResult(BaseModel):
    """Schema probe result."""

    source_id: str
    supported: bool
    status: str
    report: OneCSchemaDiscoveryReport | None = None
    diagnostics: list[str] = Field(default_factory=list)


def probe_sanitized_source_schema(
    source: OneCSandboxSource,
    fixture_tables: dict[str, list[dict[str, object]]] | None = None,
) -> OneCSchemaProbeResult:
    """Probe source schema from fixture tables or return unsupported diagnostics."""
    ensure_not_production_source(source)

    if fixture_tables is not None:
        return OneCSchemaProbeResult(
            source_id=source.source_id,
            supported=True,
            status="completed",
            report=discover_schema_from_records(
                source_id=source.source_id,
                adapter_name="OneCSchemaProbe",
                tables=fixture_tables,
            ),
        )

    path = Path(source.path)

    if not path.exists():
        return OneCSchemaProbeResult(
            source_id=source.source_id,
            supported=False,
            status="unsupported_source",
            diagnostics=[
                "Source path does not exist in local sandbox.",
                "Manual export or external parser is recommended.",
            ],
        )

    if path.suffix.lower() in {".1cd", ".dt", ".cf", ".db", ".sqlite", ".sqlite3"}:
        return OneCSchemaProbeResult(
            source_id=source.source_id,
            supported=False,
            status="unsupported_source",
            diagnostics=[
                "Binary/database-like source detected.",
                "No unsafe direct parser is implemented in v0.5.",
                "Manual export or external parser is recommended.",
            ],
        )

    return OneCSchemaProbeResult(
        source_id=source.source_id,
        supported=False,
        status="unsupported_source",
        diagnostics=["Source detected but no parser is available for schema probing."],
    )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/source_manifest.py

`SHA256=67c222ea6ea05d5e1201b3bcda906c37f523a0d6d3513481e86878e14c3c6c9f`

```py
"""
OneC source manifest.

Purpose:
    Serialize/read local sandbox source declarations.
"""

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
)


class OneCSourceManifest(BaseModel):
    """Manifest of local/test 1C-like sources."""

    fixture_status: str = "example"
    real_1c_data: bool = False
    sanitized: bool = True
    production_allowed: bool = False
    sources: list[OneCSandboxSource] = Field(default_factory=list)

    def add_source(self, source: OneCSandboxSource) -> None:
        """Add sandbox source to manifest."""
        self.sources.append(source)

    def get_source(self, source_id: str) -> OneCSandboxSource | None:
        """Get sandbox source by ID."""
        for source in self.sources:
            if source.source_id == source_id:
                return source
        return None

    def to_json_string(self) -> str:
        """Serialize manifest to JSON."""
        return self.model_dump_json(indent=2)

    @classmethod
    def from_json_string(cls, value: str) -> "OneCSourceManifest":
        """Deserialize manifest from JSON."""
        return cls.model_validate_json(value)
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/staging.py

`SHA256=bb2543ae4ec57e02ba1359576616e709c7236491d09cfa529db306700e8baa99`

```py
"""
Mapping extracted 1C-like data into Accounting Registry staging.

Purpose:
    Convert raw extracts, directory snapshots, and report snapshots into
    OneCStagingRecord objects.

Boundary:
    Staging records remain accounting-only.
"""

from forprint_accounting_registry_service.one_c_io.directories import (
    OneCDirectorySnapshot,
    directory_snapshot_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.discovery import OneCRawExtractBatch
from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    FieldMappingResult,
    apply_mapping_policy,
)
from forprint_accounting_registry_service.one_c_io.reports import OneCReportSnapshot
from forprint_accounting_registry_service.storage.models import OneCStagingRecord


def raw_extract_batch_to_staging_records(
    batch: OneCRawExtractBatch,
) -> list[OneCStagingRecord]:
    """Convert raw extract batch to staging records."""
    records: list[OneCStagingRecord] = []

    for index, item in enumerate(batch.records, start=1):
        records.append(
            OneCStagingRecord(
                snapshot_id=batch.source_id,
                record_type=f"raw_extract:{batch.table_name}",
                source_row_number=index,
                raw_payload={
                    "source_name": batch.source_name,
                    "table_name": batch.table_name,
                    "record": item,
                },
                normalized_payload={},
            )
        )

    return records


def report_snapshot_to_staging_records(
    snapshot: OneCReportSnapshot,
) -> list[OneCStagingRecord]:
    """Convert report snapshot to staging records."""
    records: list[OneCStagingRecord] = []

    for row in snapshot.rows:
        records.append(
            OneCStagingRecord(
                snapshot_id=snapshot.snapshot_id,
                record_type=f"report:{snapshot.definition.category}",
                source_row_number=row.row_number,
                raw_payload={
                    "report_code": snapshot.definition.report_code,
                    "report_category": snapshot.definition.category,
                    "row": row.raw_values,
                    "accounting_only": True,
                },
                normalized_payload=row.normalized_values,
            )
        )

    return records


def directory_import_to_staging_records(
    snapshot: OneCDirectorySnapshot,
) -> list[OneCStagingRecord]:
    """Convert directory snapshot to staging records."""
    return directory_snapshot_to_staging_records(snapshot)


def apply_mapping_to_staging_payload(
    source_payload: dict[str, object],
    definitions: list[FieldMappingDefinition],
) -> FieldMappingResult:
    """Apply mapping policy before or during staging normalization."""
    return apply_mapping_policy(source_payload=source_payload, definitions=definitions)
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/test_database_registry.py

`SHA256=788b5b279c3aff8ad3a68d2f51d0db954dc52d5ac9e60e754dce01361d2904f2`

```py
"""
OneC sanitized test database registry.

Purpose:
    Register local sanitized/disposable test DB copies safely.

Boundary:
    Real or copied DB files must stay in gitignored local_sandbox paths.
    Original source must never be mutated by tests.
"""

import hashlib
import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSourceKind,
    OneCSourceSafetyError,
)
from forprint_accounting_registry_service.one_c_io.sanitization import (
    OneCSanitizationMetadata,
    OneCSanitizationStatus,
    assert_source_is_sanitized,
)
from forprint_accounting_registry_service.one_c_io.types import OneCVersion


def utc_now() -> datetime:
    """Return timezone-aware UTC datetime."""
    return datetime.now(UTC)


class OneCSourceChecksum(BaseModel):
    """Checksum metadata for local test source files."""

    algorithm: str = "sha256"
    value: str
    file_path: str


class OneCTestDatabaseSource(BaseModel):
    """Sanitized local/test 1C database source declaration."""

    source_id: str = Field(default_factory=lambda: str(uuid4()))
    source_kind: OneCSourceKind = OneCSourceKind.FILE_DATABASE_COPY
    one_c_version: OneCVersion = OneCVersion.UNKNOWN_FUTURE_VERSION
    source_path: str

    is_sanitized: bool = True
    is_disposable: bool = False
    production_allowed: bool = False
    read_only: bool = True
    writes_allowed: bool = False
    destructive_write_allowed: bool = False

    checksum: OneCSourceChecksum | None = None
    created_at: datetime = Field(default_factory=utc_now)
    notes: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class OneCTestDatabaseManifest(BaseModel):
    """Manifest of registered sanitized local test DB sources."""

    fixture_status: str = "local_manifest"
    production_allowed: bool = False
    sources: list[OneCTestDatabaseSource] = Field(default_factory=list)

    def register(self, source: OneCTestDatabaseSource) -> None:
        """Register source after safety validation."""
        validate_test_database_source(source)
        self.sources.append(source)

    def get_source(self, source_id: str) -> OneCTestDatabaseSource | None:
        """Find source by ID."""
        for source in self.sources:
            if source.source_id == source_id:
                return source
        return None


class OneCWorkingCopyManifest(BaseModel):
    """Working copy declaration separate from original source."""

    working_copy_id: str = Field(default_factory=lambda: str(uuid4()))
    original_source_id: str
    original_source_path: str
    working_copy_path: str
    original_checksum: OneCSourceChecksum | None = None
    working_copy_checksum: OneCSourceChecksum | None = None
    disposable: bool = True
    created_at: datetime = Field(default_factory=utc_now)


def calculate_file_checksum(path: Path, algorithm: str = "sha256") -> OneCSourceChecksum:
    """Calculate file checksum if file exists."""
    digest = hashlib.new(algorithm)

    with path.open("rb") as file_obj:
        for chunk in iter(lambda: file_obj.read(1024 * 1024), b""):
            digest.update(chunk)

    return OneCSourceChecksum(
        algorithm=algorithm,
        value=digest.hexdigest(),
        file_path=str(path),
    )


def validate_test_database_source(source: OneCTestDatabaseSource) -> None:
    """Validate sanitized test DB source safety."""
    if source.production_allowed:
        raise OneCSourceSafetyError("Production source is forbidden.")

    metadata = OneCSanitizationMetadata(
        status=(OneCSanitizationStatus.SANITIZED 
                if source.is_sanitized 
                else OneCSanitizationStatus.NOT_SANITIZED
        ),
        real_1c_data=True,
        sanitized=source.is_sanitized,
        production_allowed=source.production_allowed,
    )
    assert_source_is_sanitized(metadata)

    if source.writes_allowed or source.destructive_write_allowed:
        if not source.is_disposable:
            raise OneCSourceSafetyError(
                "Write-enabled test DB source must be disposable."
            )

        if not source.metadata.get("sandbox_mode", False):
            raise OneCSourceSafetyError(
                "Write-enabled test DB source requires sandbox_mode metadata."
            )

    if not source.read_only and not source.is_disposable:
        raise OneCSourceSafetyError("Non-read-only source must be disposable.")


def register_sanitized_test_database_source(
    source_path: Path,
    source_id: str,
    is_disposable: bool = False,
    sandbox_mode: bool = False,
) -> OneCTestDatabaseSource:
    """Register sanitized test DB source and calculate checksum if file exists."""
    checksum = calculate_file_checksum(source_path) if source_path.exists() else None

    source = OneCTestDatabaseSource(
        source_id=source_id,
        source_path=str(source_path),
        is_sanitized=True,
        is_disposable=is_disposable,
        checksum=checksum,
        metadata={"sandbox_mode": sandbox_mode},
    )
    validate_test_database_source(source)
    return source


def create_working_copy_manifest(
    source: OneCTestDatabaseSource,
    working_copy_path: Path,
    copy_file: bool = False,
) -> OneCWorkingCopyManifest:
    """
    Declare working copy separate from original source.

    If copy_file=True and original exists, copy source to working path.
    Tests should use small synthetic files only.
    """
    original_path = Path(source.source_path)

    if copy_file and original_path.exists():
        working_copy_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(original_path, working_copy_path)

    original_checksum = (
        calculate_file_checksum(original_path) if original_path.exists() else source.checksum
    )
    working_checksum = (
        calculate_file_checksum(working_copy_path) if working_copy_path.exists() else None
    )

    return OneCWorkingCopyManifest(
        original_source_id=source.source_id,
        original_source_path=source.source_path,
        working_copy_path=str(working_copy_path),
        original_checksum=original_checksum,
        working_copy_checksum=working_checksum,
        disposable=True,
    )
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/one_c_io/types.py

`SHA256=9fa7284f6a2df7a09a602e12af7617cdabfe652109f9221888438919469ba4a6`

```py
"""
OneC I/O shared types.

Purpose:
    Shared enums and payload models for safe 1C adapter discovery.

Boundary:
    These types do not implement real 1C integration.
"""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field


class OneCVersion(StrEnum):
    """Supported or planned 1C/BAS-like version markers."""

    ONE_C_8_2 = "one_c_8_2"
    ONE_C_8_3 = "one_c_8_3"
    UNKNOWN_FUTURE_VERSION = "unknown_future_version"


class OneCChannel(StrEnum):
    """Supported or planned 1C I/O channels."""

    FILE_EXCHANGE = "file_exchange"
    MANUAL_EXPORT_IMPORT = "manual_export_import"
    DIRECT_DB_READONLY = "direct_db_readonly"
    HTTP_ODATA_FUTURE = "http_odata_future"


class OneCAdapterCapability(StrEnum):
    """Declared placeholder adapter capabilities."""

    READ_RAW_SNAPSHOT = "read_raw_snapshot"
    DRY_RUN_EXPORT_PACKAGE = "dry_run_export_package"
    DIRECT_DB_READONLY_DISCOVERY = "direct_db_readonly_discovery"


class DefaultValueCategory(StrEnum):
    """Allowed default value categories for mapping policy."""

    SYSTEM_DEFAULT = "system_default"
    CONFIGURED_DEFAULT = "configured_default"
    SOURCE_DEFAULT = "source_default"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"
    BLOCKED_UNTIL_MAPPED = "blocked_until_mapped"


class FieldCriticality(StrEnum):
    """Accounting field criticality."""

    LOW = "low"
    NORMAL = "normal"
    CRITICAL = "critical"


class OneCRawPayload(BaseModel):
    """Raw 1C-like payload read by placeholder adapters."""

    source_name: str
    version: OneCVersion
    channel: OneCChannel
    records: list[dict[str, Any]] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)


class OneCExportPackage(BaseModel):
    """Dry-run export package model for future 1C writes."""

    package_id: str
    package_type: str
    records: list[dict[str, Any]] = Field(default_factory=list)
    dry_run: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/repositories/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/repositories/mapping_issues.py

`SHA256=f3a634cac304ce3b06aeb7203f593abd0dc0a6b2dfc384ce5b3d5a48f810b06c`

```py
"""
Mapping issue repository.

Purpose:
    Small repository for mapping issue persistence tests and local pipeline.

Boundary:
    Mapping issues are accounting import diagnostics only.
"""

from datetime import UTC, datetime

from sqlmodel import Session, select

from forprint_accounting_registry_service.storage.mapping_models import (
    MappingIssueStatus,
    MappingIssueStorage,
)

BLOCKING_STATUSES = {
    MappingIssueStatus.MANUAL_REVIEW_REQUIRED,
    MappingIssueStatus.BLOCKED_UNTIL_MAPPED,
}


def save_mapping_issue(session: Session, issue: MappingIssueStorage) -> MappingIssueStorage:
    """Persist mapping issue."""
    session.add(issue)
    session.commit()
    session.refresh(issue)
    return issue


def get_mapping_issue(session: Session, issue_id: str) -> MappingIssueStorage | None:
    """Get mapping issue by ID."""
    return session.get(MappingIssueStorage, issue_id)


def update_mapping_issue_status(
    session: Session,
    issue_id: str,
    status: MappingIssueStatus,
) -> MappingIssueStorage:
    """Update issue status."""
    issue = session.get(MappingIssueStorage, issue_id)
    if issue is None:
        raise KeyError(f"Mapping issue not found: {issue_id}")

    issue.status = status
    if status in {MappingIssueStatus.RESOLVED, MappingIssueStatus.IGNORED}:
        issue.resolved_at = datetime.now(UTC)

    session.add(issue)
    session.commit()
    session.refresh(issue)
    return issue


def mapping_completion_is_blocked(session: Session, staging_record_id: str) -> bool:
    """Return True when unresolved blocking issues exist for staging record."""
    statement = select(MappingIssueStorage).where(
        MappingIssueStorage.staging_record_id == staging_record_id
    )
    issues = session.exec(statement).all()
    return any(issue.status in BLOCKING_STATUSES for issue in issues)
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/services/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/services/library_change_requests.py

`SHA256=876498080dd6a19d97e7fadd4d89b3bec4e2694507874cbc7dc46b0e900b8173`

```py
"""
Library Change Request service.

Purpose:
    Підготувати логіку створення заявки до Library.

Important:
    Реальна доставка заявки має йти через майбутній погоджений
    Blueprint-approved flow. На цьому етапі ми тільки формуємо command object.
"""

from forprint_accounting_registry_service.models.library_change_request import (
    LibraryChangeRequest,
    LibraryChangeRequestStatus,
    SubmitLibraryChangeRequestCommand,
)


def prepare_submit_command(request: LibraryChangeRequest) -> SubmitLibraryChangeRequestCommand:
    """Готує команду на подання заявки."""
    request.request_status = LibraryChangeRequestStatus.SUBMITTED
    return SubmitLibraryChangeRequestCommand(request=request)
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/services/mapping_issue_registry.py

`SHA256=b644e98c0b542767d84b6155b2800a5dae51e8d8003ba396473103aa6bf4db58`

```py
"""
Mapping issue registry service.

Purpose:
    Convert mapping policy issues into persisted storage diagnostics.
"""

from sqlmodel import Session

from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingResult,
    MappingIssueType,
)
from forprint_accounting_registry_service.repositories.mapping_issues import save_mapping_issue
from forprint_accounting_registry_service.storage.mapping_models import (
    MappingIssueStatus,
    MappingIssueStorage,
    UnmappedFieldRecordStorage,
)


def status_from_issue_type(issue_type: MappingIssueType) -> MappingIssueStatus:
    """Map policy issue type to storage status."""
    if issue_type == MappingIssueType.MANUAL_REVIEW_REQUIRED:
        return MappingIssueStatus.MANUAL_REVIEW_REQUIRED

    if issue_type == MappingIssueType.BLOCKED_UNTIL_MAPPED:
        return MappingIssueStatus.BLOCKED_UNTIL_MAPPED

    return MappingIssueStatus.NEW


def persist_mapping_result(
    session: Session,
    result: FieldMappingResult,
    staging_record_id: str | None = None,
    raw_snapshot_id: str | None = None,
) -> list[MappingIssueStorage]:
    """Persist mapping issues and unmapped field records."""
    stored_issues: list[MappingIssueStorage] = []

    for issue in result.issues:
        stored_issue = save_mapping_issue(
            session,
            MappingIssueStorage(
                issue_type=issue.issue_type,
                status=status_from_issue_type(issue.issue_type),
                severity=issue.severity,
                raw_snapshot_id=raw_snapshot_id,
                staging_record_id=staging_record_id,
                source_field=issue.source_field,
                target_field=issue.target_field,
                message=issue.message,
            ),
        )
        stored_issues.append(stored_issue)

    for unmapped_field in result.unmapped_fields:
        session.add(
            UnmappedFieldRecordStorage(
                staging_record_id=staging_record_id,
                field_name=unmapped_field.field_name,
                raw_value=unmapped_field.value,
            )
        )

    session.commit()
    return stored_issues
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/services/one_c_snapshot.py

`SHA256=7c39531685b8bd4687672f83e11d3440f573679a2fc3fc1a30fd4cfd1c6c1786`

```py
"""
1C snapshot service.

Purpose:
    Базова логіка для роботи зі snapshot-файлами з 1С.

Important:
    Raw snapshot не редагується.
    Нормалізація виконується пізніше через staging/projection layer.
"""

from pathlib import Path

ALLOWED_SNAPSHOT_EXTENSIONS = {".csv", ".xlsx", ".xml", ".json"}


def validate_snapshot_file(path: Path) -> bool:
    """Перевіряє, чи snapshot-файл існує і має дозволене розширення."""
    return path.exists() and path.is_file() and path.suffix.lower() in ALLOWED_SNAPSHOT_EXTENSIONS


def list_snapshot_files(raw_dir: Path) -> list[Path]:
    """Повертає список snapshot-файлів у raw-директорії."""
    if not raw_dir.exists():
        return []

    return [
        item
        for item in raw_dir.iterdir()
        if item.is_file() and item.suffix.lower() in ALLOWED_SNAPSHOT_EXTENSIONS
    ]
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/storage/__init__.py

`SHA256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

```py

```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/storage/database.py

`SHA256=2dae0ee02317fb1b69744d5fe356fb9315c9741fd5b446cfeed2521816c28c62`

```py
"""
Storage database helpers.

Purpose:
    Lightweight local SQLModel/SQLite foundation for Accounting Registry.

Boundary:
    This is not a production DB strategy.
    This is a small testable storage foundation for accounting-only and 1C-boundary data.
"""

from pathlib import Path
from typing import Any

from sqlmodel import Session, SQLModel, create_engine

from forprint_accounting_registry_service.storage import (
    mapping_models as _mapping_models,  # noqa: F401
)
from forprint_accounting_registry_service.storage import models as _storage_models  # noqa: F401

DEFAULT_SQLITE_PATH = Path("data/accounting_registry.sqlite3")


def build_sqlite_url(db_path: Path) -> str:
    """Build SQLite URL for a filesystem database."""
    return f"sqlite:///{db_path}"


def create_sqlite_engine(db_path: Path | str = ":memory:") -> Any:
    """Create SQLite engine for test/local usage."""
    if str(db_path) == ":memory:":
        return create_engine("sqlite:///:memory:")

    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(build_sqlite_url(path))


def init_storage(engine: Any) -> None:
    """Create all Accounting Registry storage tables."""
    SQLModel.metadata.create_all(engine)


def create_session(engine: Any) -> Session:
    """Create SQLModel session."""
    return Session(engine)
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/storage/mapping_models.py

`SHA256=1dfe68bb802cd0e4fa200c2a16e23b897d738819eae8d5d21b25242e905c20b2`

```py
"""
Mapping issue storage models.

Purpose:
    Persist mapping issues found while importing sanitized 1C-like exports into staging.

Boundary:
    These records are accounting import/mapping diagnostics only.
    They are not CRM, Library, Operational Registry, or product catalog truth.
"""

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, SQLModel


def utc_now() -> datetime:
    """Return UTC datetime."""
    return datetime.now(UTC)


def generate_id() -> str:
    """Generate stable string UUID."""
    return str(uuid4())


class MappingIssueStatus(StrEnum):
    """Mapping issue lifecycle status."""

    NEW = "new"
    MANUAL_REVIEW_REQUIRED = "manual_review_required"
    BLOCKED_UNTIL_MAPPED = "blocked_until_mapped"
    RESOLVED = "resolved"
    IGNORED = "ignored"


class MappingIssueStorage(SQLModel, table=True):
    """Persisted mapping issue."""

    __tablename__ = "mapping_issues"

    id: str = Field(default_factory=generate_id, primary_key=True)
    issue_type: str
    status: MappingIssueStatus = MappingIssueStatus.NEW
    severity: str = "warning"

    raw_snapshot_id: str | None = None
    staging_record_id: str | None = None
    source_field: str | None = None
    target_field: str | None = None
    message: str

    payload: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )
    created_at: datetime = Field(default_factory=utc_now)
    resolved_at: datetime | None = None


class UnmappedFieldRecordStorage(SQLModel, table=True):
    """Persisted unmapped source field."""

    __tablename__ = "unmapped_field_records"

    id: str = Field(default_factory=generate_id, primary_key=True)
    mapping_issue_id: str | None = None
    staging_record_id: str | None = None
    field_name: str
    raw_value: Any | None = Field(default=None, sa_column=Column(JSON, nullable=True))
    created_at: datetime = Field(default_factory=utc_now)


class RequiredFieldMissingIssueStorage(SQLModel, table=True):
    """Persisted required missing field issue."""

    __tablename__ = "required_field_missing_issues"

    id: str = Field(default_factory=generate_id, primary_key=True)
    mapping_issue_id: str | None = None
    staging_record_id: str | None = None
    source_field: str
    target_field: str
    critical: bool = False
    created_at: datetime = Field(default_factory=utc_now)


class FieldTypeMismatchIssueStorage(SQLModel, table=True):
    """Persisted field type mismatch issue."""

    __tablename__ = "field_type_mismatch_issues"

    id: str = Field(default_factory=generate_id, primary_key=True)
    mapping_issue_id: str | None = None
    staging_record_id: str | None = None
    field_name: str
    expected_type: str
    actual_type: str
    raw_value: Any | None = Field(default=None, sa_column=Column(JSON, nullable=True))
    created_at: datetime = Field(default_factory=utc_now)


class DefaultValueDecisionStorage(SQLModel, table=True):
    """Persisted default value decision."""

    __tablename__ = "default_value_decisions"

    id: str = Field(default_factory=generate_id, primary_key=True)
    staging_record_id: str | None = None
    target_field: str
    default_category: str
    default_value: Any | None = Field(default=None, sa_column=Column(JSON, nullable=True))
    approved: bool = False
    created_at: datetime = Field(default_factory=utc_now)
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/storage/models.py

`SHA256=c51187c7be8f12821473bd3e69846f7424725900d3721baa295c62e0ce247579`

```py
"""
Accounting Registry storage models.

Purpose:
    Small v0.2 storage foundation for OneC snapshot / staging / mapping and
    accounting-only document/reference shells.

Boundary:
    These models are accounting-only.

They must not become:
    - CRM;
    - Operational Registry;
    - Library;
    - warehouse service;
    - product catalog truth;
    - client registry;
    - order workflow owner.
"""

from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy.types import JSON
from sqlmodel import Field, SQLModel


def utc_now() -> datetime:
    """Return current UTC datetime."""
    return datetime.now(UTC)


def generate_id() -> str:
    """Generate stable string UUID for storage records."""
    return str(uuid4())


class StorageRecordBase(SQLModel):
    """Shared fields for Accounting Registry storage records."""

    id: str = Field(default_factory=generate_id, primary_key=True)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime | None = None


class OneCRawSnapshot(StorageRecordBase, table=True):
    """
    Raw 1C snapshot metadata.

    This stores metadata about imported raw files or raw export batches.
    It does not normalize 1C data and does not become a full 1C mirror.
    """

    __tablename__ = "one_c_raw_snapshots"

    snapshot_type: str
    source_name: str
    file_name: str | None = None
    file_path: str | None = None
    file_hash: str | None = None
    status: str = "stored"
    raw_metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class OneCStagingRecord(StorageRecordBase, table=True):
    """
    One 1C staging record.

    This is a temporary/staging representation of raw 1C data.
    It is not canonical CRM, Library, warehouse, or operational truth.
    """

    __tablename__ = "one_c_staging_records"

    snapshot_id: str
    record_type: str
    source_row_number: int | None = None
    one_c_id: str | None = None
    one_c_code: str | None = None
    validation_status: str = "pending"
    raw_payload: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )
    normalized_payload: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class OneCMappingRecord(StorageRecordBase, table=True):
    """
    Mapping between Accounting Registry objects and 1C objects.

    Mapping is technical accounting bridge data.
    It does not make 1C the owner of the whole ForPrint system.
    """

    __tablename__ = "one_c_mapping_records"

    entity_type: str
    internal_accounting_id: str
    one_c_id: str
    one_c_code: str | None = None
    one_c_name: str | None = None
    mapping_status: str = "active"
    source_snapshot_id: str | None = None


class OneCImportJob(StorageRecordBase, table=True):
    """Local import job for 1C snapshot/staging flow."""

    __tablename__ = "one_c_import_jobs"

    source_name: str
    snapshot_id: str | None = None
    job_status: str = "created"
    records_total: int = 0
    records_imported: int = 0
    records_failed: int = 0
    started_at: datetime | None = None
    finished_at: datetime | None = None
    job_metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class OneCExportJob(StorageRecordBase, table=True):
    """Local export job shell for future accounting export packages."""

    __tablename__ = "one_c_export_jobs"

    export_profile: str
    job_status: str = "created"
    records_total: int = 0
    records_exported: int = 0
    records_failed: int = 0
    started_at: datetime | None = None
    finished_at: datetime | None = None
    job_metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class AccountingReconciliationJob(StorageRecordBase, table=True):
    """Accounting-only reconciliation job shell."""

    __tablename__ = "accounting_reconciliation_jobs"

    reconciliation_scope: str
    job_status: str = "created"
    period_from: str | None = None
    period_to: str | None = None
    issues_count: int = 0
    job_metadata: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class AccountingDocument(StorageRecordBase, table=True):
    """
    Accounting document shell.

    This is accounting document state only.
    It is not an operational order, CRM workflow, or production lifecycle.
    """

    __tablename__ = "accounting_documents"

    accounting_document_type: str
    document_number: str | None = None
    document_state: str = "draft"
    source_reference_id: str | None = None
    one_c_document_id: str | None = None
    payload: dict[str, Any] = Field(
        default_factory=dict,
        sa_column=Column(JSON, nullable=False),
    )


class OrderAccountingReference(StorageRecordBase, table=True):
    """
    Read-only accounting reference to an external/future operational order.

    This is not canonical order ownership.
    """

    __tablename__ = "order_accounting_references"

    external_order_id: str
    source_module: str | None = None
    reference_kind: str = "external_order_reference"
    description: str | None = None


class InvoiceAccountingReference(StorageRecordBase, table=True):
    """
    Invoice accounting reference shell.

    This is not full invoice lifecycle.
    It does not own CRM command processing or operational workflow.
    """

    __tablename__ = "invoice_accounting_references"

    invoice_reference_id: str
    accounting_document_id: str | None = None
    source_reference_id: str | None = None
    invoice_state: str = "draft"
    amount_total: float = 0.0
    currency: str = "UAH"


class PaymentAccountingReference(StorageRecordBase, table=True):
    """
    Payment accounting reference shell.

    This is not full payment lifecycle.
    It does not implement real payment synchronization.
    """

    __tablename__ = "payment_accounting_references"

    payment_reference_id: str
    invoice_reference_id: str | None = None
    payment_state: str = "created"
    amount_total: float = 0.0
    currency: str = "UAH"
    paid_at: datetime | None = None
```

### MODULE SOURCE â€” app/forprint_accounting_registry_service/storage/repository.py

`SHA256=bd978c66f7f885fb46a390c30ecfec6b28961163912b580257bdf36e36715ba7`

```py
"""
Small storage repository helpers.

Purpose:
    Minimal repository helpers for v0.2 tests and local storage foundation.

Boundary:
    This is not a full domain repository layer yet.
"""

from typing import TypeVar

from sqlmodel import Session, SQLModel

StorageModelT = TypeVar("StorageModelT", bound=SQLModel)


def save_record(session: Session, record: StorageModelT) -> StorageModelT:
    """Save one SQLModel record and return refreshed instance."""
    session.add(record)
    session.commit()
    session.refresh(record)
    return record


def get_record_by_id(
    session: Session,
    model_type: type[StorageModelT],
    record_id: str,
) -> StorageModelT | None:
    """Get one record by primary key."""
    return session.get(model_type, record_id)
```

### MODULE SOURCE â€” contracts/placeholders/accounting.finance_summary.v1.yaml

`SHA256=0d890fb1fb13fc51147717cd67429bc3d09c8befc4f595b68fd283618080b6e2`

```yaml
contract_id: accounting.finance_summary.v1
fixture_status: placeholder
canonical_contract_truth: forprint_library_future

producer: forprint_accounting_registry_service
consumer: forprint_crm_future_or_project_inspector_future

purpose: >
  Placeholder read-model contract for a limited finance summary.
  It may support dashboards or inspection, but it must not become CRM dashboard ownership.

minimal_payload:
  period_from: string
  period_to: string
  currency: string
  invoices_total: number
  payments_total: number
  unpaid_total: number
  reconciliation_issues_count: integer

must_not_include:
  - customer_interaction_history
  - operational_task_state
  - production_status
  - product_catalog_truth
  - calculator_price_logic

notes: >
  This is a reporting projection only. It does not transfer business workflow
  decisions or dashboard state ownership to Accounting Registry.
```

### MODULE SOURCE â€” contracts/placeholders/accounting.invoice_request.v1.yaml

`SHA256=c4128427b60abea719412657fa1b1f2b1a92813a08c961cf8ed0e13304ba2331`

```yaml
contract_id: accounting.invoice_request.v1
fixture_status: placeholder
canonical_contract_truth: forprint_library_future

producer: forprint_integration_gateway_future
consumer: forprint_accounting_registry_service

purpose: >
  Placeholder command contract for requesting accounting invoice creation
  after a CRM business decision and Gateway command validation.

minimal_payload:
  invoice_request_id: string
  source_module: string
  source_reference_id: string
  payer_accounting_ref: string
  currency: string
  lines:
    - line_ref: string
      nomenclature_accounting_ref: string
      quantity: number
      unit: string
      unit_price: number

must_not_include:
  - crm_interaction_history
  - production_workflow_state
  - calculator_internal_formula
  - library_catalog_truth

notes: >
  This is a local placeholder only. Final contract must be approved
  by ForPrint Library and routed through Integration Gateway where needed.
```

### MODULE SOURCE â€” contracts/placeholders/accounting.one_c_import_result.v1.yaml

`SHA256=18a05ddd60dec734c989417d0d613a40ed5389341c7f17729ba5196669fb0eb1`

```yaml
contract_id: accounting.one_c_import_result.v1
fixture_status: placeholder
canonical_contract_truth: forprint_library_future

producer: forprint_accounting_registry_service
consumer: forprint_project_inspector_future_or_integration_gateway_future

purpose: >
  Placeholder event contract for reporting a local 1C import/snapshot result.

minimal_payload:
  import_job_id: string
  snapshot_id: string
  source_file_name: string
  imported_records_count: integer
  staging_records_count: integer
  mapping_issues_count: integer
  validation_issues_count: integer
  status: string
  completed_at: string

allowed_status_examples:
  - completed
  - completed_with_warnings
  - failed

notes: >
  This event reports accounting import state only.
  It does not make Accounting Registry a full 1C mirror.
```

### MODULE SOURCE â€” contracts/placeholders/accounting.payment_status_reference.v1.yaml

`SHA256=2964d3b6687eb84c4444a4871f54614cf290110e8a1d84b2e5f9d15fb8f530bd`

```yaml
contract_id: accounting.payment_status_reference.v1
fixture_status: placeholder
canonical_contract_truth: forprint_library_future

producer: forprint_accounting_registry_service
consumer: forprint_crm_future_or_operational_registry_future

purpose: >
  Placeholder event/reference contract for exposing payment status
  without transferring accounting ownership to CRM or Operational Registry.

minimal_payload:
  payment_reference_id: string
  invoice_reference_id: string
  source_reference_id: string
  payment_status: string
  paid_amount: number
  currency: string
  updated_at: string

allowed_status_examples:
  - unpaid
  - partially_paid
  - paid
  - overpaid
  - cancelled
  - reconciliation_required

notes: >
  This contract exposes financial status only. It must not expose
  accounting internals, 1C raw records, or CRM workflow decisions.
```

### MODULE SOURCE â€” docs/architecture/accounting_registry_boundaries.md

`SHA256=3f3617513eb5e87bf978267a76a13c7181e6644a9282e122b8f75917306b89df`

```md
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
```

### MODULE SOURCE â€” docs/architecture/accounting_storage_boundaries.md

`SHA256=cf8e267d7eca7e69605584bb6152739ef4d6755591feebedbb3fcc3bd5524aff`

```md

# Accounting Storage Boundaries

## Accounting-only storage

The storage layer may contain only accounting/1C-boundary data.

Allowed models include:

- `OneCRawSnapshot`
- `OneCStagingRecord`
- `OneCMappingRecord`
- `OneCImportJob`
- `OneCExportJob`
- `AccountingReconciliationJob`
- `AccountingDocument`
- `InvoiceAccountingReference`
- `PaymentAccountingReference`
- `OrderAccountingReference`

## Operational reference only

Accounting Registry may store order references such as:

- `external_order_id`
- `order_ref`
- `source_order_ref`
- `operational_entity_ref`

These are references only.

They are not order workflow ownership.

## Invoice/payment references

`InvoiceAccountingReference` and `PaymentAccountingReference` are accounting-only shells.

They do not implement:

- full invoice lifecycle;
- full payment lifecycle;
- real payment synchronization;
- CRM invoice command processing;
- Gateway invoice routing.

## Forbidden canonical models

Do not introduce canonical models named:

- `Client`
- `Customer`
- `Order`
- `Product`
- `Material`
- `Invoice`
- `Payment`

Unless the model name explicitly marks it as accounting-only, 1C snapshot, staging, or reference.

Examples of allowed names:

- `InvoiceAccountingReference`
- `PaymentAccountingReference`
- `OrderAccountingReference`
- `OneCNomenclatureSnapshot`
- `AccountingProductReference`
```

### MODULE SOURCE â€” docs/architecture/accounting_storage_foundation.md

`SHA256=02e576eba354080a3f686be04d2e8190f52301ec58199bbd64aac70a09131a91`

```md
# Accounting Storage Foundation

## Purpose

This document describes the v0.2 storage foundation for `forprint_accounting_registry_service`.

The storage foundation is intentionally small.

It supports only Accounting Registry / 1C boundary data.

## Approved scope

The service may store:

- 1C raw snapshots;
- 1C staging records;
- 1C mapping records;
- import jobs;
- export jobs;
- reconciliation jobs;
- accounting document shells;
- invoice accounting references;
- payment accounting references;
- order accounting references.

## Not a production DB strategy

The current storage layer is a lightweight SQLModel/SQLite-compatible foundation.

It is intended for:

- schema creation tests;
- local development;
- repository/service tests;
- boundary validation.

It is not yet a finalized production database strategy.

## Ownership boundary

Accounting Registry stores accounting and 1C-boundary truth.

Operational Registry will store operational truth.

ForPrint Library will store canonical catalogs, contracts, semantic IDs, aliases, and versioning.

ForPrint CRM will own business workflow coordination and dashboard/human-facing workflow.

ForPrint Integration Gateway will route runtime commands later where validation, idempotency, and transport are required.

## Forbidden

This storage foundation must not become:

- CRM;
- Operational Registry;
- Library;
- warehouse service;
- product catalog truth;
- material catalog truth;
- client registry;
- order registry;
- production status registry;
- general business database;
- full 1C mirror for everything.
```

### MODULE SOURCE â€” docs/architecture/accounting_vs_operational_registry.md

`SHA256=a0609ebdef07e257df75fdd3b812b4ead396d39ffd42c883d5fd92177eb3651e`

```md

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
```

### MODULE SOURCE â€” docs/architecture/one_c_adapter_boundary.md

`SHA256=a6a9c56cc0de39a1b9e19556e0a69d8a95e7056c78c0725673c5bbe4937375c6`

```md
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
```

### MODULE SOURCE â€” docs/architecture/one_c_boundary.md

`SHA256=75e8914886ff07f41e9807e64e1904ec442edbe26c324785929735b0eb3a4ae5`

```md
# 1C Boundary

## Purpose

This document defines how `forprint_accounting_registry_service` treats 1C.

1C is an external accounting reality.

1C is not the owner of the whole ForPrint system.

## Allowed 1C responsibilities inside this service

The service may work with:

- 1C raw snapshot files;
- 1C staging records;
- 1C import batches;
- 1C export packages;
- 1C object mappings;
- 1C accounting reconciliation;
- accounting references imported from 1C.

## Raw snapshot rule

Raw 1C snapshot data must be preserved as-is.

Raw data should not be manually rewritten to fit internal assumptions.

Normalization must happen in a separate staging or projection layer.

## Mapping rule

The service may store mappings such as:

```text
internal_accounting_id <-> one_c_id
internal_accounting_code <-> one_c_code

These mappings do not make 1C the canonical owner of the ForPrint system.

They only support accounting synchronization and reconciliation.

Projection rule

The service may keep accounting projections of external objects.

Examples:

AccountingCounterpartyReference
OneCCounterpartySnapshot
AccountingCounterpartyProjection
OneCNomenclatureSnapshot
AccountingProductReference
AccountingNomenclatureProjection

These objects must remain accounting-only.

Deferred

Do not implement yet:

real 1C API integration;
full 1C production import;
full 1C mirror;
database-heavy migration layer;
production payment synchronization;
warehouse integration.

---
```

### MODULE SOURCE â€” docs/architecture/one_c_directory_exchange.md

`SHA256=9722ee7b31bf764ae91fbaca96a3cb710cd70ce954a5c4fd8c5cfc2787137127`

```md
# OneC Directory Exchange

## Purpose

This document defines v0.4 accounting directory exchange.

Directories here are accounting/reference directories from 1C-like context.

They are not canonical ForPrint Library catalogs.

## Allowed directory concepts

- counterparty accounting references;
- nomenclature accounting references;
- invoice/accounting document references;
- payment/accounting status references;
- unit/code/tax/accounting codes as references.

## Forbidden interpretation

Directory exchange must not become:

- canonical CRM client registry;
- canonical product catalog;
- canonical material catalog;
- Library replacement;
- Operational Registry order truth.

## Flow

```text
OneC directory fixture/export
  ↓
OneCDirectorySnapshot
  ↓
OneCDirectoryImportBatch
  ↓
OneCStagingRecord
  ↓
mapping/default policy
Export rule

Directory exports are dry-run by default.

Production writes are forbidden in v0.4.


## `docs/architecture/one_c_report_extraction.md`

```markdown
# OneC Report Extraction

## Purpose

This document defines v0.4 report extraction interface.

The goal is to extract accounting report-like outputs from test/sandbox data without depending on fragile UI screens.

## Initial report categories

- counterparty balance snapshot;
- invoice register snapshot;
- payment register snapshot;
- sales turnover snapshot;
- mutual settlement snapshot;
- nomenclature turnover snapshot.

## Boundary

These are Accounting Registry report snapshots.

They are not:

- CRM analytics dashboards;
- Operational Registry reports;
- full 1C report engine replacement.

## Flow

```text
report definition
  ↓
report request
  ↓
report snapshot
  ↓
report rows
  ↓
staging records / mapping issues
Raw value rule

Report rows preserve raw source values.

Normalization must not overwrite source truth silently.
```

### MODULE SOURCE â€” docs/architecture/one_c_io_strategy.md

`SHA256=23fcca43368d4b3c013205f3737d85884ebcf518bd57655f98da49942f402846`

```md
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
```

### MODULE SOURCE â€” docs/architecture/one_c_mapping_policy.md

`SHA256=e915ba58c8cf8770c30289210450d721f55a4ebac129c34e0b5a3a6ec63c4e36`

```md
# OneC Mapping Policy

## Purpose

This document defines safe mapping/default rules for 1C source data.

## Rules

When a ForPrint field does not match a 1C field:

1. never silently guess critical accounting values;
2. preserve raw source value in `OneCRawSnapshot`;
3. store normalized attempt in `OneCStagingRecord`;
4. record mapping issue if a required field is missing;
5. apply explicit default only if policy allows it;
6. mark default source clearly;
7. never overwrite source truth silently.

## Default categories

Allowed categories:

- `system_default`
- `configured_default`
- `source_default`
- `manual_review_required`
- `blocked_until_mapped`

Critical accounting fields should default to:

```text
manual_review_required

not automatic values.

Unknown fields

Unknown fields must be captured as unmapped fields.

They must not be discarded silently.
```

### MODULE SOURCE â€” docs/architecture/one_c_read_write_policy.md

`SHA256=5b11d7ec6d16d4a521b5ee3d7ad9feacac3ada6eca3c7a5b86bf140cceb95222`

```md
# OneC Read/Write Policy

## Read policy

Allowed in v0.3:

- local file exchange discovery;
- manual export/import discovery;
- direct DB read-only exploration on test copy only;
- sanitized sample data analysis;
- mapping experiments.

## Direct DB access rule

Direct database reading is allowed only for:

- test copy;
- local sandbox copy;
- read-only mode;
- sanitized sample data;
- reverse-engineering field mapping.

Direct DB access is forbidden for:

- live production write;
- uncontrolled live production read;
- changing 1C schema;
- writing into 1C tables directly;
- treating internal 1C tables as canonical ForPrint interface.

## Write policy

Real writes to live 1C are forbidden in v0.3.

Allowed:

- write policy documentation;
- export package model;
- dry-run export payload;
- export package structure validation.

Forbidden:

- real 1C write;
- direct DB write;
- production sync;
- automatic update of live 1C directories;
- automatic invoice posting;
- payment posting;
- document posting.
```

### MODULE SOURCE â€” docs/architecture/one_c_report_extraction.md

`SHA256=9695586e7f7072f42bd229fd3915ce76cb4867ea11e92fe2d5c91f30e36f5768`

```md
# OneC Report Extraction

## Purpose

This document defines v0.4 report extraction interface.

The goal is to extract accounting report-like outputs from test/sandbox data without depending on fragile UI screens.

## Initial report categories

- counterparty balance snapshot;
- invoice register snapshot;
- payment register snapshot;
- sales turnover snapshot;
- mutual settlement snapshot;
- nomenclature turnover snapshot.

## Boundary

These are Accounting Registry report snapshots.

They are not:

- CRM analytics dashboards;
- Operational Registry reports;
- full 1C report engine replacement.

## Raw value rule

Report rows preserve raw source values.

Normalization must not overwrite source truth silently.
```

### MODULE SOURCE â€” docs/architecture/one_c_sandbox_direct_io.md

`SHA256=7cb9ab54866de031b33b53e528129d6120b057fd66fcfd7df4dc27215ee77b4e`

```md
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
```

### MODULE SOURCE â€” docs/architecture/one_c_snapshot_staging_flow.md

`SHA256=90de55ae9982f8fe236a47d59c4b9823fe7c088bde7d7ee7fe0be35e6b03cbdb`

```md
# OneC Snapshot Staging Flow

## Purpose

This document describes the approved v0.2 1C snapshot/staging flow.

## Flow

```text
1C export file / snapshot source
  ↓
OneCRawSnapshot
  ↓
OneCImportJob
  ↓
OneCStagingRecord
  ↓
validation / normalization candidate
  ↓
OneCMappingRecord
Raw snapshot rule

Raw snapshot metadata is stored in OneCRawSnapshot.

Raw data must not be treated as clean canonical ForPrint data.

Staging rule

OneCStagingRecord is a temporary/staging representation.

It may contain:

raw 1C payload;
normalized candidate payload;
validation status;
1C identifiers.

It must not become:

CRM client profile;
Library catalog truth;
Operational Registry entity;
warehouse stock truth.
Mapping rule

OneCMappingRecord connects accounting/internal references with 1C identifiers.

Mapping exists for accounting synchronization and reconciliation only.

Deferred

Do not implement yet:

real 1C API integration;
full 1C import;
production 1C synchronization;
payment import;
warehouse integration;
full 1C mirror.

---
```

### MODULE SOURCE â€” docs/architecture/one_c_test_copy_policy.md

`SHA256=4145e15e63c635fe6a5bdddbdd70aa8dbaaa82c6fecee2d3ca73f3fa61acc882`

```md
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
```

### MODULE SOURCE â€” docs/architecture/one_c_version_strategy.md

`SHA256=976bc3603dc16d761a625ac168895ffcfe46d67b0d7f24d2ba802bf0eb56c71a`

```md
# OneC Version Strategy

## Purpose

The system must not depend on one specific 1C version or department-specific export shape.

## Supported placeholders

Current v0.3 version markers:

- `one_c_8_2`
- `one_c_8_3`
- `unknown_future_version`

## Strategy

Different departments may use:

- different 1C versions;
- different export formats;
- different custom configurations;
- BAS-like future variants.

Therefore Accounting Registry uses an adapter registry:

version + channel → adapter
Boundary

Version-specific adapters must normalize only into Accounting Registry staging.

They must not create canonical CRM, Operational Registry, Library, or warehouse truth.
```

### MODULE SOURCE â€” examples/one_c/directories/counterparty_directory.yaml

`SHA256=853ca1b75f8e25898ea7324e644888d126e73fab6250289983b4c2ff22f7379d`

```yaml
fixture_status: example
real_1c_data: false
sanitized: true
production_allowed: false
directory_kind: counterparty_accounting_references
items:
  - item_id: one-c-counterparty-001
    raw_payload:
      Код: "000001"
      Назва: "ТОВ Приклад"
    normalized_payload:
      one_c_code: "000001"
      display_name: "ТОВ Приклад"
```

### MODULE SOURCE â€” examples/one_c/export_packages/invoice_dry_run_export.yaml

`SHA256=9fbeaff43ea3cb385c706f147d91cf2c788a6e145921c58e9a59d0a93f5141b3`

```yaml
fixture_status: example
real_1c_data: false
sanitized: true
production_allowed: false
package_type: invoice_export
dry_run_only: true
manual_approval_required: true
records:
  - invoice_reference_id: invoice-ref-001
    amount_total: 1000.0
    currency: UAH
```

### MODULE SOURCE â€” examples/one_c/raw_exports/counterparties_example.json

`SHA256=61ba0978aaf39493c40434071c3f1158bfa5b29c6648cb13788e2499afc1c268`

```json
{
  "fixture_status": "example",
  "real_1c_data": false,
  "sanitized": true,
  "production_allowed": false,
  "source_name": "sanitized_counterparties_export",
  "records": [
    {
      "Код": "000001",
      "Назва": "ТОВ Приклад",
      "Телефон": "+380000000000",
      "НевідомеПоле": "preserve-me"
    }
  ]
}
```

### MODULE SOURCE â€” examples/one_c/reports/payment_register_snapshot.yaml

`SHA256=0b370009f490994a94d8aa0c4b29103f4c1bb1eb96bafd02782522289a01d3c0`

```yaml
fixture_status: example
real_1c_data: false
sanitized: true
production_allowed: false
report_code: payment_register_snapshot
rows:
  - document_number: PAY-001
    amount: 1000.0
    currency: UAH
```

### MODULE SOURCE â€” examples/one_c/write_experiments/write_experiment_example.yaml

`SHA256=56a65a873b2695069892599f9f6581017e3f9c82f374ade2f6fb4251f44b9646`

```yaml
fixture_status: example
real_1c_data: false
sanitized: true
production_allowed: false
dry_run: true
destructive_test_write_allowed: false
```

### MODULE SOURCE â€” forprint_module_manifest.yaml

`SHA256=b67d5923a9fb372e2ee9c88b19659d9f10cb63fbea90892d5abb7466dd5ade39`

```yaml

module_id: forprint_accounting_registry_service
module_name: ForPrint Accounting Registry Service
role: accounting_registry_and_one_c_boundary
status: boundary_correction_development

description: >
  Accounting Registry / 1C boundary / accounting truth service for ForPrint.
  The service owns accounting document state, payments, invoices, 1C snapshots,
  1C staging records, mappings, reconciliation reports, and accounting reference
  projections. It must not become CRM, Operational Registry, Library,
  Integration Gateway, Calculator, Warehouse, or a general business database.

architecture_boundary:
  blueprint_role: accounting_registry_and_one_c_boundary
  runtime_gateway_future: forprint_integration_gateway
  canonical_contract_truth_future: forprint_library
  operational_truth_future: forprint_operational_registry
  business_workflow_owner_future: forprint_crm

owns:
  - invoice
  - payment
  - payment_status
  - accounting_document
  - accounting_document_state
  - financial_document_state
  - one_c_raw_snapshot
  - one_c_staging_record
  - one_c_import_batch
  - one_c_export_package
  - one_c_mapping_record
  - accounting_reconciliation_report
  - accounting_reference_projection
  - snapshot_file_metadata
  - import_job
  - export_job
  - reconciliation_job
  - mapping_issue
  - accounting_validation_issue

may_reference_as_projection_only:
  - accounting_counterparty_reference
  - one_c_counterparty_snapshot
  - accounting_counterparty_projection
  - one_c_nomenclature_snapshot
  - accounting_product_reference
  - accounting_nomenclature_projection
  - order_accounting_reference
  - invoice_source_reference
  - external_order_reference

must_not_own:
  - client_registry
  - customer_profile
  - customer_interaction_history
  - crm_contact_history
  - sales_pipeline
  - order_registry
  - production_order
  - operational_task_registry
  - production_status
  - order_status_as_operational_truth
  - warehouse_stock
  - warehouse_reservation
  - warehouse_writeoff
  - material_catalog
  - product_catalog
  - product_template_as_library_truth
  - price_calculation
  - calculator_price_logic
  - prepress_file_lifecycle
  - delivery_status_as_logistics_truth
  - crm_dashboard_state
  - customer_interaction_history
  - business_workflow_decisions
  - integration_routing
  - architecture_governance
  - full_one_c_mirror
  - general_business_database

deferred:
  - full_one_c_production_import
  - real_one_c_api_integration
  - database_heavy_migration_layer
  - operational_registry_inside_this_service
  - crm_dashboard_logic
  - invoice_creation_through_real_gateway_runtime
  - real_crm_integration
  - real_library_integration
  - real_calculator_integration
  - warehouse_integration
  - global_product_catalog
  - global_client_registry
  - production_payment_synchronization
  - large_refactoring

local_contract_policy:
  fixture_status: placeholder
  canonical_contract_truth: forprint_library_future
  notes: >
    Local contracts are placeholders for development and tests only.
    They are not canonical system contracts.
```

### MODULE SOURCE â€” pyproject.toml

`SHA256=b7a4c7803b144809bb59f5ba3966bb0b45b6e7359cbe7e8e19ccdd7254387fb1`

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "forprint-accounting-registry-service"
version = "0.1.0"
description = "ForPrint Accounting Registry Service"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn>=0.30.0",
    "pydantic>=2.8.0",
    "pydantic-settings>=2.4.0",
    "PyYAML>=6.0.2",
    "sqlmodel>=0.0.22"
]

[project.optional-dependencies]
dev = [
    "pytest>=8.2.0",
    "httpx>=0.27.0",
    "ruff>=0.6.0",
    "mypy>=1.11.0",
    "rich>=13.7.0"
]

[tool.setuptools]
package-dir = {"" = "app"}

[tool.setuptools.packages.find]
where = ["app"]
include = ["forprint_accounting_registry_service*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["app"]
addopts = "-q"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
ignore = []

[tool.mypy]
python_version = "3.11"
mypy_path = "app"
strict = true
```

### MODULE SOURCE â€” reports/accounting_registry_check_report.json

`SHA256=b9ac676527f93db268c0e4360d5fa771411cbdb072d567ac92cb7ae941041fc4`

```json
{
  "project": "ForPrint Accounting Registry Service",
  "report_type": "boundary_check_report",
  "status": "OK",
  "checks": [
    {
      "name": "Ruff lint",
      "expected": "Немає lint-помилок у app/tests/scripts",
      "status": "OK",
      "duration_seconds": 0.03055093900184147,
      "details": ""
    },
    {
      "name": "Pytest",
      "expected": "Усі тести проходять",
      "status": "OK",
      "duration_seconds": 1.7454681519993756,
      "details": ""
    },
    {
      "name": "Boundary, storage and OneC files",
      "expected": "Boundary docs, storage docs, OneC docs, manifest and placeholders exist",
      "status": "OK",
      "duration_seconds": 0.0006935580022400245,
      "details": ""
    },
    {
      "name": "v0.5 implementation files",
      "expected": "Sanitized source intake, export parser and pipeline files exist",
      "status": "OK",
      "duration_seconds": 0.00035968700103694573,
      "details": ""
    },
    {
      "name": "Module manifest validation",
      "expected": "Manifest declares accounting role, owns, and must_not_own",
      "status": "OK",
      "duration_seconds": 0.012048713000694988,
      "details": ""
    },
    {
      "name": "Placeholder contract validation",
      "expected": "Local contracts are placeholders and non-canonical",
      "status": "OK",
      "duration_seconds": 0.015392054003314115,
      "details": ""
    },
    {
      "name": "Storage model boundary validation",
      "expected": "No canonical Client/Order/Product/Material/Warehouse/Production models",
      "status": "OK",
      "duration_seconds": 0.0001730779986246489,
      "details": ""
    },
    {
      "name": "OneC I/O boundary validation",
      "expected": "No canonical Client/Order/Product/Material/Warehouse/Production models",
      "status": "OK",
      "duration_seconds": 0.0024272189984912984,
      "details": ""
    },
    {
      "name": "Fixture safety validation",
      "expected": "Committed examples are sanitized, examples and non-production",
      "status": "OK",
      "duration_seconds": 0.007495976002246607,
      "details": ""
    },
    {
      "name": "v0.5 test fixture validation",
      "expected": "Sanitized parser/import fixtures exist",
      "status": "OK",
      "duration_seconds": 0.00014491199908661656,
      "details": ""
    },
    {
      "name": "Gitignore sandbox validation",
      "expected": "local_sandbox and DB-like files are ignored",
      "status": "OK",
      "duration_seconds": 0.0001415109982190188,
      "details": ""
    }
  ]
}
```

### MODULE SOURCE â€” reports/accounting_registry_check_report.md

`SHA256=b530d857564b4df302f96c13e09b960c751e8cee2901d9e93f57f2cb343294d8`

```md
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
```

### MODULE SOURCE â€” reports/accounting_registry_module_status.json

`SHA256=3c5559c8563775dca41d3523c4c6c1abdba76da07bb13da7868314cba2054ebc`

```json
{
  "module_name": "forprint_accounting_registry_service",
  "module_status": "active",
  "current_phase": "governance_alignment_v0_1",
  "boundary": "sandbox_import_export_only_no_live_1c_write"
}
```

### MODULE SOURCE â€” scripts/one_c_discover_source.py

`SHA256=577f2610e79274937bfb371ac5c05bc7bc3b4310ad51b034f32a11e9b3534990`

```py
# python scripts/one_c_discover_source.py

"""
Safe local OneC source discovery smoke runner.

Default:
    read-only, no production, no write.
"""

from pathlib import Path

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.schema_probe import (
    probe_sanitized_source_schema,
)


def run_discovery(path: Path) -> str:
    """Run safe source discovery diagnostic."""
    source = OneCSandboxSource(
        source_id="cli-source",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path=str(path),
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
        sanitized=True,
        production_allowed=False,
    )
    result = probe_sanitized_source_schema(source)
    return result.status


def main() -> int:
    """CLI entrypoint."""
    status = run_discovery(Path("tests/fixtures/one_c/exports/counterparties.json"))
    print(f"OneC discovery status: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### MODULE SOURCE â€” scripts/one_c_parse_export.py

`SHA256=4102b06e8cd060655f8a14213209d96e4bec7fa05986603d17cf9cc511942493`

```py
# python scripts/one_c_parse_export.py

"""
Safe local OneC export parser smoke runner.

Default:
    parses sanitized fixture only.
"""

from pathlib import Path

from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
)


def parse_export(path: Path) -> int:
    """Parse sanitized export and return number of rows."""
    result = parse_one_c_export_file(path)
    if result.batch is None:
        return 0
    return len(result.batch.rows)


def main() -> int:
    """CLI entrypoint."""
    rows_count = parse_export(Path("tests/fixtures/one_c/exports/counterparties.json"))
    print(f"Parsed rows: {rows_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### MODULE SOURCE â€” scripts/one_c_run_import_pipeline.py

`SHA256=3d28d0a08db607772efa098adb315494991a972143ce1ba2bb000f93e8095847`

```py
# python scripts/one_c_run_import_pipeline.py

"""
Safe local OneC import pipeline smoke runner.

Default:
    in-memory storage, sanitized fixture only, no live 1C.
"""

from pathlib import Path

from forprint_accounting_registry_service.one_c_io.import_pipeline import (
    OneCSandboxImportPipeline,
)
from forprint_accounting_registry_service.one_c_io.mapping import FieldMappingDefinition
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from sqlmodel import Session


def run_pipeline() -> str:
    """Run pipeline against sanitized fixture."""
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)

    source = OneCSandboxSource(
        source_id="cli-source",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/exports/counterparties.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
        sanitized=True,
        production_allowed=False,
    )

    with Session(engine) as session:
        pipeline = OneCSandboxImportPipeline(session)
        result = pipeline.run_file_export_import(
            source=source,
            export_path=Path("tests/fixtures/one_c/exports/counterparties.json"),
            mapping_definitions=[
                FieldMappingDefinition(source_field="Код", target_field="one_c_code"),
                FieldMappingDefinition(source_field="Назва", target_field="name"),
            ],
            target_kind="counterparty_accounting_reference",
        )
        return result.status


def main() -> int:
    """CLI entrypoint."""
    print(f"Pipeline status: {run_pipeline()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

### MODULE SOURCE â€” tests/fixtures/one_c/databases/synthetic_test_db.txt

`SHA256=836a9abf4d39161a8634f799b2605ad4f494e8a01a96052ba95496a7e5d0fe8b`

```
fixture_status=example
real_1c_data=false
sanitized=true
production_allowed=false
```

### MODULE SOURCE â€” tests/fixtures/one_c/exports/counterparties.csv

`SHA256=f1ec71ab464e152c43447ea75a43d1264f52375d347bcc064b1780d1b1fddc34`

```csv
Код,Назва,Телефон,НевідомеПоле
000001,ТОВ Приклад,+380000000000,preserve-me
```

### MODULE SOURCE â€” tests/fixtures/one_c/exports/counterparties.json

`SHA256=8ca7a318a1b96a5fe7e6eaa9346b004129d0713400b1c7885966b3e2314d373b`

```json
{
  "fixture_status": "example",
  "real_1c_data": false,
  "sanitized": true,
  "production_allowed": false,
  "records": [
    {
      "Код": "000001",
      "Назва": "ТОВ Приклад",
      "Телефон": "+380000000000",
      "НевідомеПоле": "preserve-me"
    }
  ]
}
```

### MODULE SOURCE â€” tests/fixtures/one_c/exports/counterparties.xml

`SHA256=e5d57b0692172dde92533b1c3c1c7f32bbcc08b27d5abde444ae9b7ec59be74c`

```xml
<records>
  <record>
    <Код>000001</Код>
    <Назва>ТОВ Приклад</Назва>
    <НевідомеПоле>preserve-me</НевідомеПоле>
  </record>
</records>
```

### MODULE SOURCE â€” tests/fixtures/one_c/exports/payment_register.yaml

`SHA256=028f2a9e77aa2f59f68cd0de9da7817494235f7a71553694c89c13f7a80f33ed`

```yaml
fixture_status: example
real_1c_data: false
sanitized: true
production_allowed: false
rows:
  - document_number: PAY-001
    amount: 1000.0
    currency: UAH
```

### MODULE SOURCE â€” tests/unit/test_counterparty_model.py

`SHA256=8da760bc4463049e5302d7b72bee0647c9d46356e46352db0aefdb1f413d3b0f`

```py
from forprint_accounting_registry_service.models.counterparty import (
    AddressType,
    CommunicationChannel,
    CommunicationChannelType,
    Counterparty,
    CounterpartyAddress,
    CounterpartyContact,
    CounterpartyRole,
    CounterpartyType,
    DeliveryProfile,
    PaymentTerms,
)


def test_counterparty_can_have_multiple_accounting_roles() -> None:
    counterparty = Counterparty(
        counterparty_type=CounterpartyType.COMPANY,
        name="ТОВ Тест",
        roles=[CounterpartyRole.CLIENT, CounterpartyRole.SUPPLIER],
        one_c_id="one-c-counterparty-001",
        one_c_code="000001",
        one_c_raw_name="ТОВ Тест з 1С",
    )

    assert CounterpartyRole.CLIENT in counterparty.roles
    assert CounterpartyRole.SUPPLIER in counterparty.roles
    assert counterparty.one_c_id == "one-c-counterparty-001"
    assert counterparty.one_c_code == "000001"
    assert counterparty.one_c_raw_name == "ТОВ Тест з 1С"


def test_counterparty_supports_contacts_and_communication_channels() -> None:
    contact = CounterpartyContact(
        full_name="Іван Іваненко",
        position="Бухгалтер",
        channels=[
            CommunicationChannel(
                channel_type=CommunicationChannelType.PHONE,
                value="+380501112233",
                is_primary=True,
                verified=True,
            ),
            CommunicationChannel(
                channel_type=CommunicationChannelType.TELEGRAM,
                value="@ivan_test",
                is_primary=False,
                verified=False,
            ),
            CommunicationChannel(
                channel_type=CommunicationChannelType.VIBER,
                value="+380501112233",
                is_primary=False,
                verified=False,
            ),
        ],
        is_primary=True,
    )

    counterparty = Counterparty(
        counterparty_type=CounterpartyType.COMPANY,
        name="ТОВ Контакт",
        roles=[CounterpartyRole.CLIENT],
        contacts=[contact],
    )

    assert counterparty.contacts[0].full_name == "Іван Іваненко"
    assert counterparty.contacts[0].channels[0].channel_type == CommunicationChannelType.PHONE
    assert counterparty.contacts[0].channels[1].channel_type == CommunicationChannelType.TELEGRAM
    assert counterparty.contacts[0].channels[2].channel_type == CommunicationChannelType.VIBER


def test_counterparty_supports_addresses_delivery_and_payment_terms() -> None:
    counterparty = Counterparty(
        counterparty_type=CounterpartyType.COMPANY,
        name="ТОВ Доставка",
        roles=[CounterpartyRole.CLIENT],
        addresses=[
            CounterpartyAddress(
                address_type=AddressType.LEGAL,
                value="м. Київ, вул. Тестова, 1",
                city="Київ",
            ),
            CounterpartyAddress(
                address_type=AddressType.NOVA_POSHTA_BRANCH,
                value="Нова пошта, відділення №1",
                city="Київ",
            ),
        ],
        delivery_profile=DeliveryProfile(
            preferred_carrier="nova_poshta",
            nova_poshta_city_ref="kyiv-ref",
            nova_poshta_warehouse_ref="warehouse-ref-1",
            delivery_payer="client",
            recipient_name="Іван Іваненко",
            recipient_phone="+380501112233",
        ),
        payment_terms=PaymentTerms(
            payment_type="prepayment",
            prepayment_percent=100.0,
            currency="UAH",
            vat_mode="with_vat",
        ),
    )

    assert counterparty.addresses[0].address_type == AddressType.LEGAL
    assert counterparty.addresses[1].address_type == AddressType.NOVA_POSHTA_BRANCH
    assert counterparty.delivery_profile is not None
    assert counterparty.delivery_profile.preferred_carrier == "nova_poshta"
    assert counterparty.payment_terms is not None
    assert counterparty.payment_terms.prepayment_percent == 100.0
```

### MODULE SOURCE â€” tests/unit/test_mapping_issue_persistence.py

`SHA256=cc7e2dfc144dc0e6cb277f781bdcb817db325729dd6f97db209ad3b0c29b28ed`

```py
from forprint_accounting_registry_service.repositories.mapping_issues import (
    get_mapping_issue,
    mapping_completion_is_blocked,
    save_mapping_issue,
    update_mapping_issue_status,
)
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from forprint_accounting_registry_service.storage.mapping_models import (
    DefaultValueDecisionStorage,
    FieldTypeMismatchIssueStorage,
    MappingIssueStatus,
    MappingIssueStorage,
    RequiredFieldMissingIssueStorage,
    UnmappedFieldRecordStorage,
)
from sqlmodel import Session


def create_test_session() -> Session:
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)
    return Session(engine)


def test_mapping_issue_persists_and_status_can_be_updated() -> None:
    with create_test_session() as session:
        issue = save_mapping_issue(
            session,
            MappingIssueStorage(
                issue_type="required_field_missing",
                status=MappingIssueStatus.MANUAL_REVIEW_REQUIRED,
                staging_record_id="staging-001",
                source_field="Код",
                target_field="one_c_code",
                message="Missing critical code",
            ),
        )

        assert get_mapping_issue(session, issue.id) is not None
        assert mapping_completion_is_blocked(session, "staging-001") is True

        update_mapping_issue_status(session, issue.id, MappingIssueStatus.RESOLVED)

        assert mapping_completion_is_blocked(session, "staging-001") is False


def test_unmapped_required_type_mismatch_and_default_decision_persist() -> None:
    with create_test_session() as session:
        unmapped = UnmappedFieldRecordStorage(
            staging_record_id="staging-001",
            field_name="Unknown",
            raw_value="value",
        )
        required = RequiredFieldMissingIssueStorage(
            staging_record_id="staging-001",
            source_field="Код",
            target_field="one_c_code",
            critical=True,
        )
        mismatch = FieldTypeMismatchIssueStorage(
            staging_record_id="staging-001",
            field_name="Amount",
            expected_type="number",
            actual_type="string",
            raw_value="not-a-number",
        )
        decision = DefaultValueDecisionStorage(
            staging_record_id="staging-001",
            target_field="currency",
            default_category="configured_default",
            default_value="UAH",
            approved=False,
        )

        session.add(unmapped)
        session.add(required)
        session.add(mismatch)
        session.add(decision)
        session.commit()

        assert unmapped.id
        assert required.critical is True
        assert mismatch.actual_type == "string"
        assert decision.default_value == "UAH"
```

### MODULE SOURCE â€” tests/unit/test_mapping_issue_registry_service.py

`SHA256=dd6d1394d8e641f31c80a0bbb166a33d312d1fb7403a2589e3c2732a0e38ba1b`

```py
from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    apply_mapping_policy,
)
from forprint_accounting_registry_service.one_c_io.types import FieldCriticality
from forprint_accounting_registry_service.services.mapping_issue_registry import (
    persist_mapping_result,
)
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from sqlmodel import Session


def test_mapping_issue_registry_persists_policy_result() -> None:
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)

    with Session(engine) as session:
        result = apply_mapping_policy(
            source_payload={"Unknown": "preserve"},
            definitions=[
                FieldMappingDefinition(
                    source_field="Код",
                    target_field="one_c_code",
                    required=True,
                    criticality=FieldCriticality.CRITICAL,
                )
            ],
        )

        stored = persist_mapping_result(session, result, staging_record_id="staging-001")

        assert len(stored) == 2
        assert any(issue.status == "manual_review_required" for issue in stored)
```

### MODULE SOURCE â€” tests/unit/test_one_c_adapter_registry.py

`SHA256=6221261546bbe3e3fade4e6ab2f7dce6f85adba433ed30be16b6938416cc395f`

```py
from forprint_accounting_registry_service.one_c_io.adapters import (
    OneCDirectDbReadonlyAdapter,
    OneCFileExchangeAdapter,
    OneCManualExportImportAdapter,
    build_default_adapter_registry,
)
from forprint_accounting_registry_service.one_c_io.types import (
    OneCChannel,
    OneCVersion,
)


def test_adapter_registry_supports_one_c_8_2_placeholder() -> None:
    registry = build_default_adapter_registry()

    adapter = registry.get_adapter(
        OneCVersion.ONE_C_8_2,
        OneCChannel.MANUAL_EXPORT_IMPORT,
    )

    assert isinstance(adapter, OneCManualExportImportAdapter)
    assert adapter.policy.version == OneCVersion.ONE_C_8_2


def test_adapter_registry_supports_one_c_8_3_placeholder() -> None:
    registry = build_default_adapter_registry()

    adapter = registry.get_adapter(
        OneCVersion.ONE_C_8_3,
        OneCChannel.FILE_EXCHANGE,
    )

    assert isinstance(adapter, OneCFileExchangeAdapter)
    assert adapter.policy.version == OneCVersion.ONE_C_8_3


def test_adapter_registry_supports_unknown_future_direct_db_placeholder() -> None:
    registry = build_default_adapter_registry()

    adapter = registry.get_adapter(
        OneCVersion.UNKNOWN_FUTURE_VERSION,
        OneCChannel.DIRECT_DB_READONLY,
    )

    assert isinstance(adapter, OneCDirectDbReadonlyAdapter)
    assert adapter.policy.requires_test_copy is True
```

### MODULE SOURCE â€” tests/unit/test_one_c_developer_cli.py

`SHA256=3e7535f7a4712a78f6e5f579c95a8104b081409c768fbbda827dadc700ccf228`

```py
from pathlib import Path

from scripts.one_c_discover_source import run_discovery
from scripts.one_c_parse_export import parse_export
from scripts.one_c_run_import_pipeline import run_pipeline


def test_parse_export_script_function_is_safe_by_default() -> None:
    rows_count = parse_export(Path("tests/fixtures/one_c/exports/counterparties.json"))

    assert rows_count == 1


def test_discover_source_script_function_returns_status() -> None:
    status = run_discovery(Path("tests/fixtures/one_c/exports/counterparties.json"))

    assert status in {"completed", "unsupported_source"}


def test_import_pipeline_script_function_returns_status() -> None:
    status = run_pipeline()

    assert status in {
        "completed",
        "completed_with_warnings",
        "blocked_by_mapping_issues",
    }
```

### MODULE SOURCE â€” tests/unit/test_one_c_direct_db_discovery.py

`SHA256=a4847a62deb88f0c77075ab7a660805942716509bdc4613786077f83b27d0cd1`

```py
import pytest
from forprint_accounting_registry_service.one_c_io.direct_db import (
    OneCSandboxDirectDbInspector,
)
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyError,
    OneCSourceSafetyLevel,
)


def build_readonly_source() -> OneCSandboxSource:
    return OneCSandboxSource(
        source_id="sandbox-fixture",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/sanitized.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
    )


def test_direct_db_inspector_refuses_production_source() -> None:
    source = OneCSandboxSource(
        source_id="production",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="/production/one_c.1CD",
        safety_level=OneCSourceSafetyLevel.PRODUCTION_FORBIDDEN,
        production_allowed=True,
    )

    with pytest.raises(OneCSourceSafetyError):
        OneCSandboxDirectDbInspector(source)


def test_schema_discovery_report_can_be_created_from_fixture() -> None:
    inspector = OneCSandboxDirectDbInspector(build_readonly_source())

    report = inspector.discover_schema_from_fixture(
        {
            "Counterparties": [
                {"Code": "000001", "Name": "ТОВ Приклад"},
            ]
        }
    )

    assert report.source_id == "sandbox-fixture"
    assert report.canonical_truth is False
    assert report.tables[0].table_name == "Counterparties"
    assert report.tables[0].records_count == 1


def test_raw_extract_batch_can_be_created_from_fixture() -> None:
    inspector = OneCSandboxDirectDbInspector(build_readonly_source())

    batch = inspector.extract_raw_batch_from_fixture(
        table_name="Counterparties",
        records=[{"Code": "000001", "Unknown": "preserve"}],
    )

    assert batch.table_name == "Counterparties"
    assert batch.records[0]["Unknown"] == "preserve"


def test_readonly_inspector_has_no_write_method() -> None:
    inspector = OneCSandboxDirectDbInspector(build_readonly_source())

    assert not hasattr(inspector, "write")
    assert not hasattr(inspector, "post")
```

### MODULE SOURCE â€” tests/unit/test_one_c_direct_db_policy.py

`SHA256=4bb69d9c4c6a4494fff084d69648a57f83f841bbf3e792d5cd3126aa0c46561c`

```py
import pytest
from forprint_accounting_registry_service.one_c_io.adapters import (
    OneCDirectDbReadonlyAdapter,
    OneCFileExchangeAdapter,
)
from forprint_accounting_registry_service.one_c_io.policies import (
    OneCAdapterPolicy,
    OneCWritePolicyViolation,
    validate_live_write_is_forbidden,
)
from forprint_accounting_registry_service.one_c_io.types import (
    OneCChannel,
    OneCExportPackage,
    OneCVersion,
)


def test_direct_db_adapter_is_read_only_and_not_production_allowed() -> None:
    adapter = OneCDirectDbReadonlyAdapter()

    assert adapter.policy.read_only is True
    assert adapter.policy.production_allowed is False
    assert adapter.policy.writes_allowed is False
    assert adapter.policy.requires_test_copy is True


def test_live_write_is_forbidden_by_default() -> None:
    adapter = OneCFileExchangeAdapter()

    package = OneCExportPackage(
        package_id="dry-run-001",
        package_type="invoice_export",
        records=[{"invoice": "INV-001"}],
        dry_run=True,
    )

    validated = adapter.validate_export_package(package)

    assert validated.package_id == "dry-run-001"


def test_non_dry_run_export_is_blocked() -> None:
    adapter = OneCFileExchangeAdapter()

    package = OneCExportPackage(
        package_id="live-write-001",
        package_type="invoice_export",
        records=[{"invoice": "INV-001"}],
        dry_run=False,
    )

    with pytest.raises(ValueError, match="Only dry-run export packages"):
        adapter.validate_export_package(package)


def test_policy_rejects_adapter_that_allows_live_writes() -> None:
    unsafe_policy = OneCAdapterPolicy(
        adapter_name="UnsafeAdapter",
        version=OneCVersion.ONE_C_8_3,
        channel=OneCChannel.FILE_EXCHANGE,
        writes_allowed=True,
        dry_run_only=False,
    )

    with pytest.raises(OneCWritePolicyViolation):
        validate_live_write_is_forbidden(unsafe_policy)
```

### MODULE SOURCE â€” tests/unit/test_one_c_directories.py

`SHA256=92852b2cd78ab78e51c4787dbde514e3154ce419f9eb37b7bdcc372ea84667b3`

```py
from forprint_accounting_registry_service.one_c_io.directories import (
    OneCDirectoryExportPackage,
    OneCDirectoryItemSnapshot,
    OneCDirectoryKind,
    OneCDirectorySnapshot,
    build_directory_import_batch,
    directory_snapshot_to_staging_records,
)


def build_directory_snapshot() -> OneCDirectorySnapshot:
    return OneCDirectorySnapshot(
        snapshot_id="dir-snapshot-001",
        directory_kind=OneCDirectoryKind.COUNTERPARTY_ACCOUNTING_REFERENCES,
        source_name="sanitized_fixture",
        items=[
            OneCDirectoryItemSnapshot(
                item_id="one-c-counterparty-001",
                raw_payload={"Код": "000001", "Назва": "ТОВ Приклад"},
                normalized_payload={"one_c_code": "000001", "name": "ТОВ Приклад"},
            )
        ],
    )


def test_directory_snapshot_is_accounting_reference_only() -> None:
    snapshot = build_directory_snapshot()

    assert snapshot.production_allowed is False
    assert snapshot.sanitized is True
    assert snapshot.items[0].accounting_reference_only is True


def test_directory_import_batch_creates_staging_records() -> None:
    snapshot = build_directory_snapshot()

    batch = build_directory_import_batch(snapshot)
    records = directory_snapshot_to_staging_records(snapshot)

    assert batch.items_count == 1
    assert records[0].record_type.startswith("directory:")
    assert records[0].raw_payload["accounting_reference_only"] is True


def test_directory_export_package_is_dry_run_by_default() -> None:
    package = OneCDirectoryExportPackage(
        package_id="dir-export-001",
        directory_kind=OneCDirectoryKind.COUNTERPARTY_ACCOUNTING_REFERENCES,
    )

    assert package.dry_run is True
    assert package.production_write_allowed is False
    assert package.manual_approval_required is True
```

### MODULE SOURCE â€” tests/unit/test_one_c_directory_practical_import.py

`SHA256=0eed2df94407458d5083645690af26740552e0bf0b537971cdff4e2c0910be36`

```py
from pathlib import Path

from forprint_accounting_registry_service.one_c_io.directories import (
    OneCDirectoryExportPackage,
    OneCDirectoryItemSnapshot,
    OneCDirectoryKind,
    OneCDirectorySnapshot,
    build_directory_import_batch,
    directory_snapshot_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
)

FIXTURES = Path("tests/fixtures/one_c/exports")


def test_counterparty_directory_csv_fixture_imports_as_accounting_reference() -> None:
    result = parse_one_c_export_file(
        FIXTURES / "counterparties.csv",
        target_kind="counterparty_accounting_reference",
    )
    assert result.batch is not None

    snapshot = OneCDirectorySnapshot(
        snapshot_id="dir-csv-001",
        directory_kind=OneCDirectoryKind.COUNTERPARTY_ACCOUNTING_REFERENCES,
        source_name=result.batch.source_path,
        items=[
            OneCDirectoryItemSnapshot(
                item_id=row.raw_values["Код"],
                raw_payload=row.raw_values,
                normalized_payload={"one_c_code": row.raw_values["Код"]},
            )
            for row in result.batch.rows
        ],
    )

    batch = build_directory_import_batch(snapshot)
    staging = directory_snapshot_to_staging_records(snapshot)

    assert batch.items_count == 1
    assert staging[0].raw_payload["accounting_reference_only"] is True


def test_directory_export_remains_dry_run_and_manual_approval_required() -> None:
    package = OneCDirectoryExportPackage(
        package_id="directory-export",
        directory_kind=OneCDirectoryKind.NOMENCLATURE_ACCOUNTING_REFERENCES,
    )

    assert package.dry_run is True
    assert package.production_write_allowed is False
    assert package.manual_approval_required is True
```

### MODULE SOURCE â€” tests/unit/test_one_c_export_packages.py

`SHA256=f1502aad7921712ea9880859f26f1b8e62a5edf1b5ac3f956615f7f245000130`

```py
from forprint_accounting_registry_service.one_c_io.export_packages import (
    OneCDryRunExportPackage,
    OneCExportPackageType,
    validate_dry_run_export_package,
)
from forprint_accounting_registry_service.one_c_io.types import OneCVersion


def test_invoice_dry_run_export_package_validates() -> None:
    package = OneCDryRunExportPackage(
        package_id="pkg-001",
        package_type=OneCExportPackageType.INVOICE_EXPORT,
        target_adapter="OneCFileExchangeAdapter",
        target_version=OneCVersion.ONE_C_8_3,
        records=[{"invoice_reference_id": "invoice-ref-001"}],
    )

    result = validate_dry_run_export_package(package)

    assert result.valid is True


def test_directory_dry_run_export_package_validates() -> None:
    package = OneCDryRunExportPackage(
        package_id="pkg-002",
        package_type=OneCExportPackageType.DIRECTORY_EXPORT,
        target_adapter="OneCManualExportImportAdapter",
        target_version=OneCVersion.ONE_C_8_2,
        records=[{"item_id": "item-001"}],
    )

    result = validate_dry_run_export_package(package)

    assert result.valid is True


def test_package_cannot_be_marked_production_write() -> None:
    package = OneCDryRunExportPackage(
        package_id="pkg-003",
        package_type=OneCExportPackageType.PAYMENT_EXPORT,
        target_adapter="OneCFileExchangeAdapter",
        target_version=OneCVersion.ONE_C_8_3,
        production_write_allowed=True,
    )

    result = validate_dry_run_export_package(package)

    assert result.valid is False
    assert "production_write_allowed must be false" in result.errors


def test_package_requires_manual_approval() -> None:
    package = OneCDryRunExportPackage(
        package_id="pkg-004",
        package_type=OneCExportPackageType.ACCOUNTING_DOCUMENT_EXPORT,
        target_adapter="OneCFileExchangeAdapter",
        target_version=OneCVersion.ONE_C_8_3,
        manual_approval_required=False,
    )

    result = validate_dry_run_export_package(package)

    assert result.valid is False
    assert "manual_approval_required must be true" in result.errors
```

### MODULE SOURCE â€” tests/unit/test_one_c_export_parsers.py

`SHA256=3ca80fa1c508e74864d9be75949555b33de116f533ecca89980feb9ef90b920e`

```py
from pathlib import Path

from forprint_accounting_registry_service.one_c_io.export_detection import detect_export_format
from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
    parsed_export_batch_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.file_formats import OneCExportFormat

FIXTURES = Path("tests/fixtures/one_c/exports")


def test_json_export_fixture_parses() -> None:
    result = parse_one_c_export_file(FIXTURES / "counterparties.json")

    assert result.batch is not None
    assert result.batch.sanitized is True
    assert result.batch.production_allowed is False
    assert result.batch.rows[0].raw_values["Код"] == "000001"


def test_csv_export_fixture_parses() -> None:
    result = parse_one_c_export_file(FIXTURES / "counterparties.csv")

    assert result.batch is not None
    assert result.batch.export_format == OneCExportFormat.CSV
    assert result.batch.rows[0].raw_values["НевідомеПоле"] == "preserve-me"


def test_xml_export_fixture_parses_or_returns_supported_batch() -> None:
    result = parse_one_c_export_file(FIXTURES / "counterparties.xml")

    assert result.batch is not None
    assert result.batch.rows[0].raw_values["Код"] == "000001"


def test_unknown_format_returns_explicit_unsupported_result(tmp_path: Path) -> None:
    path = tmp_path / "export.bin"
    path.write_text("unknown", encoding="utf-8")

    assert detect_export_format(path) == OneCExportFormat.UNKNOWN_RAW_TEXT

    result = parse_one_c_export_file(path)

    assert result.supported is False
    assert result.batch is None


def test_parsed_export_maps_to_staging_records() -> None:
    result = parse_one_c_export_file(FIXTURES / "counterparties.json")
    assert result.batch is not None

    records = parsed_export_batch_to_staging_records(result.batch, snapshot_id="snapshot-001")

    assert records[0].record_type.startswith("parsed_export:")
    assert records[0].raw_payload["row"]["НевідомеПоле"] == "preserve-me"
```

### MODULE SOURCE â€” tests/unit/test_one_c_fixtures.py

`SHA256=aa22aa17e12287ebd73a1630b28e18cb6c2b2bbcbd96583dc9f883d23aca8076`

```py
from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_example_fixtures_are_sanitized_and_non_production() -> None:
    fixture_paths = [
        PROJECT_ROOT / "examples/one_c/directories/counterparty_directory.yaml",
        PROJECT_ROOT / "examples/one_c/reports/payment_register_snapshot.yaml",
        PROJECT_ROOT / "examples/one_c/export_packages/invoice_dry_run_export.yaml",
        PROJECT_ROOT / "examples/one_c/write_experiments/write_experiment_example.yaml",
    ]

    for path in fixture_paths:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert payload["fixture_status"] == "example"
        assert payload["real_1c_data"] is False
        assert payload["sanitized"] is True
        assert payload["production_allowed"] is False


def test_local_sandbox_paths_are_gitignored() -> None:
    gitignore = (PROJECT_ROOT / ".gitignore").read_text(encoding="utf-8")

    required_patterns = [
        "local_sandbox/",
        "*.1CD",
        "*.dt",
        "*.cf",
        "*.bak",
        "*.dump",
        "*.sqlite",
        "*.db",
    ]

    for pattern in required_patterns:
        assert pattern in gitignore
```

### MODULE SOURCE â€” tests/unit/test_one_c_import_pipeline.py

`SHA256=33ff0caeaa2d339659cd01dd133dad8037b3bd1c8bb0bfd6d8205fffefe6df63`

```py
from pathlib import Path

from forprint_accounting_registry_service.one_c_io.import_pipeline import (
    OneCImportPipelineStatus,
    OneCSandboxImportPipeline,
)
from forprint_accounting_registry_service.one_c_io.mapping import FieldMappingDefinition
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.types import FieldCriticality
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from sqlmodel import Session

FIXTURES = Path("tests/fixtures/one_c/exports")


def create_source(sanitized: bool = True, production_allowed: bool = False) -> OneCSandboxSource:
    return OneCSandboxSource(
        source_id="pipeline-source",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path=str(FIXTURES / "counterparties.json"),
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
        sanitized=sanitized,
        production_allowed=production_allowed,
    )


def run_pipeline(export_path: Path, source: OneCSandboxSource):
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)

    with Session(engine) as session:
        pipeline = OneCSandboxImportPipeline(session)
        return pipeline.run_file_export_import(
            source=source,
            export_path=export_path,
            mapping_definitions=[
                FieldMappingDefinition(source_field="Код", target_field="one_c_code"),
                FieldMappingDefinition(
                    source_field="ЄДРПОУ",
                    target_field="tax_id",
                    required=True,
                    criticality=FieldCriticality.CRITICAL,
                ),
            ],
            target_kind="counterparty_accounting_reference",
        )


def test_pipeline_runs_on_sanitized_json_fixture() -> None:
    result = run_pipeline(FIXTURES / "counterparties.json", create_source())

    assert result.raw_snapshot_count == 1
    assert result.staging_record_count == 1
    assert result.mapping_issue_count >= 1
    assert result.manual_review_required_count >= 1
    assert result.status == OneCImportPipelineStatus.BLOCKED_BY_MAPPING_ISSUES


def test_pipeline_runs_on_sanitized_csv_fixture() -> None:
    result = run_pipeline(FIXTURES / "counterparties.csv", create_source())

    assert result.raw_snapshot_count == 1
    assert result.staging_record_count == 1


def test_pipeline_returns_unsupported_source_for_unknown_format(tmp_path: Path) -> None:
    path = tmp_path / "export.bin"
    path.write_text("unknown", encoding="utf-8")

    result = run_pipeline(path, create_source())

    assert result.status == OneCImportPipelineStatus.UNSUPPORTED_SOURCE


def test_pipeline_refuses_unsanitized_source() -> None:
    result = run_pipeline(FIXTURES / "counterparties.json", create_source(sanitized=False))

    assert result.status == OneCImportPipelineStatus.FAILED


def test_pipeline_refuses_production_source() -> None:
    result = run_pipeline(
        FIXTURES / "counterparties.json",
        create_source(production_allowed=True),
    )

    assert result.status == OneCImportPipelineStatus.FAILED
```

### MODULE SOURCE â€” tests/unit/test_one_c_io_boundaries.py

`SHA256=e89d077e9dd7132b451b25618f9160f3a5e1e92868717c8fcf24752952d38654`

```py
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ONE_C_IO_ROOT = (
    PROJECT_ROOT
    / "app"
    / "forprint_accounting_registry_service"
    / "one_c_io"
)


def test_required_one_c_io_docs_exist() -> None:
    required_docs = [
        "docs/architecture/one_c_io_strategy.md",
        "docs/architecture/one_c_adapter_boundary.md",
        "docs/architecture/one_c_mapping_policy.md",
        "docs/architecture/one_c_read_write_policy.md",
        "docs/architecture/one_c_version_strategy.md",
        "docs/architecture/one_c_test_copy_policy.md",
    ]

    for relative_path in required_docs:
        assert (PROJECT_ROOT / relative_path).exists()


def test_one_c_io_package_does_not_introduce_forbidden_canonical_models() -> None:
    content = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ONE_C_IO_ROOT.glob("*.py")
    )

    forbidden_markers = [
        "class Client(",
        "class Customer(",
        "class Order(",
        "class Product(",
        "class Material(",
        "class WarehouseStock(",
        "class ProductionStatus(",
    ]

    for marker in forbidden_markers:
        assert marker not in content


def test_one_c_io_docs_document_test_copy_policy() -> None:
    content = (
        PROJECT_ROOT / "docs" / "architecture" / "one_c_test_copy_policy.md"
    ).read_text(encoding="utf-8")

    assert "test copy" in content
    assert "read_only: true" in content
    assert "production_allowed: false" in content
    assert "writes_allowed: false" in content
    assert "requires_test_copy: true" in content
```

### MODULE SOURCE â€” tests/unit/test_one_c_mapping_policy.py

`SHA256=0e0f4d9e751d41f07113c1c895ef121636072b26158707ba4403b2f1cad05df5`

```py
from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    MappingIssueType,
    apply_mapping_policy,
)
from forprint_accounting_registry_service.one_c_io.types import (
    DefaultValueCategory,
    FieldCriticality,
)


def test_mapping_policy_maps_known_fields() -> None:
    result = apply_mapping_policy(
        source_payload={"Код": "000001", "Назва": "ТОВ Тест"},
        definitions=[
            FieldMappingDefinition(source_field="Код", target_field="one_c_code"),
            FieldMappingDefinition(source_field="Назва", target_field="name"),
        ],
    )

    assert result.mapped_payload["one_c_code"] == "000001"
    assert result.mapped_payload["name"] == "ТОВ Тест"
    assert result.unmapped_fields == []


def test_mapping_policy_records_unmapped_fields() -> None:
    result = apply_mapping_policy(
        source_payload={
            "Код": "000001",
            "НевідомеПоле": "extra",
        },
        definitions=[
            FieldMappingDefinition(source_field="Код", target_field="one_c_code")
        ],
    )

    assert result.mapped_payload["one_c_code"] == "000001"
    assert result.unmapped_fields[0].field_name == "НевідомеПоле"
    assert result.issues[0].issue_type == MappingIssueType.UNMAPPED_FIELD


def test_critical_missing_field_requires_manual_review() -> None:
    result = apply_mapping_policy(
        source_payload={"Назва": "ТОВ Тест"},
        definitions=[
            FieldMappingDefinition(
                source_field="Код",
                target_field="one_c_code",
                required=True,
                criticality=FieldCriticality.CRITICAL,
                default_category=DefaultValueCategory.MANUAL_REVIEW_REQUIRED,
            )
        ],
    )

    assert result.mapped_payload == {}
    assert result.issues[0].issue_type == MappingIssueType.MANUAL_REVIEW_REQUIRED
    assert result.issues[0].severity == "critical"


def test_non_critical_missing_required_field_is_explicit_issue() -> None:
    result = apply_mapping_policy(
        source_payload={},
        definitions=[
            FieldMappingDefinition(
                source_field="Назва",
                target_field="name",
                required=True,
                criticality=FieldCriticality.NORMAL,
            )
        ],
    )

    assert result.issues[0].issue_type == MappingIssueType.REQUIRED_FIELD_MISSING


def test_configured_default_can_be_applied_explicitly() -> None:
    result = apply_mapping_policy(
        source_payload={},
        definitions=[
            FieldMappingDefinition(
                source_field="Валюта",
                target_field="currency",
                default_value="UAH",
                default_category=DefaultValueCategory.CONFIGURED_DEFAULT,
            )
        ],
    )

    assert result.mapped_payload["currency"] == "UAH"
```

### MODULE SOURCE â€” tests/unit/test_one_c_report_practical_extraction.py

`SHA256=9670732f9c303c72d809ea33315a3aa81ccb75515b7652294b6450ed1113c436`

```py
from pathlib import Path

from forprint_accounting_registry_service.one_c_io.export_parsers import (
    parse_one_c_export_file,
)
from forprint_accounting_registry_service.one_c_io.reports import (
    OneCReportCategory,
    OneCReportDefinition,
    OneCReportRequest,
    generate_report_snapshot_from_fixture,
)

FIXTURES = Path("tests/fixtures/one_c/exports")


def test_payment_register_fixture_parses_into_report_snapshot() -> None:
    result = parse_one_c_export_file(
        FIXTURES / "payment_register.yaml",
        target_kind="payment_register_snapshot",
    )
    assert result.batch is not None

    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="request-001",
        report_code=definition.report_code,
    )

    snapshot = generate_report_snapshot_from_fixture(
        snapshot_id="snapshot-001",
        definition=definition,
        request=request,
        rows=[row.raw_values for row in result.batch.rows],
    )

    assert snapshot.definition.accounting_only is True
    assert snapshot.production_allowed is False
    assert snapshot.rows[0].raw_values["document_number"] == "PAY-001"
```

### MODULE SOURCE â€” tests/unit/test_one_c_reports.py

`SHA256=e0b18b0d590464ddc3f1f2c7fd1b8a95431222a7d74d19dc9d82cc4344ab7b05`

```py
from forprint_accounting_registry_service.one_c_io.mapping import (
    MappingIssue,
    MappingIssueType,
)
from forprint_accounting_registry_service.one_c_io.reports import (
    OneCReportCategory,
    OneCReportDefinition,
    OneCReportExtractionResult,
    OneCReportRequest,
    generate_report_snapshot_from_fixture,
)


def test_report_definition_and_request_can_be_created() -> None:
    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="report-request-001",
        report_code=definition.report_code,
        period_from="2026-01-01",
        period_to="2026-01-31",
    )

    assert definition.accounting_only is True
    assert request.report_code == "payment_register_snapshot"


def test_report_snapshot_can_be_generated_from_fixture() -> None:
    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="report-request-001",
        report_code=definition.report_code,
    )

    snapshot = generate_report_snapshot_from_fixture(
        snapshot_id="report-snapshot-001",
        definition=definition,
        request=request,
        rows=[{"document": "PAY-001", "amount": 1000.0}],
    )

    assert snapshot.accounting_only if hasattr(snapshot, "accounting_only") else True
    assert snapshot.rows[0].raw_values["document"] == "PAY-001"
    assert snapshot.production_allowed is False


def test_report_extraction_result_can_include_mapping_issues() -> None:
    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="report-request-001",
        report_code=definition.report_code,
    )
    snapshot = generate_report_snapshot_from_fixture(
        snapshot_id="report-snapshot-001",
        definition=definition,
        request=request,
        rows=[],
    )

    result = OneCReportExtractionResult(
        snapshot=snapshot,
        mapping_issues=[
            MappingIssue(
                issue_type=MappingIssueType.UNMAPPED_FIELD,
                source_field="Unknown",
                message="Unknown field captured",
            )
        ],
    )

    assert result.mapping_issues[0].source_field == "Unknown"
```

### MODULE SOURCE â€” tests/unit/test_one_c_sandbox_sources.py

`SHA256=9e9f90efd7f64c0aeb562c6801d325dc1fbad84d8ee12ae2148ba2ae98e44022`

```py
import pytest
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyError,
    OneCSourceSafetyLevel,
    ensure_destructive_test_allowed,
    ensure_not_production_source,
)


def test_sandbox_source_can_be_registered_as_non_production() -> None:
    source = OneCSandboxSource(
        source_id="fixture-001",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/example.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
    )

    assert source.production_allowed is False
    assert source.sanitized is True


def test_destructive_test_requires_disposable_source_and_flag() -> None:
    source = OneCSandboxSource(
        source_id="sandbox-001",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
    )

    ensure_destructive_test_allowed(source, allow_destructive_flag=True)


def test_destructive_test_is_blocked_without_flag() -> None:
    source = OneCSandboxSource(
        source_id="sandbox-001",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
    )

    with pytest.raises(OneCSourceSafetyError):
        ensure_destructive_test_allowed(source, allow_destructive_flag=False)


def test_production_source_is_rejected() -> None:
    source = OneCSandboxSource(
        source_id="production-like",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="/production/one_c.1CD",
        safety_level=OneCSourceSafetyLevel.PRODUCTION_FORBIDDEN,
        production_allowed=True,
    )

    with pytest.raises(OneCSourceSafetyError):
        ensure_not_production_source(source)
```

### MODULE SOURCE â€” tests/unit/test_one_c_sandbox_write.py

`SHA256=fa25d252e377a7843d1b279615d7a06ff32c88ba1899cda2f5366d55a4645e4f`

```py
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.sandbox_write import (
    OneCWriteOperation,
    OneCWriteOperationType,
    OneCWritePlan,
    run_sandbox_write_experiment,
)


def build_write_plan(dry_run: bool = True) -> OneCWritePlan:
    return OneCWritePlan(
        plan_id="write-plan-001",
        dry_run=dry_run,
        operations=[
            OneCWriteOperation(
                operation_type=OneCWriteOperationType.UPSERT_DIRECTORY_ITEM,
                target_name="Counterparties",
                payload={"Code": "000001"},
            )
        ],
    )


def test_write_experiment_is_blocked_by_default() -> None:
    source = OneCSandboxSource(
        source_id="sandbox",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
    )

    result = run_sandbox_write_experiment(
        source=source,
        plan=build_write_plan(),
        allow_destructive_flag=False,
    )

    assert result.applied is False
    assert result.safety_checks[0].passed is False


def test_write_experiment_requires_disposable_source() -> None:
    source = OneCSandboxSource(
        source_id="readonly",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/readonly.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
        disposable=False,
        write_tests_allowed=False,
    )

    result = run_sandbox_write_experiment(
        source=source,
        plan=build_write_plan(),
        allow_destructive_flag=True,
    )

    assert result.applied is False
    assert result.result_metadata["blocked"] is True


def test_write_experiment_dry_run_does_not_mutate_source() -> None:
    source = OneCSandboxSource(
        source_id="disposable",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
    )

    result = run_sandbox_write_experiment(
        source=source,
        plan=build_write_plan(dry_run=True),
        allow_destructive_flag=True,
    )

    assert result.applied is False
    assert result.result_metadata["dry_run"] is True


def test_write_experiment_refuses_production_source() -> None:
    source = OneCSandboxSource(
        source_id="production",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="/production/one_c.1CD",
        safety_level=OneCSourceSafetyLevel.PRODUCTION_FORBIDDEN,
        production_allowed=True,
        disposable=True,
        write_tests_allowed=True,
    )

    result = run_sandbox_write_experiment(
        source=source,
        plan=build_write_plan(dry_run=False),
        allow_destructive_flag=True,
    )

    assert result.applied is False
```

### MODULE SOURCE â€” tests/unit/test_one_c_sandbox_write_hardening.py

`SHA256=fd4e4ae89b9e5573aa588e5ffad6e6ebf0a0da7681800aae748b19ca3ee8acd2`

```py
from pathlib import Path

from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.sandbox_write import (
    OneCWriteOperation,
    OneCWriteOperationType,
    OneCWritePlan,
    run_sandbox_write_experiment,
)
from forprint_accounting_registry_service.one_c_io.test_database_registry import (
    OneCTestDatabaseSource,
    create_working_copy_manifest,
)


def build_source() -> OneCSandboxSource:
    return OneCSandboxSource(
        source_id="disposable",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/test.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_DISPOSABLE,
        disposable=True,
        write_tests_allowed=True,
        production_allowed=False,
    )


def build_write_plan(dry_run: bool) -> OneCWritePlan:
    return OneCWritePlan(
        plan_id="write-plan",
        dry_run=dry_run,
        operations=[
            OneCWriteOperation(
                operation_type=OneCWriteOperationType.UPSERT_DIRECTORY_ITEM,
                target_name="Counterparties",
                payload={"Code": "000001"},
            )
        ],
    )


def test_write_requires_working_copy_for_non_dry_run() -> None:
    result = run_sandbox_write_experiment(
        source=build_source(),
        plan=build_write_plan(dry_run=False),
        allow_destructive_flag=True,
        working_copy=None,
    )

    assert result.applied is False
    assert result.result_metadata["missing_working_copy"] is True


def test_write_refuses_original_source_as_working_copy(tmp_path: Path) -> None:
    original = tmp_path / "original.1CD"
    original.write_text("original", encoding="utf-8")

    db_source = OneCTestDatabaseSource(
        source_id="source",
        source_path=str(original),
        is_sanitized=True,
    )
    working_copy = create_working_copy_manifest(
        db_source,
        working_copy_path=original,
        copy_file=False,
    )

    result = run_sandbox_write_experiment(
        source=build_source(),
        plan=build_write_plan(dry_run=False),
        allow_destructive_flag=True,
        working_copy=working_copy,
    )

    assert result.applied is False
    assert result.result_metadata["same_original_and_working_copy"] is True


def test_original_source_checksum_remains_unchanged(tmp_path: Path) -> None:
    original = tmp_path / "original.1CD"
    working = tmp_path / "working" / "copy.1CD"
    original.write_text("original", encoding="utf-8")

    db_source = OneCTestDatabaseSource(
        source_id="source",
        source_path=str(original),
        is_sanitized=True,
    )
    working_copy = create_working_copy_manifest(
        db_source,
        working_copy_path=working,
        copy_file=True,
    )

    result = run_sandbox_write_experiment(
        source=build_source(),
        plan=build_write_plan(dry_run=False),
        allow_destructive_flag=True,
        working_copy=working_copy,
    )

    assert result.applied is True
    assert result.result_metadata["original_source_unchanged"] is True
```

### MODULE SOURCE â€” tests/unit/test_one_c_sanitization_and_test_db_registry.py

`SHA256=ea5f92b77077beb6a3280a26d2367d23bfa5150b59756c6e52aadcfe0376acac`

```py
from pathlib import Path

import pytest
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSourceSafetyError,
)
from forprint_accounting_registry_service.one_c_io.sanitization import (
    OneCSanitizationError,
    OneCSanitizationMetadata,
    OneCSanitizationStatus,
    assert_source_is_sanitized,
)
from forprint_accounting_registry_service.one_c_io.test_database_registry import (
    OneCTestDatabaseManifest,
    OneCTestDatabaseSource,
    calculate_file_checksum,
    create_working_copy_manifest,
    register_sanitized_test_database_source,
)


def test_sanitized_test_db_source_can_be_registered(tmp_path: Path) -> None:
    source_path = tmp_path / "sanitized.1CD"
    source_path.write_text("synthetic sanitized db", encoding="utf-8")

    source = register_sanitized_test_database_source(
        source_path=source_path,
        source_id="sanitized-db",
    )

    manifest = OneCTestDatabaseManifest()
    manifest.register(source)

    assert manifest.get_source("sanitized-db") is not None
    assert source.checksum is not None


def test_unsanitized_source_is_rejected_for_processing() -> None:
    metadata = OneCSanitizationMetadata(
        status=OneCSanitizationStatus.NOT_SANITIZED,
        real_1c_data=True,
        sanitized=False,
    )

    with pytest.raises(OneCSanitizationError):
        assert_source_is_sanitized(metadata)


def test_production_source_is_rejected() -> None:
    source = OneCTestDatabaseSource(
        source_id="prod",
        source_path="/production/one_c.1CD",
        is_sanitized=True,
        production_allowed=True,
    )

    manifest = OneCTestDatabaseManifest()

    with pytest.raises(OneCSourceSafetyError):
        manifest.register(source)


def test_non_disposable_source_rejects_destructive_write_mode() -> None:
    source = OneCTestDatabaseSource(
        source_id="unsafe-write",
        source_path="local_sandbox/one_c_databases/test.1CD",
        is_sanitized=True,
        is_disposable=False,
        writes_allowed=True,
        destructive_write_allowed=True,
        metadata={"sandbox_mode": True},
    )

    manifest = OneCTestDatabaseManifest()

    with pytest.raises(OneCSourceSafetyError):
        manifest.register(source)


def test_source_checksum_is_recorded_if_sample_file_exists(tmp_path: Path) -> None:
    source_path = tmp_path / "sample.1CD"
    source_path.write_text("sample", encoding="utf-8")

    checksum = calculate_file_checksum(source_path)

    assert checksum.value
    assert checksum.file_path == str(source_path)


def test_working_copy_manifest_references_original_but_is_separate(tmp_path: Path) -> None:
    original = tmp_path / "original.1CD"
    working = tmp_path / "working_copies" / "copy.1CD"
    original.write_text("original", encoding="utf-8")

    source = register_sanitized_test_database_source(
        source_path=original,
        source_id="source-001",
    )
    manifest = create_working_copy_manifest(source, working, copy_file=True)

    assert manifest.original_source_path != manifest.working_copy_path
    assert working.exists()
    assert original.read_text(encoding="utf-8") == "original"
```

### MODULE SOURCE â€” tests/unit/test_one_c_schema_probe.py

`SHA256=bc17d23b00654803bb55dc2c6b88dfec663057c178a9407cf50a9899b4cfb0af`

```py
import pytest
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyError,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.schema_probe import (
    probe_sanitized_source_schema,
)


def test_direct_discovery_handles_synthetic_fixture() -> None:
    source = OneCSandboxSource(
        source_id="fixture",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="tests/fixtures/one_c/exports/counterparties.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
    )

    result = probe_sanitized_source_schema(
        source,
        fixture_tables={"Counterparties": [{"Code": "000001", "Unknown": "preserve"}]},
    )

    assert result.supported is True
    assert result.report is not None
    assert result.report.canonical_truth is False


def test_direct_discovery_handles_unsupported_file_gracefully() -> None:
    source = OneCSandboxSource(
        source_id="unsupported",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="local_sandbox/one_c_databases/missing.1CD",
        safety_level=OneCSourceSafetyLevel.SANDBOX_READONLY,
    )

    result = probe_sanitized_source_schema(source)

    assert result.supported is False
    assert result.status == "unsupported_source"
    assert result.diagnostics


def test_direct_discovery_refuses_production_source() -> None:
    source = OneCSandboxSource(
        source_id="prod",
        source_kind=OneCSourceKind.FILE_DATABASE_COPY,
        path="/production/one_c.1CD",
        safety_level=OneCSourceSafetyLevel.PRODUCTION_FORBIDDEN,
        production_allowed=True,
    )

    with pytest.raises(OneCSourceSafetyError):
        probe_sanitized_source_schema(source)
```

### MODULE SOURCE â€” tests/unit/test_one_c_snapshot.py

`SHA256=3747942b9428dd72e28e02608d90c1cbb8b34363763a28f1c69babced0c01be0`

```py
from pathlib import Path

from forprint_accounting_registry_service.services.one_c_snapshot import (
    ALLOWED_SNAPSHOT_EXTENSIONS,
    list_snapshot_files,
    validate_snapshot_file,
)


def test_validate_snapshot_file_rejects_missing_file() -> None:
    assert validate_snapshot_file(Path("/tmp/not-existing-file.csv")) is False


def test_validate_snapshot_file_accepts_allowed_extensions(tmp_path: Path) -> None:
    allowed_files = [
        tmp_path / "counterparties.csv",
        tmp_path / "nomenclature.xlsx",
        tmp_path / "snapshot.xml",
        tmp_path / "snapshot.json",
    ]

    for path in allowed_files:
        path.write_text("test", encoding="utf-8")
        assert validate_snapshot_file(path) is True


def test_validate_snapshot_file_rejects_disallowed_extension(tmp_path: Path) -> None:
    path = tmp_path / "readme.txt"
    path.write_text("ignore", encoding="utf-8")

    assert validate_snapshot_file(path) is False


def test_list_snapshot_files_returns_only_allowed_extensions(tmp_path: Path) -> None:
    valid_csv = tmp_path / "counterparties.csv"
    valid_json = tmp_path / "snapshot.json"
    invalid_txt = tmp_path / "readme.txt"

    valid_csv.write_text("name\nТОВ Тест\n", encoding="utf-8")
    valid_json.write_text("{}", encoding="utf-8")
    invalid_txt.write_text("ignore", encoding="utf-8")

    result = list_snapshot_files(tmp_path)

    assert valid_csv in result
    assert valid_json in result
    assert invalid_txt not in result


def test_list_snapshot_files_returns_empty_list_for_missing_directory(tmp_path: Path) -> None:
    missing_dir = tmp_path / "missing"

    assert list_snapshot_files(missing_dir) == []


def test_allowed_snapshot_extensions_are_controlled() -> None:
    assert ALLOWED_SNAPSHOT_EXTENSIONS == {".csv", ".xlsx", ".xml", ".json"}
```

### MODULE SOURCE â€” tests/unit/test_one_c_source_manifest.py

`SHA256=8ad5e39115e4b82e7a92927183631d213b85c5580d7e74a9ae3b2f0055ffbd88`

```py
from forprint_accounting_registry_service.one_c_io.sandbox_sources import (
    OneCSandboxSource,
    OneCSourceKind,
    OneCSourceSafetyLevel,
)
from forprint_accounting_registry_service.one_c_io.source_manifest import (
    OneCSourceManifest,
)


def test_source_manifest_can_be_serialized_and_read() -> None:
    source = OneCSandboxSource(
        source_id="fixture-001",
        source_kind=OneCSourceKind.JSON_FIXTURE,
        path="examples/one_c/raw_exports/counterparties_example.json",
        safety_level=OneCSourceSafetyLevel.READONLY_FIXTURE,
    )
    manifest = OneCSourceManifest()
    manifest.add_source(source)

    restored = OneCSourceManifest.from_json_string(manifest.to_json_string())

    assert restored.production_allowed is False
    assert restored.real_1c_data is False
    assert restored.get_source("fixture-001") is not None
```

### MODULE SOURCE â€” tests/unit/test_one_c_staging_mapping.py

`SHA256=6cbded4e70931953c0804b9c0a8d5ddb9d33bf62e274e69d55fa2e4fe0825bbc`

```py
from forprint_accounting_registry_service.one_c_io.directories import (
    OneCDirectoryItemSnapshot,
    OneCDirectoryKind,
    OneCDirectorySnapshot,
)
from forprint_accounting_registry_service.one_c_io.discovery import (
    create_raw_extract_batch,
)
from forprint_accounting_registry_service.one_c_io.mapping import (
    FieldMappingDefinition,
    MappingIssueType,
)
from forprint_accounting_registry_service.one_c_io.reports import (
    OneCReportCategory,
    OneCReportDefinition,
    OneCReportRequest,
    generate_report_snapshot_from_fixture,
)
from forprint_accounting_registry_service.one_c_io.staging import (
    apply_mapping_to_staging_payload,
    directory_import_to_staging_records,
    raw_extract_batch_to_staging_records,
    report_snapshot_to_staging_records,
)
from forprint_accounting_registry_service.one_c_io.types import FieldCriticality


def test_raw_extract_maps_to_staging() -> None:
    batch = create_raw_extract_batch(
        source_id="snapshot-001",
        source_name="fixture",
        table_name="Counterparties",
        records=[{"Код": "000001", "Unknown": "preserve"}],
    )

    records = raw_extract_batch_to_staging_records(batch)

    assert records[0].record_type == "raw_extract:Counterparties"
    assert records[0].raw_payload["record"]["Unknown"] == "preserve"


def test_directory_import_maps_to_staging() -> None:
    snapshot = OneCDirectorySnapshot(
        snapshot_id="dir-001",
        directory_kind=OneCDirectoryKind.NOMENCLATURE_ACCOUNTING_REFERENCES,
        source_name="fixture",
        items=[
            OneCDirectoryItemSnapshot(
                item_id="item-001",
                raw_payload={"Name": "Example"},
                normalized_payload={"name": "Example"},
            )
        ],
    )

    records = directory_import_to_staging_records(snapshot)

    assert records[0].raw_payload["accounting_reference_only"] is True


def test_report_snapshot_maps_to_staging() -> None:
    definition = OneCReportDefinition(
        report_code="payment_register_snapshot",
        category=OneCReportCategory.PAYMENT_REGISTER_SNAPSHOT,
        title="Payment register",
    )
    request = OneCReportRequest(
        request_id="request-001",
        report_code=definition.report_code,
    )
    snapshot = generate_report_snapshot_from_fixture(
        snapshot_id="report-001",
        definition=definition,
        request=request,
        rows=[{"payment": "PAY-001"}],
    )

    records = report_snapshot_to_staging_records(snapshot)

    assert records[0].record_type.startswith("report:")
    assert records[0].raw_payload["accounting_only"] is True


def test_missing_critical_field_creates_mapping_issue() -> None:
    result = apply_mapping_to_staging_payload(
        source_payload={},
        definitions=[
            FieldMappingDefinition(
                source_field="Код",
                target_field="one_c_code",
                required=True,
                criticality=FieldCriticality.CRITICAL,
            )
        ],
    )

    assert result.issues[0].issue_type == MappingIssueType.MANUAL_REVIEW_REQUIRED
```

### MODULE SOURCE â€” tests/unit/test_product_model.py

`SHA256=87571711d1999288e338b216f5598b18edcedeb5950bf76195e1d4a37bef0992`

```py
from forprint_accounting_registry_service.models.product import (
    AttributeType,
    Product,
    ProductAttribute,
    ProductDomain,
    ProductLifecycleStatus,
)


def test_product_supports_configurable_attributes() -> None:
    product = Product(
        name="Візитка",
        domain=ProductDomain.PRINT,
        attributes=[
            ProductAttribute(
                code="paper",
                name="Папір",
                attribute_type=AttributeType.ENUM,
                required=True,
                configurable=True,
                affects_price=True,
                affects_production=True,
                allowed_values=["300 г", "350 г"],
            )
        ],
    )

    assert product.domain == ProductDomain.PRINT
    assert product.attributes[0].affects_price is True
    assert product.attributes[0].affects_production is True


def test_product_supports_broad_advertising_information_domains() -> None:
    digital_product = Product(
        name="Digital рекламний банер",
        domain=ProductDomain.DIGITAL,
        lifecycle_status=ProductLifecycleStatus.PLANNED,
        category_code="digital_ad_banner",
        unit="item",
    )

    assert digital_product.domain == ProductDomain.DIGITAL
    assert digital_product.lifecycle_status == ProductLifecycleStatus.PLANNED
    assert digital_product.category_code == "digital_ad_banner"


def test_product_keeps_one_c_mapping_fields_as_accounting_projection() -> None:
    product = Product(
        name="Банер 440 г з 1С",
        domain=ProductDomain.PRINT,
        lifecycle_status=ProductLifecycleStatus.ACTIVE,
        one_c_id="one-c-nomenclature-001",
        one_c_code="BNR-440",
        one_c_raw_name="Банер 440 3.2 Китай",
    )

    assert product.one_c_id == "one-c-nomenclature-001"
    assert product.one_c_code == "BNR-440"
    assert product.one_c_raw_name == "Банер 440 3.2 Китай"


def test_product_attribute_can_be_non_configurable_internal_reference() -> None:
    product = Product(
        name="Облікова номенклатурна позиція",
        domain=ProductDomain.PRINT,
        attributes=[
            ProductAttribute(
                code="one_c_code",
                name="Код 1С",
                attribute_type=AttributeType.TEXT,
                required=False,
                configurable=False,
                visible_to_client=False,
                visible_to_manager=True,
                affects_price=False,
                affects_production=False,
            )
        ],
    )

    assert product.attributes[0].configurable is False
    assert product.attributes[0].visible_to_client is False
    assert product.attributes[0].affects_price is False
```

### MODULE SOURCE â€” tests/unit/test_storage_boundaries.py

`SHA256=cc4f0f2a7e9f87fc506bbc3d3c456edb1a6bf473b770fee1e86f8742470afac6`

```py
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
STORAGE_MODELS_PATH = (
    PROJECT_ROOT
    / "app"
    / "forprint_accounting_registry_service"
    / "storage"
    / "models.py"
)


def test_storage_models_do_not_introduce_forbidden_canonical_model_names() -> None:
    content = STORAGE_MODELS_PATH.read_text(encoding="utf-8")

    forbidden_class_markers = [
        "class Client(",
        "class Customer(",
        "class Order(",
        "class Product(",
        "class Material(",
        "class Invoice(",
        "class Payment(",
    ]

    for marker in forbidden_class_markers:
        assert marker not in content


def test_storage_models_use_explicit_accounting_and_one_c_names() -> None:
    content = STORAGE_MODELS_PATH.read_text(encoding="utf-8")

    required_names = [
        "OneCRawSnapshot",
        "OneCStagingRecord",
        "OneCMappingRecord",
        "OneCImportJob",
        "OneCExportJob",
        "AccountingReconciliationJob",
        "AccountingDocument",
        "InvoiceAccountingReference",
        "PaymentAccountingReference",
        "OrderAccountingReference",
    ]

    for name in required_names:
        assert name in content


def test_storage_boundary_docs_exist() -> None:
    required_docs = [
        "docs/architecture/accounting_storage_foundation.md",
        "docs/architecture/one_c_snapshot_staging_flow.md",
        "docs/architecture/accounting_storage_boundaries.md",
    ]

    for relative_path in required_docs:
        assert (PROJECT_ROOT / relative_path).exists()
```

### MODULE SOURCE â€” tests/unit/test_storage_database.py

`SHA256=0d904e97e536a6f53ff48d0d4067d69314e6d0022523569c553fb7b34fdaa5c8`

```py
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from sqlalchemy import inspect


def test_storage_database_can_be_initialized() -> None:
    engine = create_sqlite_engine(":memory:")

    init_storage(engine)

    table_names = set(inspect(engine).get_table_names())

    required_tables = {
        "one_c_raw_snapshots",
        "one_c_staging_records",
        "one_c_mapping_records",
        "one_c_import_jobs",
        "one_c_export_jobs",
        "accounting_reconciliation_jobs",
        "accounting_documents",
        "order_accounting_references",
        "invoice_accounting_references",
        "payment_accounting_references",
    }

    assert required_tables.issubset(table_names)
```

### MODULE SOURCE â€” tests/unit/test_storage_records.py

`SHA256=4f63dbc2d37fadb49d8b866bf81c7c441745cc5bfb8c420ff41ecef346a2eacd`

```py
from forprint_accounting_registry_service.storage.database import (
    create_sqlite_engine,
    init_storage,
)
from forprint_accounting_registry_service.storage.models import (
    AccountingDocument,
    AccountingReconciliationJob,
    InvoiceAccountingReference,
    OneCExportJob,
    OneCImportJob,
    OneCMappingRecord,
    OneCRawSnapshot,
    OneCStagingRecord,
    OrderAccountingReference,
    PaymentAccountingReference,
)
from forprint_accounting_registry_service.storage.repository import (
    get_record_by_id,
    save_record,
)
from sqlmodel import Session


def create_test_session() -> Session:
    engine = create_sqlite_engine(":memory:")
    init_storage(engine)
    return Session(engine)


def test_one_c_raw_snapshot_can_be_stored_and_read() -> None:
    with create_test_session() as session:
        snapshot = save_record(
            session,
            OneCRawSnapshot(
                snapshot_type="counterparties",
                source_name="one_c_manual_export",
                file_name="counterparties.csv",
                raw_metadata={"encoding": "utf-8"},
            ),
        )

        stored = get_record_by_id(session, OneCRawSnapshot, snapshot.id)

        assert stored is not None
        assert stored.snapshot_type == "counterparties"
        assert stored.raw_metadata["encoding"] == "utf-8"


def test_one_c_staging_record_can_be_stored_and_read() -> None:
    with create_test_session() as session:
        record = save_record(
            session,
            OneCStagingRecord(
                snapshot_id="snapshot-001",
                record_type="counterparty",
                source_row_number=1,
                one_c_id="one-c-001",
                raw_payload={"name": "ТОВ Тест"},
                normalized_payload={"name": "ТОВ Тест"},
            ),
        )

        stored = get_record_by_id(session, OneCStagingRecord, record.id)

        assert stored is not None
        assert stored.record_type == "counterparty"
        assert stored.raw_payload["name"] == "ТОВ Тест"


def test_one_c_mapping_record_can_be_stored_and_read() -> None:
    with create_test_session() as session:
        mapping = save_record(
            session,
            OneCMappingRecord(
                entity_type="accounting_counterparty_reference",
                internal_accounting_id="internal-001",
                one_c_id="one-c-001",
                one_c_code="000001",
                one_c_name="ТОВ Тест",
            ),
        )

        stored = get_record_by_id(session, OneCMappingRecord, mapping.id)

        assert stored is not None
        assert stored.internal_accounting_id == "internal-001"
        assert stored.one_c_code == "000001"


def test_import_export_and_reconciliation_jobs_can_be_created() -> None:
    with create_test_session() as session:
        import_job = save_record(
            session,
            OneCImportJob(
                source_name="manual_csv",
                snapshot_id="snapshot-001",
                records_total=10,
                job_metadata={"profile": "counterparties"},
            ),
        )
        export_job = save_record(
            session,
            OneCExportJob(
                export_profile="daily_accounting_export",
                records_total=5,
                job_metadata={"target": "one_c"},
            ),
        )
        reconciliation_job = save_record(
            session,
            AccountingReconciliationJob(
                reconciliation_scope="one_c_mapping",
                period_from="2026-01-01",
                period_to="2026-01-31",
                issues_count=0,
            ),
        )

        assert get_record_by_id(session, OneCImportJob, import_job.id) is not None
        assert get_record_by_id(session, OneCExportJob, export_job.id) is not None
        assert (
            get_record_by_id(session, AccountingReconciliationJob, reconciliation_job.id)
            is not None
        )


def test_accounting_document_and_invoice_payment_references_are_accounting_only() -> None:
    with create_test_session() as session:
        document = save_record(
            session,
            AccountingDocument(
                accounting_document_type="invoice",
                document_number="INV-001",
                document_state="draft",
                source_reference_id="external-order-001",
                payload={"note": "accounting shell only"},
            ),
        )
        invoice_ref = save_record(
            session,
            InvoiceAccountingReference(
                invoice_reference_id="invoice-ref-001",
                accounting_document_id=document.id,
                source_reference_id="external-order-001",
                invoice_state="draft",
                amount_total=1000.0,
                currency="UAH",
            ),
        )
        payment_ref = save_record(
            session,
            PaymentAccountingReference(
                payment_reference_id="payment-ref-001",
                invoice_reference_id=invoice_ref.invoice_reference_id,
                payment_state="created",
                amount_total=500.0,
                currency="UAH",
            ),
        )

        stored_invoice = get_record_by_id(session, InvoiceAccountingReference, invoice_ref.id)
        stored_payment = get_record_by_id(session, PaymentAccountingReference, payment_ref.id)

        assert stored_invoice is not None
        assert stored_invoice.source_reference_id == "external-order-001"
        assert stored_payment is not None
        assert stored_payment.payment_state == "created"


def test_order_accounting_reference_does_not_own_operational_workflow() -> None:
    with create_test_session() as session:
        order_reference = save_record(
            session,
            OrderAccountingReference(
                external_order_id="order-001",
                source_module="future_operational_registry",
                reference_kind="invoice_source_reference",
                description="Reference only, not workflow state.",
            ),
        )

        stored = get_record_by_id(session, OrderAccountingReference, order_reference.id)

        assert stored is not None
        assert stored.external_order_id == "order-001"
        assert stored.reference_kind == "invoice_source_reference"
```

## Blueprint context bodies


### BLUEPRINT CONTEXT â€” coordination/human_intent/modules/forprint_accounting_registry_service.yaml

`SHA256=e7dfccee8b5c7eb641000fce43dd01d835a8af0c7d5dc5930d67ce129f31abdb`

```yaml
schema_version: forprint_module_human_intent_ledger_v0_1
module_id: forprint_accounting_registry_service
display_name: ForPrint Accounting Registry Service
authority: planning_context_not_release_authority
status: active_planning_context
append_only: true
intents:
  - status: AGREED
    text: 'Accounting Registry Service є owner accounts receivable workflow: invoice/order, amount due/paid, due
      date, payment status, overdue days, promise-to-pay date.'
    context: CRM і Telegram лише допомагають комунікувати.
    roadmap: ''
    intent_id: HI-FP-ACCOUNTING-REGISTRY-SERVICE-001
  - status: AGREED
    text: 'Базовий state machine: DUE -> OVERDUE_SOFT -> OVERDUE_REMINDER -> PROMISE_TO_PAY -> WAITING_PROMISED_DATE
      -> OVERDUE_ESCALATED -> HUMAN_ATTENTION.'
    context: Клієнтська відповідь змінює стан workflow, а не просто додається коментарем.
    roadmap: ''
    intent_id: HI-FP-ACCOUNTING-REGISTRY-SERVICE-002
  - status: AGREED
    text: 'Side states: DISPUTED, PARTIAL_PAYMENT, PAYMENT_PENDING_RECONCILIATION, CONTACT_UNAVAILABLE, PAUSED,
      PAID.'
    context: Щоб не штовхати кожен кейс в одну лінійну схему.
    roadmap: ''
    intent_id: HI-FP-ACCOUNTING-REGISTRY-SERVICE-003
  - status: AGREED
    text: AI може адаптувати тон нагадування, але не може самостійно блокувати клієнта, зупиняти production/shipping,
      скасовувати кредит чи списувати борг.
    context: Це рішення людини/політики.
    roadmap: ''
    intent_id: HI-FP-ACCOUNTING-REGISTRY-SERVICE-004
  - status: AGREED
    text: 'Cadence нагадувань має бути конфігурованим: quiet hours, max per day, importance/history і поточний контекст
      клієнта.'
    context: Не перетворювати автоматизацію на спам.
    roadmap: ''
    intent_id: HI-FP-ACCOUNTING-REGISTRY-SERVICE-005
  - status: RECOVERED
    text: Для procurement/goods receipt потрібен intake з Excel/CSV/PDF, OCR для фото/сканів і focused operator
      review.
    context: Попередній портфель уже містив цей напрям.
    roadmap: ''
    intent_id: HI-FP-ACCOUNTING-REGISTRY-SERVICE-006
  - status: RECOVERED
    text: Supplier alias learning і fuzzy candidate mapping корисні, але OCR/matching не повинні ставати silent
      truth.
    context: Підтверджені mappings можна перевикористовувати.
    roadmap: ''
    intent_id: HI-FP-ACCOUNTING-REGISTRY-SERVICE-007
  - status: AGREED
    text: Фактична production variance впливає на actual cost analytics через Accounting, але первинні physical
      facts приходять від production/Warehouse.
    context: Не переносити production measurement у бухгалтерський модуль.
    roadmap: ''
    intent_id: HI-FP-ACCOUNTING-REGISTRY-SERVICE-008
  - intent_id: HI-FP-ACCOUNTING-REGISTRY-009
    status: AGREED
    text: 'Reprint responsibility and customer billing consequence are separate fields: an internal-defect reprint
      may consume material/cost without a new customer charge.'
    context: Accounting records the financial consequence; OCR owns the reprint execution workflow.
    roadmap: ACC-REPRINT-01
  - intent_id: HI-FP-ACCOUNTING-REGISTRY-010
    status: AGREED
    text: Proof/sample purpose does not automatically mean free; billing policy can be FREE, INCLUDED or PAID per
      case/policy.
    context: Do not infer finance solely from the legacy proba token.
    roadmap: ACC-PROOF-01
  - intent_id: HI-FP-ACCOUNTING-REGISTRY-011
    status: AGREED
    text: Accounting should support incoming supplier-document parsing for Excel, PDF, Word and scans/photos with
      human confirmation when financial facts are uncertain.
    context: Repeated supplier templates should become increasingly deterministic.
    roadmap: ACC-GOODS-01
  - intent_id: HI-FP-ACCOUNTING-REGISTRY-012
    status: AGREED
    text: Supplier-specific descriptions/part numbers map to one canonical material while preserving supplier alias/SKU
      provenance.
    context: The organization's preferred material identity remains stable.
    roadmap: ACC-GOODS-02
  - intent_id: HI-FP-ACCOUNTING-REGISTRY-013
    status: AGREED
    text: A mature Accounting roadmap may include bounded preauthorized conditional payment mandates with strict
      limits, idempotency and audit.
    context: Early stages require confirmation; auto-payment is later high-risk automation.
    roadmap: ACC-PAYMENT-01
```

### BLUEPRINT CONTEXT â€” coordination/module_policy/forprint_accounting_registry_service/goods_receipt_automation_target_state_v0_1_20260826.md

`SHA256=dac053bd4efebeb5ce71325d447db2e7dac09090b41b23848503b2beab468c30`

```md
# Accounting Registry — Goods Receipt Automation Target State v0.1

Status: PROVISIONAL / SYNTHETIC / OWNER REFINEMENT EXPECTED

Goal: reduce manual goods-receipt entry to a short review/confirmation workflow.

Inputs include Excel/structured supplier files, PDF documents, and scans/photos through OCR.

Target flow:

`source -> identify supplier/document -> parse/OCR -> supplier item mapping -> canonical Library material -> extract quantity/price/tax/document facts -> confidence -> operator review/correction -> confirm/post -> audit trail`

One canonical material may have many supplier descriptions/part numbers:

`supplier_id + supplier_part_number + supplier_description -> canonical_material_id`

Confirmed mappings should reduce future manual work.

OCR/fuzzy/AI matching may propose candidates, but low-confidence material, quantity, price or
financial facts must not silently post.

Preserve original source, parsed values, mapping/confidence, corrections, confirmation evidence and
final posted facts.

Canonical material semantics belong to Library.

<!-- supplier-document-business-partner-clarification-2026-09-01:start -->
## 2026-09-01 clarification

Supplier identity references the shared Business Partner master; Accounting owns financial attributes
and posting consequences.

Preserve supplier item provenance:
supplier_business_partner_id + supplier_part_number + supplier_description -> canonical Library material ID.

Incoming supplier documents may be Excel/structured, PDF, Word-like or scans/photos. Low-confidence
financial facts remain human-confirmed.

Future conditional payment mandates are later high-risk automation requiring preauthorization, limits,
duplicate prevention, idempotency, audit and staged activation.
<!-- supplier-document-business-partner-clarification-2026-09-01:end -->
```

### BLUEPRINT CONTEXT â€” coordination/module_policy/forprint_accounting_registry_service/module_policy.md

`SHA256=c046b321858ea0008659ff3edf3e67e91d57c430e5a95b5dd11ee5e9be7a5d52`

```md
# Module Policy — ForPrint Accounting Registry Service

## Module ID

```text
forprint_accounting_registry_service
```

## Priority

```text
selective
```

## Development status

```text
sandbox_1c_import_export_ready
```

## Strategic role

Accounting boundary and 1C synchronization/staging module.

## Main goals

- `Maintain accounting-only references and 1C staging.`
- `Support sanitized import/export experiments.`
- `Prepare mappings and reconciliation logic.`
- `Keep live 1C write and automatic posting forbidden until explicitly approved.`

## Owns

- `accounting_references`
- `one_c_raw_snapshot`
- `one_c_staging_record`
- `one_c_mapping_record`
- `import_job`
- `export_job`
- `reconciliation_job`
- `sandbox_one_c_io`

## Must not own

- `operational_client_registry`
- `operational_order_registry`
- `canonical_catalog_truth`
- `crm_workflow`
- `calculator_logic`
- `warehouse_stock_truth`

## Next focus

- `Maintain v0.5 sandbox readiness.`
- `Wait for real sanitized 1C samples before v0.6.`
- `Do not proceed to live 1C integration yet.`

## Adoption rule

This module policy is strategic guidance. It does not automatically authorize large refactors or broad rewrites. The module should compare this policy with its current implementation and report alignment, conflicts or questions to Blueprint.
```

### BLUEPRINT CONTEXT â€” coordination/roadmaps/details/forprint_system_blueprint/accounts_receivable_collection_direction_v0_1.md

`SHA256=39be8a528eda77172adaf5b092a63efbbf6365fa8a04ef38e2066fe343c0e745`

```md
<!-- Integrated from Evening Architecture Package v1.0 on 2026-08-30. This document does not change release/H10 authority by itself. -->

# 03. Payments & Accounts Receivable Collection v1.0

Primary owner: `forprint_accounting_registry_service`.

Supporting:
- `forprint_crm`
- `telegram_bot`
- `forprint_operations_control_registry`
- `forprint_integration_gateway`

## Receivable model

```yaml
invoice_id: ...
order_id: ...
customer_id: ...
organization_id: ...
amount_due: ...
amount_paid: ...
due_date: ...
payment_status: ...
overdue_days: ...
promise_to_pay_date: null
collection_state: ...
```

## Payment preference/order start

CRM/Accounting determine whether customer uses:
- prepayment;
- postpay/contract;
- invoice with VAT;
- another allowed policy.

New client without known preference can be asked via Telegram.

Payment reconciliation comes from Accounting + bank/integration evidence.
If payment is detected even without payment slip, order is updated and customer
is informed.

## Collection state machine

```text
DUE
→ OVERDUE_SOFT
→ OVERDUE_REMINDER
→ PROMISE_TO_PAY
→ WAITING_PROMISED_DATE
→ OVERDUE_ESCALATED
→ HUMAN_ATTENTION
```

Side states:
- DISPUTED
- PARTIAL_PAYMENT
- PAYMENT_PENDING_RECONCILIATION
- CONTACT_UNAVAILABLE
- PAUSED
- PAID

## Dialogue policy

Tone:
- friendly;
- polite;
- non-threatening;
- persistent;
- contextual.

Cadence configurable by:
- days overdue;
- amount;
- customer history;
- promised date;
- dispute state;
- customer tier;
- communication availability.

Не зашивати одну універсальну формулу 1/2/4 messages per day.

## Structured extraction

«Оплачу в п'ятницю»:
```yaml
promise_to_pay_date: Friday
```

«Бухгалтер буде в понеділок»:
```yaml
next_action_at: Monday
```

«Ми вже оплатили»:
→ payment reconciliation request.

«Не згодні з сумою»:
→ DISPUTED + pause normal reminder escalation.

## AI boundary

AI може адаптувати wording, аналізувати діалог, уникати повторів.

AI не може самостійно:
- списати борг;
- змінити credit limit;
- заблокувати customer;
- заборонити відвантаження;
- визнати payment без reconciliation.

## Audit history

Зберігати:
- sent reminders;
- customer replies;
- promises;
- due-date changes;
- dispute events;
- reconciliation;
- state transitions;
- timestamps/source.
```

### BLUEPRINT CONTEXT â€” coordination/roadmaps/details/forprint_system_blueprint/evening_architecture_module_amendments_v0_1/forprint_accounting_registry_service.md

`SHA256=f18aaed4bf3c50beb8fad9168e5ed7c26c1605bac16f1d72f5ed84dc4a013132`

```md
# forprint_accounting_registry_service — Evening Architecture Roadmap Amendment v0.1

Status: Blueprint planning projection; no module release/prompt activation.

## Planned additions

- receivable lifecycle
- payment reconciliation
- promise-to-pay
- collection state machine
- adaptive bounded reminders

## Execution boundary

Before implementation resolve active roadmap step, applicable governance
revision, dependencies, validators and acceptance evidence.
```

### BLUEPRINT CONTEXT â€” coordination/roadmaps/details/forprint_system_blueprint/portfolio_full_horizon_target_states_v0_1.md

`SHA256=01bc35e630c4a42c3f360aa658c4d67a0d008fd23551bc62904a59163c71861a`

```md
# ForPrint Portfolio Full-Horizon Target States v0.1

Status: `PROPOSED_PORTFOLIO_BASELINE_REQUIRES_OWNER_REVIEW`

Normal module implementation remains held.

## forprint_system_blueprint

Priority: `P0`
Inventory state: `STRONG_EXISTING_FOUNDATION`
Role: Architecture/governance/portfolio coordination

### AGREED / RECOVERED
- Global architecture, boundaries, standards, Human Intent, dependency/readiness balance.

- Historical Asset Index is accepted as real portfolio work, implemented as a projection over domain-owned asset, technical and operational evidence rather than as a new competing source of truth.
- The retrieval host remains an explicit architecture decision; the existing Semantic Retrieval candidate must not be promoted automatically merely because historical indexing is required.

- The working portfolio host for the first durable Process Manager capability is Operations Control Registry; no standalone Process Manager module is created initially.
- Process Manager is deliberately designed as a hosted-but-extractable capability, so later separation requires evidence rather than an early architectural guess.

### SYNTHETIC / PROPOSED
- Stronger automated portfolio health/decision-support projections.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.
11. Define the cross-module Historical Asset Index contract over Library reference semantics, Prepress technical asset facts and Operations Control Registry order/job/revision state.
12. Define candidate retrieval stages as cheap scoped retrieval followed by deeper comparison of a small candidate set and explicit human/customer selection when ambiguity remains.
13. Resolve the final hosted-capability location only after comparing an existing-host implementation with the noncanonical Semantic Retrieval module candidate.
14. Govern the hosted Process Manager boundary so process truth, domain truth, transport state and human-facing workflow UI remain explicitly separated.
15. Review extraction triggers after real usage evidence, including independent scaling, availability, topology, ownership pressure and cross-domain coupling.

### Dependencies
- none / portfolio owner

Human control surfaces: `DEVELOPER_AUDIT, ADMIN_FACING`
Module value test: `KEEP`

## calculator_engine

Priority: `P0`
Inventory state: `OWNER_DIRECTION_CLEAR_DEEP_INVENTORY_REQUIRED`
Role: Calculation, quote and structured Job Specification engine

### AGREED / RECOVERED
- Calculation/quote/order drafts, price/material/time estimates, early visual configuration, exact reference set recovered.

### SYNTHETIC / PROPOSED
- Reusable constructor family, outsourcing decisions and partner-adapter integration.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_library`
- `forprint_contract_registry`
- `forprint_prepress_hub`
- `warehouse_service`

Human control surfaces: `USER_FACING, OPERATOR_FACING, ADMIN_FACING`
Module value test: `KEEP`

## forprint_library

Priority: `P0`
Inventory state: `OWNER_DIRECTION_CLEAR`
Role: Canonical semantic/catalog/reference and shared UI publication authority

### AGREED / RECOVERED
- Canonical products/materials/services/operations/aliases/profiles; shared UI package publication.

- Historical/reference asset semantics use stable asset and revision references; Library may own canonical reference-media metadata where applicable, while customer/order/production truth remains with its domain owners.
- Historical Asset Index entries are projections over authoritative sources; an index/search result never becomes canonical asset, order or production truth.

### SYNTHETIC / PROPOSED
- Fast capability/semantic discovery and mature version/adoption lifecycle.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.
11. Define stable historical/reference asset metadata semantics including asset ID, source module, entity links, revision references, media type and provenance.
12. Define the boundary between Library-owned canonical reference media and customer/order/production assets owned by operational domains.

### Dependencies
- `forprint_contract_registry`

Human control surfaces: `DEVELOPER_AUDIT, ADMIN_FACING`
Module value test: `KEEP`

## forprint_contract_registry

Priority: `P0`
Inventory state: `DIRECTION_CLEAR_FOUNDATION_PENDING`
Role: Versioned inter-module contract lifecycle registry

### AGREED / RECOVERED
- Contract manifests/revisions/compatibility/adoption; first pilot Calculator Job Specification -> OCR.

### SYNTHETIC / PROPOSED
- Generated projections, migration/deprecation automation and compatibility view after proven pilots.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_system_blueprint`
- `forprint_project_inspector`

Human control surfaces: `DEVELOPER_AUDIT, ADMIN_FACING`
Module value test: `KEEP`

## forprint_project_inspector

Priority: `P0`
Inventory state: `STRONG_DIRECTION`
Role: Read-only structural/semantic/conformance verification

### AGREED / RECOVERED
- Detects drift/contradictions/ownership violations; never invents domain truth.

### SYNTHETIC / PROPOSED
- Self-inventory health, duplicate-capability detection, UI conformance, bounded semantic review.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_system_blueprint`

Human control surfaces: `DEVELOPER_AUDIT, ADMIN_FACING`
Module value test: `KEEP`

## forprint_identity_access_service

Priority: `P0`
Inventory state: `CONFIRMED_NEW_MODULE_NOT_IMPLEMENTED`
Role: Shared identity/authentication/authorization/access service

### AGREED / RECOVERED
- One shared identity/access capability; roles + user overrides; deny-by-default cross-client access.

### SYNTHETIC / PROPOSED
- Sessions/devices/recovery/MFA/passkeys/SSO/admin access-review.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_operations_control_registry`
- `forprint_system_administration`

Human control surfaces: `USER_FACING, ADMIN_FACING`
Module value test: `KEEP`

## forprint_operations_control_registry

Priority: `P0`
Inventory state: `FOUNDATION_EXISTS_DEEP_REVIEW_REQUIRED`
Role: Canonical operational party/order/task/control registry and write boundary

### AGREED / RECOVERED
- Operational orders/requests/events/tasks/blockers and stable shared party/order IDs.

- Operations Control Registry remains authoritative for operational order/job identity, Job Ticket revision and production lifecycle state referenced by historical assets.
- Historical asset revision-family projections must derive operational status from explicit order/job/revision evidence rather than filenames or search inference.

- The first durable Process Manager capability is hosted inside Operations Control Registry because this module already owns the canonical operational state and write boundary for orders, tasks, blockers, incidents, deadlines and cross-module execution context.
- Hosted Process Manager state is a distinct capability namespace: it owns durable process instances, current step, waiting conditions, expected events, timers, deadlines, retry state, escalation state and transitions without absorbing foreign domain truth.
- The hosted capability must remain extraction-ready through explicit contracts, its own state model, adapters, tests and minimal imports from the Operations Control Registry host.

- Treat the current Operations Control Registry worktree as present implementation evidence while preserving historical Operational Registry identifiers in immutable provenance; repository/path cleanup remains separately authorized.
- Reconcile the persistent ClientRecord/OrderRecord core with richer ClientAccount/OperationalOrder foundations before promoting either richer generation to canonical runtime truth; make the chosen migration or decomposition boundary explicit.
- Separate business-partner/person/organization/customer/billing/delivery ownership and order/workflow/process/production/payment-fact/dictionary status axes before expanding canonical machine ownership.
- After the project interaction-role taxonomy is settled, reconcile accepted Accounting/Warehouse/Logistics/Prepress inbound facts and references plus Operations command/query boundaries without letting transport or message direction create semantic ownership.

### SYNTHETIC / PROPOSED
- Mature operational lifecycle, Job Ticket state, reservations/obligations and resilient commands/events.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.
11. Define the operational historical-asset link contract connecting asset references to order ID, job ID, revision and authoritative operational state.
12. Define explicit current/superseded/production-result and approval-related revision evidence required by historical asset consumers.
13. Expose operational revision/status projections for historical retrieval without transferring operational truth into the search/index layer.
14. Define the hosted Process Manager namespace and durable process-instance identity/state model inside Operations Control Registry.
15. Define current-step, waiting-condition, expected-event, timer, deadline, retry, escalation and transition semantics for long-running processes.
16. Define an append-only process transition/event ledger with correlation, idempotency, restart recovery and deterministic resume semantics.
17. Define operator-attention and authorized human-decision integration without letting unattended workflow state silently authorize foreign-domain actions.
18. Define domain adapters so CRM, Telegram, Logistics and other modules can observe or participate through typed process intents/events without owning the durable process instance.
19. Add explicit extraction-readiness criteria so the capability can later move to a standalone Process Manager service if scale, topology or ownership evidence justifies separation.

### Dependencies
- `calculator_engine`
- `forprint_contract_registry`
- `forprint_library`

Human control surfaces: `OPERATOR_FACING, ADMIN_FACING`
Module value test: `KEEP`

## forprint_accounting_registry_service

Priority: `P0`
Inventory state: `OWNER_DIRECTION_CLEAR_DECOMPOSITION_REQUIRED`
Role: Operational/commercial accounting registry and 1C compatibility boundary

### AGREED / RECOVERED
- Invoices/payments/accounting documents/reconciliation/1C staging; supplier-document automation.

### SYNTHETIC / PROPOSED
- Management accounting, settlements, safe conditional mandates and mature 1C exchange.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_operations_control_registry`
- `forprint_library`
- `warehouse_service`
- `calculator_engine`

Human control surfaces: `OPERATOR_FACING, ADMIN_FACING`
Module value test: `KEEP`

## warehouse_service

Priority: `P1`
Inventory state: `DEEP_REVIEW_REQUIRED`
Role: Physical inventory/material-location truth and movement service

### AGREED / RECOVERED
- Physical stock fact distinct from accounting valuation and Calculator planned need.

### SYNTHETIC / PROPOSED
- Reservations, receipts/issues/writeoffs, locations, shortages, cycle count, traceable reprint consumption.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_library`
- `forprint_operations_control_registry`
- `forprint_accounting_registry_service`

Human control surfaces: `OPERATOR_FACING, ADMIN_FACING`
Module value test: `KEEP`

## forprint_prepress_hub

Priority: `P1`
Inventory state: `FIRST_PASS_DIRECTION_RECORDED`
Role: Prepress/file preparation and production-readiness evidence

### AGREED / RECOVERED
- PDF/document probe and readiness evidence consuming Calculator + Library.

- Prepress contributes deterministic technical asset facts and derived preview evidence for historical indexing without owning customer/order history or search-result truth.
- Technical asset evidence may include exact file hash, type, size, page count, dimensions, color/resolution facts, preview references and file revision provenance.

### SYNTHETIC / PROPOSED
- Preflight/normalization/imposition/profile/hot-folder and future metadata projections.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.
11. Define a machine-readable technical Asset Fact Packet containing deterministic file facts, source revision, hashes and safe preview references.
12. Define deterministic fingerprint/probe outputs suitable for downstream candidate retrieval while keeping semantic match decisions outside Prepress.
13. Define historical-file provenance and master-versus-derived relationships without making Prepress the raw archive or historical search owner.

### Dependencies
- `calculator_engine`
- `forprint_library`
- `forprint_contract_registry`

Human control surfaces: `OPERATOR_FACING`
Module value test: `KEEP`

## production_runtime_inspector

Priority: `P1`
Inventory state: `DEEP_REVIEW_REQUIRED`
Role: Runtime production actuals/evidence and exact device-used inspection

### AGREED / RECOVERED
- Records concrete device and actuals without silently rewriting approved norms.

### SYNTHETIC / PROPOSED
- Operation actuals, quality/variance signals, telemetry and norm-change proposals.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_operations_control_registry`
- `forprint_system_administration`
- `forprint_library`

Human control surfaces: `OPERATOR_FACING, DEVELOPER_AUDIT`
Module value test: `KEEP`

## forprint_crm

Priority: `P1`
Inventory state: `FIRST_PASS_PLUS_NEW_OWNER_DIRECTION`
Role: Unified human business cockpit, analytics and composite workflow entry point

### AGREED / RECOVERED
- Owner-data aggregation without foreign-data ownership; dashboards/wallboards; composite workflows.

- Customer intelligence is a layered CRM capability with separate Seed Profile, Observed Customer Model and Effective Policy layers; this does not make CRM the canonical client registry or owner of foreign domain truth.
- Seed Profile is a simple manager-selected starting preset for relationship and communication handling and is not inferred authority.
- Observed Customer Model is derived from evidence with provenance, recency, confidence and domain-specific coverage rather than from opaque permanent labels.
- Effective Policy combines approved policy rules with permitted customer-model evidence but must never silently expand commercial, financial or operational authority.
- Customer-specific semantics distinguish baseline, exception, possible shift, probable shift and new baseline using recency weighting, minimum evidence, hysteresis and contextual segmentation.
- Customer relationship health and trajectory are multidimensional projections covering payment health, commercial value, growth momentum, margin quality, service burden, order clarity, dispute risk, relationship stability and strategic potential, with underlying facts retained by their owner modules.
- Customer-model updates combine event-driven evidence with periodic reconciliation; stale, conflicting and insufficient evidence must remain explicit.
- Profile and policy transitions require durable provenance, transition history and auditable human override rather than destructive replacement of prior state.

- CRM is the primary human-facing Process Manager control surface but does not own durable process instances, timers, retries, deadlines or transition truth.

### SYNTHETIC / PROPOSED
- Customer/Supplier 360, universal search, saved role views, activity timeline, exception center.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.
11. Define the CRM customer-intelligence model as separate Seed Profile, Observed Customer Model and Effective Policy layers without absorbing canonical client identity or foreign domain truth.
12. Define manager-selectable Seed Profiles as bootstrap presets with explicit scope, version and provenance.
13. Define the Observed Customer Model with evidence provenance, recency, confidence, domain-specific coverage and safe handling of insufficient evidence.
14. Define Effective Policy composition so approved rules may consume customer-model evidence without silently expanding financial, commercial or operational authority.
15. Implement baseline-to-shift semantics with exception, possible-shift, probable-shift and new-baseline states plus recency weighting, minimum evidence, hysteresis and contextual segmentation.
16. Define multidimensional customer health and trajectory projections using owner-sourced payment, value, growth, margin, service-burden, clarity, dispute, stability and strategic-potential evidence.
17. Define event-driven customer-model updates plus periodic reconciliation, freshness checks and explicit conflict/staleness handling.
18. Define immutable profile/policy transition history, provenance and auditable human override before customer-specific policy automation is considered mature.
19. Define CRM views for active processes, current step, blockers, waiting state, deadlines, escalations and next authorized actions from Process Manager projections.
20. Define structured operator commands for clarification, acknowledgement, override request and authorized intervention without creating shadow workflow state.

### Dependencies
- `forprint_operations_control_registry`
- `calculator_engine`
- `forprint_accounting_registry_service`
- `warehouse_service`
- `logistics_service`
- `forprint_identity_access_service`

Human control surfaces: `OPERATOR_FACING, ADMIN_FACING`
Module value test: `KEEP`

## logistics_service

Priority: `P1`
Inventory state: `IMPLEMENTATION_EXISTS_RUNTIME_SCOPE_GATED`
Role: Provider-neutral shipment/pickup/delivery/tracking truth

### AGREED / RECOVERED
- Provider adapters, shipment drafts/tracking/events; current H10 sole automation pilot.

- Logistics retains authoritative shipment-specific workflow state machines, retries and reconciliation, while broader cross-domain Process Manager state is hosted by Operations Control Registry.

### SYNTHETIC / PROPOSED
- Mature carrier/taxi/courier adapters, evidence handoff, delivery exceptions and bounded automation.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.
11. Define the boundary between Logistics shipment lifecycle state and a parent or linked cross-domain Process Manager instance.
12. Expose typed shipment events, waiting conditions and outcomes to Process Manager without transferring carrier/provider truth out of Logistics.

### Dependencies
- `forprint_operations_control_registry`
- `forprint_accounting_registry_service`
- `forprint_identity_access_service`

Human control surfaces: `OPERATOR_FACING, ADMIN_FACING`
Module value test: `KEEP`

## telegram_bot

Priority: `P1`
Inventory state: `ACTIVE_HISTORY_NEW_EXECUTION_HELD`
Role: Conversational customer/staff channel adapter

### AGREED / RECOVERED
- Structured request/response channel without owning CRM/order/accounting truth.
- Personalized communication orchestration: Telegram preserves dialogue continuity and renders canonical domain facts according to approved customer communication context without changing those facts.
- Structured inbound requests and outbound communication intents are the preferred cross-module communication contract.
- Customer-specific communication context may be consumed by Telegram, while canonical customer profile, commercial policy and customer economics remain outside Telegram ownership.
- Clarification converges toward structured Order Drafts using canonical Library, Calculator and other domain constraints.
- AI remains a replaceable helper after deterministic rules, history, classifiers, customer context and clarification, with human escalation for unresolved ambiguity.
- Historical asset retrieval is consumed through a machine-readable index; Telegram does not own archives, fingerprints or historical asset truth.
- Long-running business processes are external durable process truth; Telegram participates only through communication intents, acknowledgements and clarification.

### SYNTHETIC / PROPOSED
- Voice transcription, supplier enrichment, richer self-service, future TTS/voice.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.
11. Define personalized communication orchestration with conversation continuity, approved communication preferences and strict presentation-versus-facts separation.
12. Define channel-neutral inbound structured domain requests/events and outbound structured communication intents with correlation and provenance.
13. Define consumption of customer-specific communication context without moving canonical customer profile, commercial policy or analytics into Telegram.
14. Define bounded clarification and structured Order Draft interaction using canonical Library/Calculator/domain constraints.
15. Define deterministic-to-context-to-AI-to-human escalation with replaceable model/provider slots and progress/contradiction based escalation.
16. Define Telegram consumption of historical customer asset retrieval results without live archive scanning or asset-index ownership.
17. Define Telegram as a communication participant for durable long-running business processes while process state/timers/deadlines/transitions remain with the eventual canonical Process Manager owner.

### Dependencies
- `calculator_engine`
- `forprint_crm`
- `forprint_identity_access_service`
- `forprint_integration_gateway`

Human control surfaces: `USER_FACING, ADMIN_FACING`
Module value test: `KEEP`

## forprint_operations_assistant

Priority: `P1`
Inventory state: `FIRST_PASS_DIRECTION_RECORDED`
Role: Low-friction shop-floor assistant, guided forms and operational knowledge

### AGREED / RECOVERED
- Procedures/guided forms/Job Ticket assistance/physical observations.

### SYNTHETIC / PROPOSED
- Role-aware training, visual SOPs, reprint/exception capture, bounded operational AI.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_library`
- `forprint_operations_control_registry`
- `forprint_identity_access_service`

Human control surfaces: `OPERATOR_FACING`
Module value test: `KEEP`

## forprint_system_administration

Priority: `P1`
Inventory state: `FIRST_PASS_DIRECTION_RECORDED`
Role: IT/workplace/device/data-platform/secrets administration

### AGREED / RECOVERED
- Workstation/admin surface plus physical PostgreSQL and secrets-platform operations.

### SYNTHETIC / PROPOSED
- Fleet onboarding, device capability inventory, backup/PITR, health and operational-readiness gates.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `cloud_backup_manager`
- `forprint_project_inspector`

Human control surfaces: `ADMIN_FACING, DEVELOPER_AUDIT`
Module value test: `KEEP`

## forprint_integration_gateway

Priority: `P2`
Inventory state: `PAUSED_UNTIL_RUNTIME_NEED`
Role: Runtime transport validation/routing/idempotency/correlation boundary

### AGREED / RECOVERED
- Routes/validates ACTIVE contracts without business ownership.

- Gateway delivery state, retry, queue and dead-letter handling remain transport mechanics and must not become durable business Process Manager state.

### SYNTHETIC / PROPOSED
- Delivery ledger, observability and scalable routing when runtime need justifies activation.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.
11. Define transport correlation between Gateway delivery attempts and Process Manager process/event identities without merging their state machines.
12. Keep Gateway retry/dead-letter decisions transport-scoped while business waiting, deadline and escalation truth remains in the hosted Process Manager capability.

### Dependencies
- `forprint_contract_registry`
- `forprint_operations_control_registry`

Human control surfaces: `DEVELOPER_AUDIT, ADMIN_FACING`
Module value test: `KEEP`

## website

Priority: `P2`
Inventory state: `FIRST_PASS_DIRECTION_RECORDED`
Role: Customer web channel using shared Calculator/Identity/domain contracts

### AGREED / RECOVERED
- Must not duplicate Calculator/catalog/order truth; legacy surface needs controlled reconciliation.

### SYNTHETIC / PROPOSED
- Modern self-service, account/order/calculation/files/payment/delivery views.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `calculator_engine`
- `forprint_identity_access_service`
- `forprint_library`
- `forprint_operations_control_registry`

Human control surfaces: `USER_FACING`
Module value test: `KEEP`

## mobile_app

Priority: `P2`
Inventory state: `DEFERRED`
Role: Future mobile customer/staff channel

### AGREED / RECOVERED
- Deferred until Calculator/Identity/API contracts mature.

### SYNTHETIC / PROPOSED
- Secure mobile self-service over the same domain contracts as web.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `calculator_engine`
- `forprint_identity_access_service`
- `forprint_integration_gateway`

Human control surfaces: `USER_FACING`
Module value test: `KEEP`

## forprint_marketing_orchestrator

Priority: `P3`
Inventory state: `NON_BLOCKING_FUTURE`
Role: Marketing campaign/content orchestration

### AGREED / RECOVERED
- Campaign/content planning and human-reviewed publication without becoming CRM.

### SYNTHETIC / PROPOSED
- Multi-channel automation, AI creative routing, cost/performance learning and lead handoff.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_crm`
- `website`
- `forprint_library`
- `forprint_accounting_registry_service`

Human control surfaces: `OPERATOR_FACING, ADMIN_FACING`
Module value test: `KEEP`

## forprint_strategic_control_plane

Priority: `P3`
Inventory state: `NON_BLOCKING_FUTURE`
Role: Strategic priority/status/decision-support layer

### AGREED / RECOVERED
- Tracks goals/priorities and challenges stale direction without overriding Blueprint/operator.

### SYNTHETIC / PROPOSED
- Scenario analysis, strategic KPI aggregation and advisory loops.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_system_blueprint`

Human control surfaces: `ADMIN_FACING, DEVELOPER_AUDIT`
Module value test: `KEEP`

## cloud_backup_manager

Priority: `SUPPORT`
Inventory state: `IMPLEMENTED_SUPPORT_MODULE`
Role: Infrastructure backup utility/reference UI shell

### AGREED / RECOVERED
- Backup/health support; UI reference shell candidate.

### SYNTHETIC / PROPOSED
- Possible absorption into System Administration if lifecycle evidence justifies it.

### Full horizon
1. Reconcile current implementation/evidence and stale documentation.
2. Close charter, ownership boundaries and mature target state.
3. Build/repair capability catalog and module self-inventory surfaces.
4. Define canonical data/contracts/dependency timing.
5. Harden deterministic core with fixtures/tests.
6. Add early role-appropriate Human Control Surface where useful.
7. Integrate only through accepted producer/consumer contracts.
8. Add observability, exception handling, recovery and audit evidence.
9. Pilot bounded automation only under explicit authority and measure variance/cost/quality.
10. Reach mature target, document migration/retirement paths and continue measured optimization.

### Dependencies
- `forprint_system_administration`

Human control surfaces: `ADMIN_FACING`
Module value test: `REVIEW_MERGE_LATER`

## Proposed/noncanonical

- `forprint_semantic_retrieval_service`: preserve proposal/Human Intent, but require explicit value review before canonical promotion.

## verification_lab

- Strategic priority: `P0`
- Role: Independent verification, adversarial testing, fault-injection and deterministic regression evidence module.
- Inventory state: `CONFIRMED_NEW_MODULE_NOT_IMPLEMENTED`
- Implementation eligible now: `false`
- Portfolio gate: `HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE`
- Module value test: `KEEP`

### AGREED / RECOVERED

- Detects drift/contradictions/ownership violations; never invents domain truth.
- Verification Lab is a distinct canonical module that intentionally tries to prove the system wrong before customers or incidents do.

### SYNTHETIC / PROPOSED

- Self-inventory health, duplicate-capability detection, UI conformance, bounded semantic review.
- Mature Verification Lab should support black/gray/white-box Test Plane campaigns, adversarial/fault/concurrency testing, deterministic regression and release-gate evidence with synthetic side effects only.

### Full horizon

1. Establish Verification Lab canonical identity, charter and strict separation from Project Inspector and Runtime Inspector.
2. Define BLACK_BOX, GRAY_BOX and WHITE_BOX read-only diagnostic modes and their evidence boundaries.
3. Define Test Plane isolation with fake/synthetic payment, courier, printer, email, cloud, Telegram and database side effects.
4. Define normal/invalid/boundary/malformed/combinatorial/multilingual/out-of-domain/auth/data-isolation test taxonomy.
5. Define prompt-adversarial, tool-misuse, state-machine, concurrency, idempotency, stale-cache and schema-fuzz campaigns.
6. Define fault/recovery, timeout, unavailable-resource, retry/dead-letter, load/performance and cost-regression campaigns.
7. Convert useful AI-discovered failures into owner-confirmed deterministic regression corpus rather than permanent stochastic-only tests.
8. Define change-triggered, nightly, weekly, manual, pre-release and post-release verification campaign policy.
9. Define trace-aware evaluation of intermediate contract/tool/state behavior, not only final user-visible answer.
10. Remain planning-only until Test Plane, Execution Policy Gate, IAM and explicit operator distribution/implementation approval are ready.

### Dependencies

- `forprint_system_blueprint`
- `forprint_contract_registry`
- `forprint_project_inspector`
- `forprint_system_administration`

### Human control surfaces

- `DEVELOPER_AUDIT`
- `ADMIN_FACING`

<!-- FORPRINT_U92_U107_CANONICAL_INTEGRATION_20260903:START -->
## 2026-09-03 u92/u107 architecture integration

Canonical module count after approved planning promotion: **23**.

New canonical module: `verification_lab`.

`forprint_semantic_retrieval_service` remains proposed/noncanonical.

Roadmap/governance narrative:
`coordination/internal_work/blueprint/evening_reviews/2026-09-03/2026-09-03__u92_architecture_governance_integration_v0_1.md`

This planning integration does **not** authorize module implementation, assistant distribution,
prompt activation, H10 widening, automatic acceptance/release, or cross-repository diagnostics.
<!-- FORPRINT_U92_U107_CANONICAL_INTEGRATION_20260903:END -->
```

### BLUEPRINT CONTEXT â€” coordination/roadmaps/details/forprint_system_blueprint/portfolio_full_horizon_target_states_v0_1.yaml

`SHA256=cbfca4b97c739e9b13ec1ed31afd7d32834923a87d8caa756eb4c1355fc50486`

```yaml
schema_version: forprint_portfolio_full_horizon_target_states_v0_1
date: '2026-09-01'
status: PROPOSED_PORTFOLIO_BASELINE_REQUIRES_OWNER_REVIEW
authority: planning_projection_not_release_authority
global_execution_gate:
  ordinary_module_implementation_allowed: false
  requirements_before_resume:
    - full-horizon roadmaps sufficiently reconciled
    - mature target states sufficiently meaningful
    - module self-inventory/self-indexing baseline
    - dependency/readiness/priority dashboard
  assistant_distribution_allowed: false
  assistant_distribution_resume_requirements:
    - portfolio analysis and semantic reconciliation complete
    - module-specific roadmaps and mature targets reviewed
    - dependency/readiness/priority balance reviewed
    - open semantic conflicts dispositioned
    - explicit operator approval to distribute work
    - cleanliness-conformance state and local cleanliness-pack roadmap recorded for every canonical module
    - AI Execution Safety & Runtime Governance gate reviewed and configured for future assistant/runtime execution
  project_cleanliness_conformance_required: true
  project_cleanliness_policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
  blueprint_cleanliness_automation_status: IMPLEMENTED
  cross_repository_cleanliness_automation_status: PLANNED_NOT_IMPLEMENTED
  ai_execution_safety_runtime_governance_required: true
  ai_execution_safety_runtime_governance_state: PLANNING_REQUIRED_NOT_IMPLEMENTED
  ai_execution_safety_runtime_governance_ref: coordination/roadmaps/details/forprint_system_blueprint/ai_execution_safety_runtime_governance_gate_v0_1.md
modules:
  forprint_system_blueprint:
    strategic_priority: P0
    role: Portfolio architecture, ownership, governance, roadmap/dependency balancing and release/distribution gate authority.
    target_state:
      agreed_or_recovered:
        - Global architecture, boundaries, standards, Human Intent, dependency/readiness balance.
        - Blueprint must formalize managed autonomy, Verification Lab, development/runtime separation and a common module maturity path before future distribution.
        - >-
          Historical Asset Index is accepted as real portfolio work, implemented as a projection over domain-owned asset, technical and operational evidence rather than as a new competing source of truth.
        - >-
          The retrieval host remains an explicit architecture decision; the existing Semantic Retrieval candidate must not be promoted automatically merely because historical indexing is required.
        - >-
          The working portfolio host for the first durable Process Manager capability is Operations Control Registry; no standalone Process Manager module is created initially.
        - >-
          Process Manager is deliberately designed as a hosted-but-extractable capability, so later separation requires evidence rather than an early architectural guess.
      synthetic_or_proposed:
        - Stronger automated portfolio health/decision-support projections.
        - Mature Blueprint should reduce human control to a small number of portfolio/exception/approval surfaces while preserving explicit high-impact authority.
    full_horizon_steps:
      - Integrate u92 architecture decisions into Human Intent, canonical portfolio roadmaps and governance without opening implementation.
      - Promote Verification Lab to canonical module identity while Semantic Retrieval remains proposed/noncanonical.
      - Formalize DEV → VERIFICATION → RELEASE → RUNTIME separation and immutable-runtime/self-evolution rules.
      - Formalize M0-M9 module maturity and production-entry sequence for all future modules.
      - Formalize shared resource concurrency/availability states, retry/backpressure/dead-letter semantics.
      - Formalize Execution Policy Gate, capability-shaped tools and risk-class authorization.
      - Formalize managed-autonomy levels, context checkpoint/handoff and AI budget-runway evidence.
      - Strengthen dependency-constrained readiness and assistant-distribution prerequisites using the 23-module canonical set.
      - Require Verification Lab and Project Inspector evidence before production promotion while keeping their roles separate.
      - Keep assistant distribution, module implementation, H10 widening and automatic acceptance closed until explicit operator approval.
      - >-
        Define the cross-module Historical Asset Index contract over Library reference semantics, Prepress technical asset facts and Operations Control Registry order/job/revision state.
      - >-
        Define candidate retrieval stages as cheap scoped retrieval followed by deeper comparison of a small candidate set and explicit human/customer selection when ambiguity remains.
      - >-
        Resolve the final hosted-capability location only after comparing an existing-host implementation with the noncanonical Semantic Retrieval module candidate.
      - >-
        Govern the hosted Process Manager boundary so process truth, domain truth, transport state and human-facing workflow UI remain explicitly separated.
      - >-
        Review extraction triggers after real usage evidence, including independent scaling, availability, topology, ownership pressure and cross-domain coupling.
    dependencies_or_inputs:
      - forprint_project_inspector
      - forprint_contract_registry
      - verification_lab
    human_control_surfaces:
      - DEVELOPER_AUDIT
      - ADMIN_FACING
    inventory_state: STRONG_EXISTING_FOUNDATION
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  calculator_engine:
    strategic_priority: P0
    role: Canonical production calculation, quote-item semantics and production-filename interpretation engine.
    target_state:
      agreed_or_recovered:
        - Calculation/quote/order drafts, price/material/time estimates, early visual configuration, exact reference set recovered.
        - Calculator owns calculated quote/item semantics and production filename interpretation, not the whole customer basket or order.
      synthetic_or_proposed:
        - Reusable constructor family, outsourcing decisions and partner-adapter integration.
        - Mature Calculator should expose deterministic contracts, offline estimate rules with revalidation and Verification Lab regression surfaces.
    full_horizon_steps:
      - Preserve Calculator ownership of calculation, quote-item and production-filename semantics.
      - Keep Library as vocabulary/profile source and avoid local shadow aliases/defaults.
      - Separate calculated item/quote from CRM basket/checkout and OCR canonical operational order state.
      - Define stable request/result contracts with provenance, assumptions and deterministic rounding rules.
      - Define offline estimate behavior where allowed and mandatory server/current-norm revalidation before commitment.
      - Define deterministic filename correction only for unambiguous cases and retain source/provenance.
      - Define Prepress capability/probe handoff without Calculator owning file-repair execution.
      - Provide deterministic fixtures and boundary cases to Verification Lab for regression.
      - Use Runtime Inspector actuals only as proposal evidence for norm changes, never silent rewrite.
      - Hold broader automation until Library/Contract Registry/consumer adoption evidence is portfolio-ready.
    dependencies_or_inputs:
      - forprint_library
      - forprint_prepress_hub
    human_control_surfaces:
      - USER_FACING
      - OPERATOR_FACING
      - ADMIN_FACING
    inventory_state: OWNER_DIRECTION_CLEAR_DEEP_INVENTORY_REQUIRED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_library:
    strategic_priority: P0
    role: Canonical semantic/catalog/reference and shared UI publication authority
    target_state:
      agreed_or_recovered:
        - Canonical products/materials/services/operations/aliases/profiles; shared UI package publication.
        - >-
          Historical/reference asset semantics use stable asset and revision references; Library may own canonical reference-media metadata where applicable, while customer/order/production truth remains with its domain owners.
        - >-
          Historical Asset Index entries are projections over authoritative sources; an index/search result never becomes canonical asset, order or production truth.
      synthetic_or_proposed:
        - Fast capability/semantic discovery and mature version/adoption lifecycle.
    full_horizon_steps:
      - Reconcile current Library catalog, alias, template, naming-profile and UI publication evidence.
      - Confirm Library ownership of product/material/service/operation semantics and shared UI publication, excluding business workflows.
      - Complete capability/self-inventory for canonical IDs, aliases, misspellings, production tokens, templates and technical cards.
      - Define versioned naming/profile/default semantics consumed by Calculator, Prepress and operations surfaces.
      - Define material/product/service canonical identifiers and stable lookup contracts for Warehouse and other consumers.
      - 'Define UI design-system package lifecycle: lookup, proposal, prototype, Inspector review, operator approval, publish and adoption.'
      - Add version/adoption metadata and compatibility rules without creating live global CSS or uncontrolled defaults.
      - Plan fast capability/semantic discovery while keeping retrieval candidate-only and domain-owner truth authoritative.
      - Define deprecation/migration paths for legacy aliases/profiles and evidence requirements for consumer adoption.
      - Hold broader implementation until Contract Registry and consumer readiness are reconciled in the portfolio.
      - >-
        Define stable historical/reference asset metadata semantics including asset ID, source module, entity links, revision references, media type and provenance.
      - >-
        Define the boundary between Library-owned canonical reference media and customer/order/production assets owned by operational domains.
    dependencies_or_inputs:
      - forprint_contract_registry
    human_control_surfaces:
      - DEVELOPER_AUDIT
      - ADMIN_FACING
    inventory_state: OWNER_DIRECTION_CLEAR
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_contract_registry:
    strategic_priority: P0
    role: Versioned inter-module contract lifecycle registry
    target_state:
      agreed_or_recovered:
        - Contract manifests/revisions/compatibility/adoption; first pilot Calculator Job Specification -> OCR.
      synthetic_or_proposed:
        - Generated projections, migration/deprecation automation and compatibility view after proven pilots.
    full_horizon_steps:
      - Reconcile existing contract concepts, manifests, lifecycle states and governance references.
      - Confirm Contract Registry as lifecycle/compatibility authority, not business semantics or runtime routing authority.
      - Complete self-inventory for contract IDs, revisions, producer/consumer registration, fixtures and compatibility evidence.
      - Finalize lifecycle states and the rule that breaking revisions cannot become ACTIVE before mandatory consumers support them.
      - Use Calculator Job Specification to OCR/Prepress as the first full contract-lifecycle planning pilot.
      - Define adoption matrix, compatibility checks, migration metadata and Inspector evidence expectations.
      - Define deprecation, supported-legacy, revoked and retired handling with explicit operator/governance boundaries.
      - Plan generated read-only contract catalogs and projections without creating a second semantic source of truth.
      - Define Integration Gateway consumption of ACTIVE contracts only and prevent unilateral activation by producers or consumers.
      - Hold runtime activation until pilot evidence and portfolio dependency gates are explicitly approved.
    dependencies_or_inputs:
      - forprint_system_blueprint
      - forprint_project_inspector
    human_control_surfaces:
      - DEVELOPER_AUDIT
      - ADMIN_FACING
    inventory_state: DIRECTION_CLEAR_FOUNDATION_PENDING
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_project_inspector:
    strategic_priority: P0
    role: Read-only structural, semantic, cleanliness, architecture and governance conformance verification.
    target_state:
      agreed_or_recovered:
        - Detects drift/contradictions/ownership violations; never invents domain truth.
        - Project Inspector detects drift/conflicts/duplication candidates but never invents or activates domain truth.
      synthetic_or_proposed:
        - Self-inventory health, duplicate-capability detection, UI conformance, bounded semantic review.
        - Mature Inspector should verify dev/runtime boundary, module maturity, autonomy evidence and intake Verification Lab findings as conformance evidence.
    full_horizon_steps:
      - Reconcile Project Inspector scope against Blueprint, Runtime Inspector and Verification Lab.
      - Confirm Inspector is read-only conformance authority and not an adversarial test executor or domain owner.
      - 'Define deterministic checks first: schema, generators, indexes, ownership, cleanliness and contract adoption.'
      - Define duplicate/equivalent-capability candidate detection with owner-reviewed dispositions and no auto-delete.
      - Define module current-state, roadmap, maturity M0-M9 and dependency-constrained readiness conformance.
      - Define DEV/VERIFICATION/RELEASE/RUNTIME separation and immutable-runtime conformance checks.
      - Define bounded semantic review after deterministic evidence with stable finding taxonomy.
      - Define periodic/risk-triggered review and checkpoint-to-commit evidence packages.
      - Ingest Verification Lab results as evidence while leaving intentional test generation to Verification Lab.
      - Keep foreign-repo mutation, truth activation and autonomous deletion forbidden.
    dependencies_or_inputs:
      - forprint_system_blueprint
      - forprint_contract_registry
    human_control_surfaces:
      - DEVELOPER_AUDIT
      - ADMIN_FACING
    inventory_state: STRONG_DIRECTION
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_identity_access_service:
    strategic_priority: P0
    role: Shared identity/authentication/authorization/access service
    target_state:
      agreed_or_recovered:
        - One shared identity/access capability; roles + user overrides; deny-by-default cross-client access.
      synthetic_or_proposed:
        - Sessions/devices/recovery/MFA/passkeys/SSO/admin access-review.
    full_horizon_steps:
      - Reconcile the new IAM concept against current module identity, CRM business-person and SysAdmin security boundaries.
      - Confirm ownership of technical accounts/auth/session/authorization while CRM retains business person/customer relationships.
      - Complete self-inventory for account IDs, sessions, devices, roles, permissions, overrides, recovery and audit.
      - Define account_id to CRM person_id linkage and separate selected business context from authenticated technical identity.
      - Define deny-by-default authorization, role baselines and per-user overrides with auditable access decisions.
      - Plan modern password hashing, MFA/passkeys, recovery and device/session controls.
      - Define SSO/shared-client boundary for web, mobile, Telegram/admin clients without duplicating business context.
      - Separate external partner credentials into centralized SysAdmin secrets infrastructure with least privilege and rotation.
      - Define admin access-review UI, security audit evidence and revocation/recovery procedures.
      - Keep module unimplemented until portfolio roadmap, SysAdmin and operational dependencies are approved.
    dependencies_or_inputs:
      - forprint_operations_control_registry
      - forprint_system_administration
    human_control_surfaces:
      - USER_FACING
      - ADMIN_FACING
    inventory_state: CONFIRMED_NEW_MODULE_NOT_IMPLEMENTED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_operations_control_registry:
    strategic_priority: P0
    role: Canonical operational party/order/task/control registry and write boundary
    target_state:
      agreed_or_recovered:
        - Operational orders/requests/events/tasks/blockers and stable shared party/order IDs.
        - >-
          Operations Control Registry remains authoritative for operational order/job identity, Job Ticket revision and production lifecycle state referenced by historical assets.
        - >-
          Historical asset revision-family projections must derive operational status from explicit order/job/revision evidence rather than filenames or search inference.
        - >-
          The first durable Process Manager capability is hosted inside Operations Control Registry because this module already owns the canonical operational state and write boundary for orders, tasks, blockers, incidents, deadlines and cross-module execution context.
        - >-
          Hosted Process Manager state is a distinct capability namespace: it owns durable process instances, current step, waiting conditions, expected events, timers, deadlines, retry state, escalation state and transitions without absorbing foreign domain truth.
        - >-
          The hosted capability must remain extraction-ready through explicit contracts, its own state model, adapters, tests and minimal imports from the Operations Control Registry host.
        - "Treat the current Operations Control Registry worktree as present implementation evidence while preserving historical Operational Registry identifiers in immutable provenance; repository/path cleanup remains separately authorized."
        - "Reconcile the persistent ClientRecord/OrderRecord core with richer ClientAccount/OperationalOrder foundations before promoting either richer generation to canonical runtime truth; make the chosen migration or decomposition boundary explicit."
        - "Separate business-partner/person/organization/customer/billing/delivery ownership and order/workflow/process/production/payment-fact/dictionary status axes before expanding canonical machine ownership."
        - "After the project interaction-role taxonomy is settled, reconcile accepted Accounting/Warehouse/Logistics/Prepress inbound facts and references plus Operations command/query boundaries without letting transport or message direction create semantic ownership."
      synthetic_or_proposed:
        - Mature operational lifecycle, Job Ticket state, reservations/obligations and resilient commands/events.
    full_horizon_steps:
      - Reconcile operational order/request/task/event/party concepts and historical aliases.
      - Confirm stable operational identities and authorized write boundary without absorbing foreign domain semantics.
      - Complete self-inventory for business partner references, order IDs, requests, tasks, blockers, incidents and deadlines.
      - Define operational order/Job Ticket lifecycle and explicit HOLD, priority, proof, reprint and exception states.
      - Define obligations, reservations, shortages and execution context contracts with Warehouse, Accounting and Logistics.
      - Define command/query boundaries plus outbox/inbox/idempotency/correlation rules for resilient cross-module interactions.
      - Separate communicator, customer, billing and organization context while preserving historical relationships.
      - Define read/write interfaces used by CRM and channels without transferring ownership of operational truth.
      - Plan reporting projections and exception/event evidence for dashboards without making read models authoritative.
      - Hold expanded execution until Calculator/Library/Contract Registry producer dependencies and portfolio gates are ready.
      - >-
        Define the operational historical-asset link contract connecting asset references to order ID, job ID, revision and authoritative operational state.
      - >-
        Define explicit current/superseded/production-result and approval-related revision evidence required by historical asset consumers.
      - >-
        Expose operational revision/status projections for historical retrieval without transferring operational truth into the search/index layer.
      - >-
        Define the hosted Process Manager namespace and durable process-instance identity/state model inside Operations Control Registry.
      - >-
        Define current-step, waiting-condition, expected-event, timer, deadline, retry, escalation and transition semantics for long-running processes.
      - >-
        Define an append-only process transition/event ledger with correlation, idempotency, restart recovery and deterministic resume semantics.
      - >-
        Define operator-attention and authorized human-decision integration without letting unattended workflow state silently authorize foreign-domain actions.
      - >-
        Define domain adapters so CRM, Telegram, Logistics and other modules can observe or participate through typed process intents/events without owning the durable process instance.
      - >-
        Add explicit extraction-readiness criteria so the capability can later move to a standalone Process Manager service if scale, topology or ownership evidence justifies separation.
    dependencies_or_inputs:
      - calculator_engine
      - forprint_contract_registry
      - forprint_library
    human_control_surfaces:
      - OPERATOR_FACING
      - ADMIN_FACING
    inventory_state: FOUNDATION_EXISTS_DEEP_REVIEW_REQUIRED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_accounting_registry_service:
    strategic_priority: P0
    role: Operational/commercial accounting registry and 1C compatibility boundary
    target_state:
      agreed_or_recovered:
        - Invoices/payments/accounting documents/reconciliation/1C staging; supplier-document automation.
      synthetic_or_proposed:
        - Management accounting, settlements, safe conditional mandates and mature 1C exchange.
    full_horizon_steps:
      - Reconcile current accounting registry, 1C staging, document and supplier-automation evidence.
      - Confirm accounting ownership of accounting references/documents/reconciliation while excluding operational order and catalog truth.
      - Complete self-inventory for 1C snapshots, mappings, import/export/reconciliation jobs and accounting documents.
      - Define billing/customer/responsibility contexts and prevent proof/sample classifications from implying payment semantics.
      - Define rounding, totals, taxes/fees and reconciliation boundaries so accounting never silently changes Calculator semantics.
      - Plan supplier-document parsing into reviewable staging rather than direct authoritative posting.
      - Define payment/reconciliation views and safe conditional mandates with explicit approval and audit boundaries.
      - Define management-accounting and settlement projections while preserving operational/accounting truth separation.
      - Plan mature 1C exchange, failure recovery and evidence without allowing 1C compatibility to dominate internal architecture.
      - Hold automation expansion until operational, warehouse, calculator and identity dependencies are contractually ready.
    dependencies_or_inputs:
      - forprint_operations_control_registry
      - forprint_library
      - warehouse_service
      - calculator_engine
    human_control_surfaces:
      - OPERATOR_FACING
      - ADMIN_FACING
    inventory_state: OWNER_DIRECTION_CLEAR_DECOMPOSITION_REQUIRED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  warehouse_service:
    strategic_priority: P1
    role: Physical inventory/material-location truth and movement service
    target_state:
      agreed_or_recovered:
        - Physical stock fact distinct from accounting valuation and Calculator planned need.
      synthetic_or_proposed:
        - Reservations, receipts/issues/writeoffs, locations, shortages, cycle count, traceable reprint consumption.
    full_horizon_steps:
      - Reconcile warehouse stock, location, movement, material and defect/reprint evidence.
      - Confirm Warehouse ownership of physical inventory truth distinct from accounting valuation and Calculator planned consumption.
      - Complete self-inventory for stock facts, locations, lots, movements, reservations, shortages and counts.
      - Bind all stock/material records to Library canonical material IDs and controlled alias resolution.
      - Define receipts, issues, transfers, writeoffs and reservations against stable operational order/job references.
      - Define shortage and availability contracts for Calculator/OCR without letting Warehouse decide pricing or production rules.
      - Define internal-defect/reprint material consumption as traceable physical movements with reason/evidence.
      - Plan cycle counts, discrepancy workflows and audit trails with explicit human resolution.
      - Define Accounting handoff for valuation/documents while retaining physical quantity/location truth.
      - Hold automation until Library, operational registry and accounting contracts are accepted.
    dependencies_or_inputs:
      - forprint_library
      - forprint_operations_control_registry
      - forprint_accounting_registry_service
    human_control_surfaces:
      - OPERATOR_FACING
      - ADMIN_FACING
    inventory_state: DEEP_REVIEW_REQUIRED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_prepress_hub:
    strategic_priority: P1
    role: Prepress/file preparation and production-readiness evidence
    target_state:
      agreed_or_recovered:
        - PDF/document probe and readiness evidence consuming Calculator + Library.
        - >-
          Prepress contributes deterministic technical asset facts and derived preview evidence for historical indexing without owning customer/order history or search-result truth.
        - >-
          Technical asset evidence may include exact file hash, type, size, page count, dimensions, color/resolution facts, preview references and file revision provenance.
      synthetic_or_proposed:
        - Preflight/normalization/imposition/profile/hot-folder and future metadata projections.
    full_horizon_steps:
      - Reconcile current PDF/document probe, readiness and prepress planning evidence.
      - Confirm Prepress ownership of file preparation/readiness evidence, not Calculator logic, catalog truth or device identity.
      - Complete self-inventory for probes, requirements, blockers, corrections, profiles, imposition and production-package outputs.
      - Define consumption of accepted Calculator Job Spec and Library naming/material/profile contracts.
      - Specify deterministic PDF validation/correction boundaries; ambiguous semantic repair must escalate rather than guess.
      - Plan imposition, normalization and production profile selection with explicit evidence and reproducible fixtures.
      - Define hot-folder/station preset policy while concrete device identity/capability remains SysAdmin-owned.
      - Define HOLD/reject/readiness evidence and handoff to operational Job Ticket/QC flows.
      - Plan production-file provenance and future metadata projections without making filenames the source of truth.
      - Hold implementation expansion until Calculator, Library and Contract Registry dependencies are accepted.
      - >-
        Define a machine-readable technical Asset Fact Packet containing deterministic file facts, source revision, hashes and safe preview references.
      - >-
        Define deterministic fingerprint/probe outputs suitable for downstream candidate retrieval while keeping semantic match decisions outside Prepress.
      - >-
        Define historical-file provenance and master-versus-derived relationships without making Prepress the raw archive or historical search owner.
    dependencies_or_inputs:
      - calculator_engine
      - forprint_library
      - forprint_contract_registry
    human_control_surfaces:
      - OPERATOR_FACING
    inventory_state: FIRST_PASS_DIRECTION_RECORDED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  production_runtime_inspector:
    strategic_priority: P1
    role: Runtime execution evidence, actuals, device-used, queue/retry/health and AI/tool-cost telemetry observer.
    target_state:
      agreed_or_recovered:
        - Records concrete device and actuals without silently rewriting approved norms.
        - Runtime Inspector records facts and actuals but never silently rewrites approved norms.
      synthetic_or_proposed:
        - Operation actuals, quality/variance signals, telemetry and norm-change proposals.
        - Mature runtime inspection should trace retries, waiting states, dead letters, AI/tool usage, latency, cost and deployment/canary evidence.
    full_horizon_steps:
      - Reconcile runtime execution, device-used and actuals evidence scope.
      - Confirm Runtime Inspector observes facts but owns neither approved norms nor architecture policy.
      - Define end-to-end request/job trace identifiers across queue, tool, AI and external dependencies.
      - Define WAITING/RETRY/DEGRADED/dead-letter/stuck-work evidence and detection.
      - 'Define AI/tool telemetry: calls, repetitions, tokens, latency, cost, retries and escalation counts.'
      - Define budget-runway and abnormal-cost signals without autonomously changing business strategy.
      - Define actual-vs-standard variance evidence and proposal-only norm-change feedback.
      - Define deployment/shadow/canary runtime evidence consumed by Verification Lab and release decisions.
      - 'Define privacy/retention boundaries: execution evidence, not hidden chain-of-thought capture.'
      - Hold any active control-loop behavior until bounded autonomy and portfolio gates are explicitly approved.
    dependencies_or_inputs:
      - forprint_operations_control_registry
      - forprint_system_administration
      - forprint_library
    human_control_surfaces:
      - OPERATOR_FACING
      - DEVELOPER_AUDIT
    inventory_state: DEEP_REVIEW_REQUIRED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_crm:
    strategic_priority: P1
    role: Business workflow coordinator, Customer Portal composition layer and cross-domain human workspace.
    target_state:
      agreed_or_recovered:
        - Owner-data aggregation without foreign-data ownership; dashboards/wallboards; composite workflows.
        - CRM may compose Customer Portal and basket/checkout workflow while domain-owned semantics remain with their actual owners.
        - >-
          Customer intelligence is a layered CRM capability with separate Seed Profile, Observed Customer Model and Effective Policy layers; this does not make CRM the canonical client registry or owner of foreign domain truth.
        - >-
          Seed Profile is a simple manager-selected starting preset for relationship and communication handling and is not inferred authority.
        - >-
          Observed Customer Model is derived from evidence with provenance, recency, confidence and domain-specific coverage rather than from opaque permanent labels.
        - >-
          Effective Policy combines approved policy rules with permitted customer-model evidence but must never silently expand commercial, financial or operational authority.
        - >-
          Customer-specific semantics distinguish baseline, exception, possible shift, probable shift and new baseline using recency weighting, minimum evidence, hysteresis and contextual segmentation.
        - >-
          Customer relationship health and trajectory are multidimensional projections covering payment health, commercial value, growth momentum, margin quality, service burden, order clarity, dispute risk, relationship stability and strategic potential, with underlying facts retained by their owner modules.
        - >-
          Customer-model updates combine event-driven evidence with periodic reconciliation; stale, conflicting and insufficient evidence must remain explicit.
        - >-
          Profile and policy transitions require durable provenance, transition history and auditable human override rather than destructive replacement of prior state.
        - >-
          CRM is the primary human-facing Process Manager control surface but does not own durable process instances, timers, retries, deadlines or transition truth.
      synthetic_or_proposed:
        - Customer/Supplier 360, universal search, saved role views, activity timeline, exception center.
        - Mature CRM should provide customer/supplier 360, exception/task workspaces, universal search, timeline and cross-domain projections without absorbing foreign truth.
    full_horizon_steps:
      - Reconcile CRM as business coordinator and human workspace rather than physical owner of all ForPrint data.
      - Preserve person/organization/context semantics and phone as strong identifier/search aid, not immutable identity.
      - Define Customer Portal composition with shared IAM and selected business context.
      - Define basket/checkout orchestration around Calculator quote items without creating calculator or accounting truth.
      - Define request/order handoff through Operations Control Registry with stable operational identifiers.
      - Define payment/accounting/logistics/warehouse views through owner-provided projections and explicit provenance.
      - Define Task/Case/Exception Center and role-specific workspaces as CRM-owned workflow composition.
      - Define universal search/timeline/customer-supplier 360 over read models without cross-domain write ownership.
      - Define analytics/variance views while strategic recommendation ownership remains with Strategic Control Plane.
      - Keep cross-domain writes contract-bound and dependency-gated before assistant distribution.
      - >-
        Define the CRM customer-intelligence model as separate Seed Profile, Observed Customer Model and Effective Policy layers without absorbing canonical client identity or foreign domain truth.
      - >-
        Define manager-selectable Seed Profiles as bootstrap presets with explicit scope, version and provenance.
      - >-
        Define the Observed Customer Model with evidence provenance, recency, confidence, domain-specific coverage and safe handling of insufficient evidence.
      - >-
        Define Effective Policy composition so approved rules may consume customer-model evidence without silently expanding financial, commercial or operational authority.
      - >-
        Implement baseline-to-shift semantics with exception, possible-shift, probable-shift and new-baseline states plus recency weighting, minimum evidence, hysteresis and contextual segmentation.
      - >-
        Define multidimensional customer health and trajectory projections using owner-sourced payment, value, growth, margin, service-burden, clarity, dispute, stability and strategic-potential evidence.
      - >-
        Define event-driven customer-model updates plus periodic reconciliation, freshness checks and explicit conflict/staleness handling.
      - >-
        Define immutable profile/policy transition history, provenance and auditable human override before customer-specific policy automation is considered mature.
      - >-
        Define CRM views for active processes, current step, blockers, waiting state, deadlines, escalations and next authorized actions from Process Manager projections.
      - >-
        Define structured operator commands for clarification, acknowledgement, override request and authorized intervention without creating shadow workflow state.
    dependencies_or_inputs:
      - forprint_operations_control_registry
      - forprint_identity_access_service
      - calculator_engine
      - forprint_accounting_registry_service
      - logistics_service
    human_control_surfaces:
      - OPERATOR_FACING
      - ADMIN_FACING
    inventory_state: FIRST_PASS_PLUS_NEW_OWNER_DIRECTION
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  logistics_service:
    strategic_priority: P1
    role: Provider-neutral shipment/pickup/delivery/tracking truth
    target_state:
      agreed_or_recovered:
        - Provider adapters, shipment drafts/tracking/events; current H10 sole automation pilot.
        - >-
          Logistics retains authoritative shipment-specific workflow state machines, retries and reconciliation, while broader cross-domain Process Manager state is hosted by Operations Control Registry.
      synthetic_or_proposed:
        - Mature carrier/taxi/courier adapters, evidence handoff, delivery exceptions and bounded automation.
    full_horizon_steps:
      - Reconcile Logistics provider-neutral shipment/pickup/delivery/tracking model and existing H10 pilot evidence.
      - Confirm Logistics truth boundaries against OCR operational identities, Accounting costs and IAM access.
      - Complete self-inventory for shipment drafts, provider adapters, tracking events, delivery evidence and exceptions.
      - Define stable shipment/order/address references and provider-neutral command/response contracts.
      - Define carrier/taxi/courier adapter boundary, secrets usage, retries, idempotency and correlation.
      - Define pickup/delivery/tracking event lifecycle plus evidence for failures, cancellation and manual takeover.
      - Define cost/charge handoff to Accounting without making Logistics accounting authority.
      - Define delivery exception and escalation workflows with Telegram/operator attention but no hidden auto-decisions.
      - Evaluate the existing Logistics-only H10 automation pilot against cost, quality, retry and operator-intervention evidence.
      - Do not widen H10 or authorize other modules until the pilot and full portfolio are explicitly approved.
      - >-
        Define the boundary between Logistics shipment lifecycle state and a parent or linked cross-domain Process Manager instance.
      - >-
        Expose typed shipment events, waiting conditions and outcomes to Process Manager without transferring carrier/provider truth out of Logistics.
    dependencies_or_inputs:
      - forprint_operations_control_registry
      - forprint_accounting_registry_service
      - forprint_identity_access_service
    human_control_surfaces:
      - OPERATOR_FACING
      - ADMIN_FACING
    inventory_state: IMPLEMENTATION_EXISTS_RUNTIME_SCOPE_GATED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  telegram_bot:
    strategic_priority: P1
    role: Conversational customer/staff channel adapter
    target_state:
      agreed_or_recovered:
        - Structured request/response channel without owning CRM/order/accounting truth.
        - Personalized communication orchestration: Telegram preserves dialogue continuity and renders canonical domain facts according to approved customer communication context without changing those facts.
        - Structured inbound requests and outbound communication intents are the preferred cross-module communication contract.
        - Customer-specific communication context may be consumed by Telegram, while canonical customer profile, commercial policy and customer economics remain outside Telegram ownership.
        - Clarification converges toward structured Order Drafts using canonical Library, Calculator and other domain constraints.
        - AI remains a replaceable helper after deterministic rules, history, classifiers, customer context and clarification, with human escalation for unresolved ambiguity.
        - Historical asset retrieval is consumed through a machine-readable index; Telegram does not own archives, fingerprints or historical asset truth.
        - Long-running business processes are external durable process truth; Telegram participates only through communication intents, acknowledgements and clarification.
      synthetic_or_proposed:
        - Voice transcription, supplier enrichment, richer self-service, future TTS/voice.
    full_horizon_steps:
      - Reconcile current Telegram channel flows, identity/context handling and historical execution evidence.
      - Confirm Telegram as channel adapter only, never canonical CRM/order/calculation/accounting/catalog truth.
      - Complete self-inventory for dialog flow, message UI, uploads, confirmations and channel context.
      - Define authentication/linkage through IAM and visible customer/billing/business context selection.
      - Define structured calculation/order request handoff to Calculator/OCR with audited confirmations.
      - Define file/status/payment/delivery views as domain-owned read projections with clear freshness/provenance.
      - Define context switching without duplicate CRM persons/orders and without phone becoming immutable identity.
      - Plan voice transcription and richer interaction as bounded channel capabilities with fallback and operator visibility.
      - Define retry/idempotency/correlation and anti-loop budgets for channel-to-domain interactions.
      - Hold new execution until IAM, Gateway/contract and portfolio readiness gates are approved.
      - Define personalized communication orchestration with conversation continuity, approved communication preferences and strict presentation-versus-facts separation.
      - Define channel-neutral inbound structured domain requests/events and outbound structured communication intents with correlation and provenance.
      - Define consumption of customer-specific communication context without moving canonical customer profile, commercial policy or analytics into Telegram.
      - Define bounded clarification and structured Order Draft interaction using canonical Library/Calculator/domain constraints.
      - Define deterministic-to-context-to-AI-to-human escalation with replaceable model/provider slots and progress/contradiction based escalation.
      - Define Telegram consumption of historical customer asset retrieval results without live archive scanning or asset-index ownership.
      - Define Telegram as a communication participant for durable long-running business processes while process state/timers/deadlines/transitions remain with the eventual canonical Process Manager owner.
    planning_sources:
      - coordination/internal_work/blueprint/evening_reviews/2026-09-19/forprint_evening_architecture_handoff_20260919_v0_1/02_evening_architecture_summary.md
      - coordination/roadmaps/telegram_bot.yaml
    dependencies_or_inputs:
      - calculator_engine
      - forprint_crm
      - forprint_identity_access_service
      - forprint_integration_gateway
    human_control_surfaces:
      - USER_FACING
      - ADMIN_FACING
    inventory_state: ACTIVE_HISTORY_NEW_EXECUTION_HELD
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_operations_assistant:
    strategic_priority: P1
    role: Low-friction human entry point for guided operational and bounded technical assistance.
    target_state:
      agreed_or_recovered:
        - Procedures/guided forms/Job Ticket assistance/physical observations.
        - Operations Assistant is a human entry surface and may route technical requests to SysAdmin without becoming technical-system authority.
      synthetic_or_proposed:
        - Role-aware training, visual SOPs, reprint/exception capture, bounded operational AI.
        - Mature capability may support voice/mobile/Telegram entry, fuzzy intent resolution, role-aware SOPs and bounded tool invocation.
    full_horizon_steps:
      - Reconcile shop-floor assistant, SOP, guided form, Job Ticket and technical-help entry responsibilities.
      - Confirm Operations Assistant owns interaction context, not operational/order/accounting/technical platform truth.
      - Define role-aware guided forms, SOP discovery and visual instruction flows.
      - Define voice/mobile/Telegram entry as optional interfaces to the same bounded interaction model.
      - Define fuzzy intent/entity resolution with deterministic confirmation before sensitive action.
      - Define routing of technical requests to SysAdmin capabilities and business requests to domain owners.
      - Define IAM-aware capability checks and Execution Policy Gate before any tool side effect.
      - Define low-friction reprint/exception/observation capture with provenance.
      - Define bounded operational AI with repeat/hop/budget/manual-review limits.
      - Keep autonomous high-impact action disabled until Verification Lab and portfolio gates pass.
    dependencies_or_inputs:
      - forprint_library
      - forprint_operations_control_registry
      - forprint_identity_access_service
      - forprint_system_administration
    human_control_surfaces:
      - OPERATOR_FACING
    inventory_state: FIRST_PASS_DIRECTION_RECORDED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_system_administration:
    strategic_priority: P1
    role: Recovery-first technical operations, device, endpoint, data-platform, secrets and offline-continuity administration.
    target_state:
      agreed_or_recovered:
        - Workstation/admin surface plus physical PostgreSQL and secrets-platform operations.
        - SysAdmin is the recovery-first technical operations helper and may integrate with voice/mobile/Telegram through bounded interfaces.
      synthetic_or_proposed:
        - Fleet onboarding, device capability inventory, backup/PITR, health and operational-readiness gates.
        - Mature SysAdmin should manage known-good endpoint state, software/driver lifecycle, recovery artifacts, diagnostics and bounded technical actions with offline continuity.
    full_horizon_steps:
      - Reconcile device, endpoint, PostgreSQL, secrets, backup and recovery responsibilities into one technical-operations boundary.
      - Confirm SysAdmin owns technical platform/device administration but not business workflow or domain semantics.
      - Define stable device inventory, discovery and capability evidence distinct from concrete job assignment.
      - Define known-good workstation/device configuration profiles and drift evidence.
      - Define corporate software/workspace/plugin deployment packs while domain owners retain semantic ownership of business resources.
      - Define stable/pinned driver lifecycle, rollback and compatibility evidence rather than uncontrolled latest-driver upgrades.
      - Define recovery images/snapshots, offline artifact bank and restore procedures with measurable evidence.
      - Integrate Operations Assistant/voice/Telegram as human entry surfaces to bounded SysAdmin capabilities.
      - Define diagnostics and approved-manual troubleshooting with no invented repair procedures or arbitrary shell authority.
      - Hold broad autonomous IT actions until IAM, Execution Policy Gate, Verification Lab and operator approval criteria are satisfied.
    dependencies_or_inputs:
      - cloud_backup_manager
      - forprint_project_inspector
      - forprint_operations_assistant
      - forprint_identity_access_service
    human_control_surfaces:
      - ADMIN_FACING
      - DEVELOPER_AUDIT
    inventory_state: FIRST_PASS_DIRECTION_RECORDED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_integration_gateway:
    strategic_priority: P2
    role: Narrow-waist transport, schema/version routing, idempotency, correlation and delivery-state boundary.
    target_state:
      agreed_or_recovered:
        - Routes/validates ACTIVE contracts without business ownership.
        - Gateway owns transport/contract mechanics, not domain truth or business decisions.
        - >-
          Gateway delivery state, retry, queue and dead-letter handling remain transport mechanics and must not become durable business Process Manager state.
      synthetic_or_proposed:
        - Delivery ledger, observability and scalable routing when runtime need justifies activation.
        - Mature Gateway should expose explicit queue/busy/retry/degraded outcomes, backpressure, deadlines, circuit breaking and dead-letter evidence.
    full_horizon_steps:
      - Reconcile Gateway as narrow-waist transport and contract-validation infrastructure only.
      - Confirm no domain truth, pricing, customer, accounting or workflow-decision ownership.
      - Bind routing to supported Contract Registry revisions and reject unsupported revisions deterministically.
      - Define request envelopes, idempotency keys, correlation/causation and persistent delivery-state ledger semantics.
      - Define shared outcomes OK/QUEUED/BUSY_RETRYABLE/TEMPORARILY_UNAVAILABLE/TIMEOUT/CONFLICT/NOT_FOUND/PERMISSION_DENIED/FAILED_PERMANENT.
      - Define WAITING_RESOURCE/WAITING_EXTERNAL_DEPENDENCY/RETRY_SCHEDULED and distinguish temporary unavailability from not-found.
      - Define bounded retries, exponential backoff, deadlines/TTL, circuit breaker, dead-letter and manual-review escalation.
      - Define backpressure/resource-queue behavior while domain owners retain transactional concurrency decisions.
      - Define observability projections without becoming operational event truth.
      - Remain PAUSED until concrete runtime traffic and portfolio approval demonstrate shared Gateway value.
      - >-
        Define transport correlation between Gateway delivery attempts and Process Manager process/event identities without merging their state machines.
      - >-
        Keep Gateway retry/dead-letter decisions transport-scoped while business waiting, deadline and escalation truth remains in the hosted Process Manager capability.
    dependencies_or_inputs:
      - forprint_contract_registry
      - forprint_operations_control_registry
      - forprint_identity_access_service
    human_control_surfaces:
      - DEVELOPER_AUDIT
      - ADMIN_FACING
    inventory_state: PAUSED_UNTIL_RUNTIME_NEED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  website:
    strategic_priority: P2
    role: Public web presence, SEO entry point and conversion router; not a business-truth owner.
    target_state:
      agreed_or_recovered:
        - Must not duplicate Calculator/catalog/order truth; legacy surface needs controlled reconciliation.
        - Website is the public façade and SEO entry point, not authentication, pricing, payment, cart or canonical order truth.
      synthetic_or_proposed:
        - Modern self-service, account/order/calculation/files/payment/delivery views.
        - Mature public web should maximize organic discovery and route customers into shared Calculator and Customer Portal/domain workflows.
    full_horizon_steps:
      - Reconcile Website strictly as public façade, SEO entry point and service discovery surface.
      - Confirm Website owns no authentication, price truth, payment truth, basket truth or canonical order state.
      - Define explicit routing from public service/product pages into Calculator, design tools and Customer Portal workflows.
      - Define crawl/index hygiene, canonical URLs, sitemap, robots and structured-data rules.
      - Define mobile-first performance and Core Web Vitals targets without duplicating native-app functionality.
      - Define service/product landing semantics from Library/Calculator truth with no local shadow catalog.
      - Define Search Console, analytics, conversion and query-to-order measurement with privacy-aware evidence.
      - Plan content freshness, internal linking and authority-building as governed marketing/website collaboration.
      - Plan organic-query → landing → calculation → customer-workflow optimization with measurable funnel evidence.
      - Keep business logic external and implementation deferred until required shared contracts are portfolio-ready.
    dependencies_or_inputs:
      - calculator_engine
      - forprint_library
      - forprint_crm
    human_control_surfaces:
      - USER_FACING
    inventory_state: FIRST_PASS_DIRECTION_RECORDED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  mobile_app:
    strategic_priority: P2
    role: Deferred native mobile customer/staff channel that reuses shared domain contracts.
    target_state:
      agreed_or_recovered:
        - Deferred until Calculator/Identity/API contracts mature.
        - Native mobile implementation remains paused until customer scale and native-only value justify it.
      synthetic_or_proposed:
        - Secure mobile self-service over the same domain contracts as web.
        - Mature native app may provide fast calculation, orders, push, camera/QR and offline non-authoritative cache over shared APIs.
    full_horizon_steps:
      - Keep Mobile App in PAUSED/PROPOSED planning state and define measurable activation triggers.
      - Use responsive/mobile-first web and shared Customer Portal capabilities as the present customer-mobile baseline.
      - Define future native client as a channel only, with no local domain-truth ownership.
      - Define IAM/session/device security and shared selected business-context behavior before native implementation.
      - Plan fast Calculator and basket/order composition over the same contracts used by web.
      - Define offline cache/estimate behavior as non-authoritative and requiring server revalidation before commitment.
      - Plan push notifications and customer confirmations through audited shared messaging/event contracts.
      - Plan camera, QR and file-upload capabilities without making QR a permission mechanism.
      - Plan unified conversation/history through shared CRM/communication services rather than mobile-only shadow state.
      - Authorize native implementation only after usage, client-base and native-value evidence clears the portfolio gate.
    dependencies_or_inputs:
      - calculator_engine
      - forprint_crm
      - forprint_identity_access_service
      - forprint_library
    human_control_surfaces:
      - USER_FACING
    inventory_state: DEFERRED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_marketing_orchestrator:
    strategic_priority: P3
    role: Brand, campaign and content operations orchestration with human-governed publication.
    target_state:
      agreed_or_recovered:
        - Campaign/content planning and human-reviewed publication without becoming CRM.
        - Marketing Orchestrator is a distinct Brand & Content Operations capability, not merely a post generator and not CRM/customer truth.
      synthetic_or_proposed:
        - Multi-channel automation, AI creative routing, cost/performance learning and lead handoff.
        - Mature capability may orchestrate cross-channel campaigns, AI creative routing, brand-character consistency, reuse, analytics and bounded low-risk auto-publication.
    full_horizon_steps:
      - Reconcile Marketing Orchestrator as brand/content operations distinct from CRM and Website ownership.
      - Confirm product/customer/accounting truth always comes from domain owners.
      - Define brand system, tone, visual rules and Brand Character Bible for persistent mascot/spokescharacter consistency.
      - Define website visual/content audit and handoff with Website/Prepress/Library.
      - Define multi-channel campaign plan, editorial calendar and reusable content asset lifecycle.
      - Define short-form image/video/content generation with provider abstraction, centralized secrets and cost budgets.
      - Define publication maturity DRAFT_ONLY → HUMAN_APPROVAL_REQUIRED → bounded low-risk auto-publish.
      - Define provenance, rollback and audit for all external publication.
      - Define campaign performance learning as advisory proposals and CRM lead/conversion handoff without duplicate customer history.
      - Remain non-blocking/future until core operations mature and operator explicitly approves activation.
    dependencies_or_inputs:
      - forprint_crm
      - website
      - forprint_library
      - forprint_accounting_registry_service
    human_control_surfaces:
      - OPERATOR_FACING
      - ADMIN_FACING
    inventory_state: NON_BLOCKING_FUTURE
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  forprint_strategic_control_plane:
    strategic_priority: P3
    role: Long-horizon business decision intelligence, scenario analysis and strategy-memory plane.
    target_state:
      agreed_or_recovered:
        - Tracks goals/priorities and challenges stale direction without overriding Blueprint/operator.
        - Strategic Control Plane supports long-horizon quantified human decisions rather than acting as an autonomous strategic executor.
      synthetic_or_proposed:
        - Scenario analysis, strategic KPI aggregation and advisory loops.
        - Mature capability should maintain strategic objectives/KPIs, economics/capacity/market intelligence, scenarios, investment cases and forecast→decision→actual memory.
    full_horizon_steps:
      - Reconcile Strategic Control Plane as decision intelligence, not dashboard duplication or operational control.
      - Confirm strategic recommendations remain human decisions and do not directly mutate operational truth.
      - Define strategic objectives registry and structured KPI catalog with provenance.
      - Define product/customer economics, capacity, bottleneck and investment evidence inputs from domain owners.
      - Define external market/search/competitor intelligence as sourced evidence, never invented fact.
      - Define scenario engine with assumptions, uncertainty, risk and sensitivity.
      - Define investment cases and measurable expected return/capacity/quality effects.
      - Define strategy memory linking forecast → recommendation → human decision → actual outcome.
      - Define monthly refresh, quarterly deep review, annual rebaseline and event-triggered recalculation cadence.
      - Keep autonomous execution forbidden; mature output is quantified options and evidence for operator decisions.
    dependencies_or_inputs:
      - forprint_crm
      - forprint_accounting_registry_service
      - forprint_operations_control_registry
      - warehouse_service
      - production_runtime_inspector
    human_control_surfaces:
      - ADMIN_FACING
      - DEVELOPER_AUDIT
    inventory_state: NON_BLOCKING_FUTURE
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  cloud_backup_manager:
    strategic_priority: SUPPORT
    role: Off-site backup, controlled one-way corporate-resource replication and recovery-evidence support service.
    target_state:
      agreed_or_recovered:
        - Backup/health support; UI reference shell candidate.
        - Cloud Backup Manager covers off-site backup, controlled one-way corporate-resource replication and retention/integrity/recovery evidence.
      synthetic_or_proposed:
        - Possible absorption into System Administration if lifecycle evidence justifies it.
        - Mature backup operation should be provider-neutral, encrypted, checksum-verified, restore-tested and resilient to temporary network loss.
    full_horizon_steps:
      - Reconcile implemented backup utility capabilities and exact overlap with SysAdmin platform operations.
      - Confirm Cloud Backup Manager owns backup/replication jobs and recovery evidence, not business data semantics.
      - Define domain-owned prepared-artifact backup inputs with explicit source ownership and provenance.
      - Define one canonical publisher → many consumers replication for approved corporate resources without overwriting user areas.
      - Define retention, versioning/immutability options, encryption, checksum and centralized secret requirements.
      - Define RPO/RTO objectives and periodic restore verification as first-class acceptance evidence.
      - Define provider abstraction, quota/health reporting and safe credential rotation boundaries.
      - Define persistent offline queue/retry so temporary internet loss becomes WAITING/RETRY, never silent loss.
      - Define bandwidth scheduling, retry backoff, alerts and degraded-mode behavior.
      - Reassess KEEP versus merge into SysAdmin only after capability overlap and migration evidence are explicit.
    dependencies_or_inputs:
      - forprint_system_administration
      - forprint_library
    human_control_surfaces:
      - ADMIN_FACING
    inventory_state: IMPLEMENTED_SUPPORT_MODULE
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
  verification_lab:
    strategic_priority: P0
    role: Independent verification, adversarial testing, fault-injection and deterministic regression evidence module.
    target_state:
      agreed_or_recovered:
        - Detects drift/contradictions/ownership violations; never invents domain truth.
        - Verification Lab is a distinct canonical module that intentionally tries to prove the system wrong before customers or incidents do.
      synthetic_or_proposed:
        - Self-inventory health, duplicate-capability detection, UI conformance, bounded semantic review.
        - Mature Verification Lab should support black/gray/white-box Test Plane campaigns, adversarial/fault/concurrency testing, deterministic regression and release-gate evidence with synthetic side effects only.
    full_horizon_steps:
      - Establish Verification Lab canonical identity, charter and strict separation from Project Inspector and Runtime Inspector.
      - Define BLACK_BOX, GRAY_BOX and WHITE_BOX read-only diagnostic modes and their evidence boundaries.
      - Define Test Plane isolation with fake/synthetic payment, courier, printer, email, cloud, Telegram and database side effects.
      - Define normal/invalid/boundary/malformed/combinatorial/multilingual/out-of-domain/auth/data-isolation test taxonomy.
      - Define prompt-adversarial, tool-misuse, state-machine, concurrency, idempotency, stale-cache and schema-fuzz campaigns.
      - Define fault/recovery, timeout, unavailable-resource, retry/dead-letter, load/performance and cost-regression campaigns.
      - Convert useful AI-discovered failures into owner-confirmed deterministic regression corpus rather than permanent stochastic-only tests.
      - Define change-triggered, nightly, weekly, manual, pre-release and post-release verification campaign policy.
      - Define trace-aware evaluation of intermediate contract/tool/state behavior, not only final user-visible answer.
      - Remain planning-only until Test Plane, Execution Policy Gate, IAM and explicit operator distribution/implementation approval are ready.
    dependencies_or_inputs:
      - forprint_system_blueprint
      - forprint_contract_registry
      - forprint_project_inspector
      - forprint_system_administration
    human_control_surfaces:
      - DEVELOPER_AUDIT
      - ADMIN_FACING
    inventory_state: CONFIRMED_NEW_MODULE_NOT_IMPLEMENTED
    implementation_eligible_now: false
    portfolio_gate: HOLD_UNTIL_PORTFOLIO_READINESS_BASELINE_COMPLETE
    module_value_test: KEEP
proposed_noncanonical_modules:
  forprint_semantic_retrieval_service:
    status: PROPOSED_ONLY_NOT_CANONICAL_MODULE_ID
    module_value_test: REVIEW_BEFORE_PROMOTION
```

### BLUEPRINT CONTEXT â€” coordination/roadmaps/details/forprint_system_blueprint/portfolio_module_roadmap_approval_matrix_v0_1.md

`SHA256=2efa675aac3ac5b5c1b95d5261a4a5c5040917ea771286ad4ae4358a9dfef4ad`

```md
# ForPrint Portfolio Module Roadmap Approval Matrix v0.1

Status: **ACTIVE INTERNAL PORTFOLIO ANALYSIS**

## Distribution gate

**CLOSED.** No module assistant contact, task distribution, prompt activation or implementation is authorized.

## Module horizons

### `calculator_engine`

Role: Calculation, quote and structured Job Specification engine

1. **AGREED_PLANNING_DIRECTION** — Reconcile implemented calculation, filename parsing, external-reference evidence and stale calculator documentation.
2. **AGREED_PLANNING_DIRECTION** — Confirm Calculator ownership of calculation/quote/Job Spec semantics and its non-ownership of catalog/accounting/order truth.
3. **AGREED_PLANNING_DIRECTION** — Complete capability self-inventory for products, rules, pricing, material/time estimates, filename profiles and warnings.
4. **AGREED_PLANNING_DIRECTION** — Define Contract Registry lifecycle for Calculator Job Specification and mandatory consumer compatibility.
5. **AGREED_OR_RECOVERED_TARGET** — Reconcile Library-owned materials, aliases, production naming profiles and omission/default semantics.
6. **AGREED_OR_RECOVERED_TARGET** — Specify deterministic calculation, rounding, sheet/copy semantics, warnings and evidence fixtures.
7. **AGREED_OR_RECOVERED_TARGET** — Define early visual configuration/workbench UX without duplicating Library catalog or CRM/order truth.
8. **PROPOSED_TARGET_REFINEMENT** — Design outsourcing decision rules and provider adapters, keeping credentials and provider specifics outside Calculator truth.
9. **PROPOSED_TARGET_REFINEMENT** — Define actual-vs-norm feedback intake from Runtime Inspector as proposals that can never silently rewrite approved norms.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold implementation expansion until producer/consumer contracts, self-inventory and portfolio dependency gates are approved.

### `cloud_backup_manager`

Role: Infrastructure backup utility/reference UI shell

1. **AGREED_PLANNING_DIRECTION** — Reconcile implemented backup utility capabilities, UI shell evidence and overlap with SysAdmin.
2. **AGREED_PLANNING_DIRECTION** — Confirm current ownership of backup jobs/sources/targets/health only; no business workflow or domain truth.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for backup scheduling, retention, health, restore evidence and UI capabilities.
4. **AGREED_PLANNING_DIRECTION** — Define encryption, retention, failure reporting and restore-test expectations under SysAdmin security policy.
5. **AGREED_OR_RECOVERED_TARGET** — Define handoff of backup health and recovery evidence to SysAdmin without duplicate platform authority.
6. **AGREED_OR_RECOVERED_TARGET** — Evaluate whether its UI shell remains a reusable reference without making it the shared UI source of truth.
7. **AGREED_OR_RECOVERED_TARGET** — Compare capabilities against SysAdmin backup/PITR roadmap and identify exact duplication.
8. **PROPOSED_TARGET_REFINEMENT** — Choose KEEP, MERGE_INTO_SYSADMIN or RETIRE as a portfolio decision with migration evidence.
9. **PROPOSED_TARGET_REFINEMENT** — If kept, define narrow support-module contracts and operational health SLAs.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Do not expand implementation until the module-value decision is explicitly approved.

### `forprint_accounting_registry_service`

Role: Operational/commercial accounting registry and 1C compatibility boundary

1. **AGREED_PLANNING_DIRECTION** — Reconcile current accounting registry, 1C staging, document and supplier-automation evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm accounting ownership of accounting references/documents/reconciliation while excluding operational order and catalog truth.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for 1C snapshots, mappings, import/export/reconciliation jobs and accounting documents.
4. **AGREED_PLANNING_DIRECTION** — Define billing/customer/responsibility contexts and prevent proof/sample classifications from implying payment semantics.
5. **AGREED_OR_RECOVERED_TARGET** — Define rounding, totals, taxes/fees and reconciliation boundaries so accounting never silently changes Calculator semantics.
6. **AGREED_OR_RECOVERED_TARGET** — Plan supplier-document parsing into reviewable staging rather than direct authoritative posting.
7. **AGREED_OR_RECOVERED_TARGET** — Define payment/reconciliation views and safe conditional mandates with explicit approval and audit boundaries.
8. **PROPOSED_TARGET_REFINEMENT** — Define management-accounting and settlement projections while preserving operational/accounting truth separation.
9. **PROPOSED_TARGET_REFINEMENT** — Plan mature 1C exchange, failure recovery and evidence without allowing 1C compatibility to dominate internal architecture.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold automation expansion until operational, warehouse, calculator and identity dependencies are contractually ready.

### `forprint_contract_registry`

Role: Versioned inter-module contract lifecycle registry

1. **AGREED_PLANNING_DIRECTION** — Reconcile existing contract concepts, manifests, lifecycle states and governance references.
2. **AGREED_PLANNING_DIRECTION** — Confirm Contract Registry as lifecycle/compatibility authority, not business semantics or runtime routing authority.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for contract IDs, revisions, producer/consumer registration, fixtures and compatibility evidence.
4. **AGREED_PLANNING_DIRECTION** — Finalize lifecycle states and the rule that breaking revisions cannot become ACTIVE before mandatory consumers support them.
5. **AGREED_OR_RECOVERED_TARGET** — Use Calculator Job Specification to OCR/Prepress as the first full contract-lifecycle planning pilot.
6. **AGREED_OR_RECOVERED_TARGET** — Define adoption matrix, compatibility checks, migration metadata and Inspector evidence expectations.
7. **AGREED_OR_RECOVERED_TARGET** — Define deprecation, supported-legacy, revoked and retired handling with explicit operator/governance boundaries.
8. **PROPOSED_TARGET_REFINEMENT** — Plan generated read-only contract catalogs and projections without creating a second semantic source of truth.
9. **PROPOSED_TARGET_REFINEMENT** — Define Integration Gateway consumption of ACTIVE contracts only and prevent unilateral activation by producers or consumers.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold runtime activation until pilot evidence and portfolio dependency gates are explicitly approved.

### `forprint_crm`

Role: Unified human business cockpit, analytics and composite workflow entry point

1. **AGREED_PLANNING_DIRECTION** — Reconcile CRM dashboard, person/organization context, workflow and cross-module read-projection evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm CRM as human business cockpit/coordinator, not owner of accounting, catalog, calculation or operational registry truth.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for dashboards, operator decisions, analytics, composite workflows and context selection.
4. **AGREED_PLANNING_DIRECTION** — Define person, organization and temporal relationship views while keeping technical auth identity in IAM.
5. **AGREED_OR_RECOVERED_TARGET** — Define Customer/Supplier 360 from domain-owned projections with explicit source and write-routing boundaries.
6. **AGREED_OR_RECOVERED_TARGET** — Plan Task/Case and Exception Center workflows that coordinate domain actions without becoming a shadow operational registry.
7. **AGREED_OR_RECOVERED_TARGET** — Define universal search, saved role workspaces and activity timeline with provenance and permission-aware visibility.
8. **PROPOSED_TARGET_REFINEMENT** — Plan variance/exception analytics and configurable wallboards using reporting projections, not transactional ownership.
9. **PROPOSED_TARGET_REFINEMENT** — Define composite cross-module workflow UI with explicit commands to domain owners and audited confirmations.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold implementation expansion until IAM, operational, accounting, warehouse and logistics contracts are reconciled.
11. **AGREED_PLANNING_DIRECTION** — Define the CRM customer-intelligence model as separate Seed Profile, Observed Customer Model and Effective Policy layers without absorbing canonical client identity or foreign domain truth.
12. **AGREED_PLANNING_DIRECTION** — Define manager-selectable Seed Profiles as bootstrap presets with explicit scope, version and provenance.
13. **AGREED_PLANNING_DIRECTION** — Define the Observed Customer Model with evidence provenance, recency, confidence, domain-specific coverage and safe handling of insufficient evidence.
14. **AGREED_PLANNING_DIRECTION** — Define Effective Policy composition so approved rules may consume customer-model evidence without silently expanding financial, commercial or operational authority.
15. **AGREED_PLANNING_DIRECTION** — Implement baseline-to-shift semantics with exception, possible-shift, probable-shift and new-baseline states plus recency weighting, minimum evidence, hysteresis and contextual segmentation.
16. **AGREED_PLANNING_DIRECTION** — Define multidimensional customer health and trajectory projections using owner-sourced payment, value, growth, margin, service-burden, clarity, dispute, stability and strategic-potential evidence.
17. **AGREED_PLANNING_DIRECTION** — Define event-driven customer-model updates plus periodic reconciliation, freshness checks and explicit conflict/staleness handling.
18. **AGREED_PLANNING_DIRECTION** — Define immutable profile/policy transition history, provenance and auditable human override before customer-specific policy automation is considered mature.
19. **AGREED_PLANNING_DIRECTION** — Define CRM views for active processes, current step, blockers, waiting state, deadlines, escalations and next authorized actions from Process Manager projections.
20. **AGREED_PLANNING_DIRECTION** — Define structured operator commands for clarification, acknowledgement, override request and authorized intervention without creating shadow workflow state.

### `forprint_integration_gateway`

Role: Runtime transport validation/routing/idempotency/correlation boundary

1. **AGREED_PLANNING_DIRECTION** — Reconcile current Gateway concept and verify that no runtime need justifies premature activation.
2. **AGREED_PLANNING_DIRECTION** — Confirm Gateway owns transport validation/routing/idempotency/correlation only, never business decisions or domain truth.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for envelopes, routing rules, validation errors, idempotency and correlation contexts.
4. **AGREED_PLANNING_DIRECTION** — Bind all routing to Contract Registry ACTIVE contracts and reject unsupported revisions deterministically.
5. **AGREED_OR_RECOVERED_TARGET** — Define command/query transport boundaries, retries, deadlines, hop/loop budgets and dead-letter behavior.
6. **AGREED_OR_RECOVERED_TARGET** — Define delivery ledger and observability projections without becoming operational event truth.
7. **AGREED_OR_RECOVERED_TARGET** — Define degraded/manual-review behavior and operator-attention routing for repeated or cyclic failures.
8. **PROPOSED_TARGET_REFINEMENT** — Plan scalable routing/adapters only when concrete channel/domain traffic requires a shared gateway.
9. **PROPOSED_TARGET_REFINEMENT** — Set objective activation criteria so direct module contracts remain preferred until central routing adds value.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Remain PAUSED until runtime need and portfolio approval are explicit.
11. **AGREED_PLANNING_DIRECTION** — Define transport correlation between Gateway delivery attempts and Process Manager process/event identities without merging their state machines.
12. **AGREED_PLANNING_DIRECTION** — Keep Gateway retry/dead-letter decisions transport-scoped while business waiting, deadline and escalation truth remains in the hosted Process Manager capability.

### `forprint_identity_access_service`

Role: Shared identity/authentication/authorization/access service

1. **AGREED_PLANNING_DIRECTION** — Reconcile the new IAM concept against current module identity, CRM business-person and SysAdmin security boundaries.
2. **AGREED_PLANNING_DIRECTION** — Confirm ownership of technical accounts/auth/session/authorization while CRM retains business person/customer relationships.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for account IDs, sessions, devices, roles, permissions, overrides, recovery and audit.
4. **AGREED_PLANNING_DIRECTION** — Define account_id to CRM person_id linkage and separate selected business context from authenticated technical identity.
5. **AGREED_OR_RECOVERED_TARGET** — Define deny-by-default authorization, role baselines and per-user overrides with auditable access decisions.
6. **AGREED_OR_RECOVERED_TARGET** — Plan modern password hashing, MFA/passkeys, recovery and device/session controls.
7. **AGREED_OR_RECOVERED_TARGET** — Define SSO/shared-client boundary for web, mobile, Telegram/admin clients without duplicating business context.
8. **PROPOSED_TARGET_REFINEMENT** — Separate external partner credentials into centralized SysAdmin secrets infrastructure with least privilege and rotation.
9. **PROPOSED_TARGET_REFINEMENT** — Define admin access-review UI, security audit evidence and revocation/recovery procedures.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Keep module unimplemented until portfolio roadmap, SysAdmin and operational dependencies are approved.

### `forprint_library`

Role: Canonical semantic/catalog/reference and shared UI publication authority

1. **AGREED_PLANNING_DIRECTION** — Reconcile current Library catalog, alias, template, naming-profile and UI publication evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm Library ownership of product/material/service/operation semantics and shared UI publication, excluding business workflows.
3. **AGREED_PLANNING_DIRECTION** — Complete capability/self-inventory for canonical IDs, aliases, misspellings, production tokens, templates and technical cards.
4. **AGREED_PLANNING_DIRECTION** — Define versioned naming/profile/default semantics consumed by Calculator, Prepress and operations surfaces.
5. **AGREED_OR_RECOVERED_TARGET** — Define material/product/service canonical identifiers and stable lookup contracts for Warehouse and other consumers.
6. **AGREED_OR_RECOVERED_TARGET** — Define UI design-system package lifecycle: lookup, proposal, prototype, Inspector review, operator approval, publish and adoption.
7. **AGREED_OR_RECOVERED_TARGET** — Add version/adoption metadata and compatibility rules without creating live global CSS or uncontrolled defaults.
8. **PROPOSED_TARGET_REFINEMENT** — Plan fast capability/semantic discovery while keeping retrieval candidate-only and domain-owner truth authoritative.
9. **PROPOSED_TARGET_REFINEMENT** — Define deprecation/migration paths for legacy aliases/profiles and evidence requirements for consumer adoption.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold broader implementation until Contract Registry and consumer readiness are reconciled in the portfolio.
11. **AGREED_PLANNING_DIRECTION** — Define stable historical/reference asset metadata semantics including asset ID, source module, entity links, revision references, media type and provenance.
12. **AGREED_PLANNING_DIRECTION** — Define the boundary between Library-owned canonical reference media and customer/order/production assets owned by operational domains.

### `forprint_marketing_orchestrator`

Role: Marketing campaign/content orchestration

1. **AGREED_PLANNING_DIRECTION** — Reconcile marketing/content orchestration concept and verify separation from CRM/customer truth.
2. **AGREED_PLANNING_DIRECTION** — Confirm ownership of campaign/content planning and creative workflow with mandatory human-reviewed publication.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for briefs, content plans, asset review and campaign-performance views.
4. **AGREED_PLANNING_DIRECTION** — Define Library asset/product semantics and CRM lead/audience handoff boundaries.
5. **AGREED_OR_RECOVERED_TARGET** — Define Accounting budget/cost/performance inputs without creating marketing accounting truth.
6. **AGREED_OR_RECOVERED_TARGET** — Plan multi-channel publication adapters with explicit authorization, scheduling, rollback and audit.
7. **AGREED_OR_RECOVERED_TARGET** — Plan AI image/video/content provider routing with centralized secrets, cost budgets and human review.
8. **PROPOSED_TARGET_REFINEMENT** — Define campaign performance learning as advisory proposals rather than silent strategy mutation.
9. **PROPOSED_TARGET_REFINEMENT** — Define lead/conversion handoff to CRM with provenance and no duplicate customer history.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Remain NON-BLOCKING/FUTURE until core operational portfolio is mature and operator approves activation.

### `forprint_operations_assistant`

Role: Low-friction shop-floor assistant, guided forms and operational knowledge

1. **AGREED_PLANNING_DIRECTION** — Reconcile shop-floor assistant, SOP, guided-form, Job Ticket and observation concepts.
2. **AGREED_PLANNING_DIRECTION** — Confirm assistant as low-friction human surface, not owner of order, accounting, catalog or unbounded decision truth.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for interaction context, guided forms, procedures, operational knowledge and observation capture.
4. **AGREED_PLANNING_DIRECTION** — Define role-aware authentication/authorization through IAM and context through operational registry interfaces.
5. **AGREED_OR_RECOVERED_TARGET** — Define Job Ticket assistance, HOLD/priority/proof/reprint visibility and explicit operator confirmation boundaries.
6. **AGREED_OR_RECOVERED_TARGET** — Plan physical observation capture for equipment/material/quality events with provenance and routing to domain owners.
7. **AGREED_OR_RECOVERED_TARGET** — Define mobile/paper/QR assistance where QR identifies a job/resource but never grants permission.
8. **PROPOSED_TARGET_REFINEMENT** — Plan visual SOP/training and contextual help from Library/knowledge sources without silently inventing procedures.
9. **PROPOSED_TARGET_REFINEMENT** — Define bounded operational AI fallback with budgets, escalation and Assistant Intervention Ledger evidence.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Keep execution disabled until portfolio approval and dependent operational/identity/library contracts are ready.

### `forprint_operations_control_registry`

Role: Canonical operational party/order/task/control registry and write boundary

1. **AGREED_PLANNING_DIRECTION** — Reconcile operational order/request/task/event/party concepts, historical aliases, and the historical Operational Registry → canonical Operations Control Registry repository/layout mapping while preserving immutable historical provenance.
2. **AGREED_PLANNING_DIRECTION** — Confirm stable operational identities and the authorized operational-truth/write boundary for clients/orders/jobs/tasks/status/events, with explicit Accounting/CRM/Library/Warehouse/Logistics/Prepress exclusions and no foreign-domain semantic absorption.
3. **AGREED_PLANNING_DIRECTION** — Complete current-worktree self-inventory for business-partner references, order IDs, requests, tasks, blockers, incidents, deadlines and current documentation/status; classify the persistent core separately from next-generation foundations.
4. **AGREED_PLANNING_DIRECTION** — Define the canonical operational order/Job Ticket lifecycle, including explicit HOLD, priority, proof, reprint and exception states; reconcile OrderRecord versus OperationalOrder generation while separating order, workflow/process, production, payment-fact/projection and dictionary/reference status axes.
5. **AGREED_OR_RECOVERED_TARGET** — Define obligations, requirements, reservations, shortages and execution-context contracts with Warehouse, Accounting, Logistics and Prepress, preserving each domain's truth and making inbound fact/reference directions explicit.
6. **AGREED_OR_RECOVERED_TARGET** — Define command/query and event-contract boundaries plus outbox/inbox/idempotency/correlation rules for resilient cross-module interactions; once the project interaction-role taxonomy is canonical, distinguish semantic/domain ownership from message direction and transport/runtime state.
7. **AGREED_OR_RECOVERED_TARGET** — Define stable business-partner/person/organization/customer/billing/delivery identity and reference boundaries across Operations, CRM, IAM, Accounting and Logistics while preserving historical relationships, before promoting the rich ClientAccount foundation to canonical truth.
8. **PROPOSED_TARGET_REFINEMENT** — Define read/write interfaces used by CRM and channels without transferring ownership of operational truth.
9. **PROPOSED_TARGET_REFINEMENT** — Plan reporting projections and exception/event evidence for dashboards without making read models authoritative.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold expanded execution until Calculator/Library/Contract Registry producer dependencies and portfolio gates are ready.
11. **AGREED_PLANNING_DIRECTION** — Define the operational historical-asset link contract connecting asset references to order ID, job ID, revision and authoritative operational state.
12. **AGREED_PLANNING_DIRECTION** — Define explicit current/superseded/production-result and approval-related revision evidence required by historical asset consumers.
13. **AGREED_PLANNING_DIRECTION** — Expose operational revision/status projections for historical retrieval without transferring operational truth into the search/index layer.
14. **AGREED_PLANNING_DIRECTION** — Define the hosted Process Manager namespace and durable process-instance identity/state model inside Operations Control Registry.
15. **AGREED_PLANNING_DIRECTION** — Define current-step, waiting-condition, expected-event, timer, deadline, retry, escalation and transition semantics for long-running processes.
16. **AGREED_PLANNING_DIRECTION** — Define an append-only process transition/event ledger with correlation, idempotency, restart recovery and deterministic resume semantics.
17. **AGREED_PLANNING_DIRECTION** — Define operator-attention and authorized human-decision integration without letting unattended workflow state silently authorize foreign-domain actions.
18. **AGREED_PLANNING_DIRECTION** — Define domain adapters so CRM, Telegram, Logistics and other modules can observe or participate through typed process intents/events without owning the durable process instance.
19. **AGREED_PLANNING_DIRECTION** — Add explicit extraction-readiness criteria so the capability can later move to a standalone Process Manager service if scale, topology or ownership evidence justifies separation.

### `forprint_prepress_hub`

Role: Prepress/file preparation and production-readiness evidence

1. **AGREED_PLANNING_DIRECTION** — Reconcile current PDF/document probe, readiness and prepress planning evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm Prepress ownership of file preparation/readiness evidence, not Calculator logic, catalog truth or device identity.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for probes, requirements, blockers, corrections, profiles, imposition and production-package outputs.
4. **AGREED_PLANNING_DIRECTION** — Define consumption of accepted Calculator Job Spec and Library naming/material/profile contracts.
5. **AGREED_OR_RECOVERED_TARGET** — Specify deterministic PDF validation/correction boundaries; ambiguous semantic repair must escalate rather than guess.
6. **AGREED_OR_RECOVERED_TARGET** — Plan imposition, normalization and production profile selection with explicit evidence and reproducible fixtures.
7. **AGREED_OR_RECOVERED_TARGET** — Define hot-folder/station preset policy while concrete device identity/capability remains SysAdmin-owned.
8. **PROPOSED_TARGET_REFINEMENT** — Define HOLD/reject/readiness evidence and handoff to operational Job Ticket/QC flows.
9. **PROPOSED_TARGET_REFINEMENT** — Plan production-file provenance and future metadata projections without making filenames the source of truth.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold implementation expansion until Calculator, Library and Contract Registry dependencies are accepted.
11. **AGREED_PLANNING_DIRECTION** — Define a machine-readable technical Asset Fact Packet containing deterministic file facts, source revision, hashes and safe preview references.
12. **AGREED_PLANNING_DIRECTION** — Define deterministic fingerprint/probe outputs suitable for downstream candidate retrieval while keeping semantic match decisions outside Prepress.
13. **AGREED_PLANNING_DIRECTION** — Define historical-file provenance and master-versus-derived relationships without making Prepress the raw archive or historical search owner.

### `forprint_project_inspector`

Role: Read-only structural/semantic/conformance verification

1. **AGREED_PLANNING_DIRECTION** — Reconcile Inspector structural, semantic, cleanliness, UI and contract-conformance scope.
2. **AGREED_PLANNING_DIRECTION** — Confirm Inspector detects/report conflicts but never invents domain truth, owns architecture or mutates foreign semantics.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for repository checks, module readiness, duplicate capability, UI and document-surface conformance.
4. **AGREED_PLANNING_DIRECTION** — Define deterministic checks first: schema, generators, indexes, ownership, duplicate capabilities and contract adoption.
5. **AGREED_OR_RECOVERED_TARGET** — Define bounded semantic review only after deterministic evidence, with context limits and stable finding taxonomy.
6. **AGREED_OR_RECOVERED_TARGET** — Define checkpoint-to-commit evidence and read-only audit packages with reproducible references.
7. **AGREED_OR_RECOVERED_TARGET** — Define cleanliness pack against Document Type/Generator/Validator registries and canonical source maps.
8. **PROPOSED_TARGET_REFINEMENT** — Define periodic/risk-triggered semantic audits, including UI conformance and legal issue spotting only.
9. **PROPOSED_TARGET_REFINEMENT** — Define advisory escalation and manual resolution without automatic truth activation or foreign-repo rewrite.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold runtime-like automation until portfolio and governance acceptance criteria are satisfied.

### `forprint_strategic_control_plane`

Role: Strategic priority/status/decision-support layer

1. **AGREED_PLANNING_DIRECTION** — Reconcile whether a separate strategic control plane still adds value beyond Blueprint and CRM analytics.
2. **AGREED_PLANNING_DIRECTION** — Confirm any future role as advisory priority/status layer, not current runtime orchestration or operator override.
3. **AGREED_PLANNING_DIRECTION** — Complete a minimal self-inventory/value hypothesis before creating implementation scope.
4. **AGREED_PLANNING_DIRECTION** — Define strategic goals/priority/status inputs and provenance from Blueprint/domain reporting projections.
5. **AGREED_OR_RECOVERED_TARGET** — Define scenario analysis and KPI aggregation as advisory outputs with explicit uncertainty.
6. **AGREED_OR_RECOVERED_TARGET** — Define stale-direction challenge mechanism that proposes review without changing priorities automatically.
7. **AGREED_OR_RECOVERED_TARGET** — Define boundaries against Blueprint architecture authority, CRM operational dashboards and Accounting metrics.
8. **PROPOSED_TARGET_REFINEMENT** — Plan decision-support loops and operator review surfaces only if duplication remains acceptably low.
9. **PROPOSED_TARGET_REFINEMENT** — Run module-value test: KEEP, MERGE or RETIRE based on demonstrated unique capability.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Remain NON-BLOCKING/FUTURE until explicit portfolio decision.

### `forprint_system_administration`

Role: IT/workplace/device/data-platform/secrets administration

1. **AGREED_PLANNING_DIRECTION** — Reconcile workstation, endpoint, device, PostgreSQL, backup and secrets administration evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm SysAdmin ownership of physical IT/platform operations without owning business data semantics or workflow.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for endpoints, approved software, device identity/capabilities, DB platform, secrets and backups.
4. **AGREED_PLANNING_DIRECTION** — Define canonical device identity/model/serial/capability inventory distinct from eligible queues/groups.
5. **AGREED_OR_RECOVERED_TARGET** — Define central PostgreSQL platform operations, roles, credentials, backups/PITR and health while domain schemas retain semantic ownership.
6. **AGREED_OR_RECOVERED_TARGET** — Define centralized secrets storage, least privilege, rotation, audit and provider credential boundaries.
7. **AGREED_OR_RECOVERED_TARGET** — Reconcile Cloud Backup Manager responsibilities and decide keep/merge/retire based on capability overlap and evidence.
8. **PROPOSED_TARGET_REFINEMENT** — Plan fleet onboarding, software consistency, disk/health monitoring and administrative readiness gates.
9. **PROPOSED_TARGET_REFINEMENT** — Define admin Control Center surfaces and audited privileged actions without arbitrary remote-shell authority.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold expanded automation until Inspector/backup/platform contracts and operator security policy are approved.

### `forprint_system_blueprint`

Role: Architecture/governance/portfolio coordination

1. **AGREED_PLANNING_DIRECTION** — Reconcile all evening/morning Human Intent, handoff evidence and current canonical planning surfaces.
2. **AGREED_PLANNING_DIRECTION** — Close canonical module identity questions, including the review-only semantic retrieval candidate.
3. **AGREED_PLANNING_DIRECTION** — Lock module charters, data ownership and must-not-own boundaries across the portfolio.
4. **AGREED_PLANNING_DIRECTION** — Complete module self-inventory/self-index baselines and reusable-capability visibility.
5. **AGREED_OR_RECOVERED_TARGET** — Replace generic mature targets with module-specific current-to-target roadmaps and explicit gaps.
6. **AGREED_OR_RECOVERED_TARGET** — Reconcile producer/consumer dependencies, Contract Registry timing and dependency-constrained readiness.
7. **AGREED_OR_RECOVERED_TARGET** — Bind shared UI, IAM, PostgreSQL, anti-loop, cleanliness and Human Control Surface standards to module plans.
8. **PROPOSED_TARGET_REFINEMENT** — Run portfolio balancing/critical-path review so no assistant outruns blocked producers.
9. **PROPOSED_TARGET_REFINEMENT** — Resolve semantic conflicts and mark each roadmap step AGREED, PROPOSED, BLOCKED or REVIEW-ONLY.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Obtain explicit operator approval of the portfolio and only then prepare future assistant distribution/execution packages.
11. **AGREED_PLANNING_DIRECTION** — Define the cross-module Historical Asset Index contract over Library reference semantics, Prepress technical asset facts and Operations Control Registry order/job/revision state.
12. **AGREED_PLANNING_DIRECTION** — Define candidate retrieval stages as cheap scoped retrieval followed by deeper comparison of a small candidate set and explicit human/customer selection when ambiguity remains.
13. **AGREED_PLANNING_DIRECTION** — Resolve the final hosted-capability location only after comparing an existing-host implementation with the noncanonical Semantic Retrieval module candidate.
14. **AGREED_PLANNING_DIRECTION** — Govern the hosted Process Manager boundary so process truth, domain truth, transport state and human-facing workflow UI remain explicitly separated.
15. **AGREED_PLANNING_DIRECTION** — Review extraction triggers after real usage evidence, including independent scaling, availability, topology, ownership pressure and cross-domain coupling.

### `logistics_service`

Role: Provider-neutral shipment/pickup/delivery/tracking truth

1. **AGREED_PLANNING_DIRECTION** — Reconcile Logistics provider-neutral shipment/pickup/delivery/tracking model and existing H10 pilot evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm Logistics truth boundaries against OCR operational identities, Accounting costs and IAM access.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for shipment drafts, provider adapters, tracking events, delivery evidence and exceptions.
4. **AGREED_PLANNING_DIRECTION** — Define stable shipment/order/address references and provider-neutral command/response contracts.
5. **AGREED_OR_RECOVERED_TARGET** — Define carrier/taxi/courier adapter boundary, secrets usage, retries, idempotency and correlation.
6. **AGREED_OR_RECOVERED_TARGET** — Define pickup/delivery/tracking event lifecycle plus evidence for failures, cancellation and manual takeover.
7. **AGREED_OR_RECOVERED_TARGET** — Define cost/charge handoff to Accounting without making Logistics accounting authority.
8. **PROPOSED_TARGET_REFINEMENT** — Define delivery exception and escalation workflows with Telegram/operator attention but no hidden auto-decisions.
9. **PROPOSED_TARGET_REFINEMENT** — Evaluate the existing Logistics-only H10 automation pilot against cost, quality, retry and operator-intervention evidence.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Do not widen H10 or authorize other modules until the pilot and full portfolio are explicitly approved.
11. **AGREED_PLANNING_DIRECTION** — Define the boundary between Logistics shipment lifecycle state and a parent or linked cross-domain Process Manager instance.
12. **AGREED_PLANNING_DIRECTION** — Expose typed shipment events, waiting conditions and outcomes to Process Manager without transferring carrier/provider truth out of Logistics.

### `mobile_app`

Role: Future mobile customer/staff channel

1. **AGREED_PLANNING_DIRECTION** — Reconcile mobile-app concept against Website, Telegram and shared-domain channel architecture.
2. **AGREED_PLANNING_DIRECTION** — Confirm Mobile App as deferred client/channel with no domain truth ownership.
3. **AGREED_PLANNING_DIRECTION** — Complete a future self-inventory skeleton for auth, account, calculation, order, file, payment and delivery surfaces.
4. **AGREED_PLANNING_DIRECTION** — Define IAM/session/device security and selected business-context behavior before any client implementation.
5. **AGREED_OR_RECOVERED_TARGET** — Reuse the same Calculator, Library, OCR and delivery contracts as web instead of creating mobile-specific semantics.
6. **AGREED_OR_RECOVERED_TARGET** — Define offline/cache behavior as non-authoritative with explicit freshness/conflict handling.
7. **AGREED_OR_RECOVERED_TARGET** — Plan notifications, uploads and customer confirmations through bounded APIs and audit evidence.
8. **PROPOSED_TARGET_REFINEMENT** — Define accessibility, device compatibility, telemetry and release/security requirements.
9. **PROPOSED_TARGET_REFINEMENT** — Reassess value/timing after Website and shared API contracts mature to avoid parallel duplication.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Remain DEFERRED until explicit portfolio approval releases the channel.

### `production_runtime_inspector`

Role: Runtime production actuals/evidence and exact device-used inspection

1. **AGREED_PLANNING_DIRECTION** — Reconcile current production-inspection, device-used and actuals concepts.
2. **AGREED_PLANNING_DIRECTION** — Confirm Runtime Inspector records actual execution evidence and never owns approved norms or general project conformance.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for concrete device, operation actuals, time/material actuals, quality and telemetry evidence.
4. **AGREED_PLANNING_DIRECTION** — Bind concrete device identity/model/serial/capability to SysAdmin sources and operational jobs to OCR identities.
5. **AGREED_OR_RECOVERED_TARGET** — Define actual material/time/operation capture and provenance without inferring missing production truth.
6. **AGREED_OR_RECOVERED_TARGET** — Define quality, defect and reprint signals with routing to Warehouse/OCR and traceable cause evidence.
7. **AGREED_OR_RECOVERED_TARGET** — Define variance calculation against approved norms without modifying Calculator/Library norms.
8. **PROPOSED_TARGET_REFINEMENT** — Plan norm-change proposal generation as reviewable suggestions routed to the correct domain owner.
9. **PROPOSED_TARGET_REFINEMENT** — Plan telemetry/health integration and runtime exception evidence without becoming equipment administration authority.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold broader runtime automation until contracts, identifiers and portfolio approval are complete.

### `telegram_bot`

Role: Conversational customer/staff channel adapter

1. **AGREED_PLANNING_DIRECTION** — Reconcile current Telegram channel flows, identity/context handling and historical execution evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm Telegram as channel adapter only, never canonical CRM/order/calculation/accounting/catalog truth.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for dialog flow, message UI, uploads, confirmations and channel context.
4. **AGREED_PLANNING_DIRECTION** — Define authentication/linkage through IAM and visible customer/billing/business context selection.
5. **AGREED_OR_RECOVERED_TARGET** — Define structured calculation/order request handoff to Calculator/OCR with audited confirmations.
6. **AGREED_OR_RECOVERED_TARGET** — Define file/status/payment/delivery views as domain-owned read projections with clear freshness/provenance.
7. **AGREED_OR_RECOVERED_TARGET** — Define context switching without duplicate CRM persons/orders and without phone becoming immutable identity.
8. **PROPOSED_TARGET_REFINEMENT** — Plan voice transcription and richer interaction as bounded channel capabilities with fallback and operator visibility.
9. **PROPOSED_TARGET_REFINEMENT** — Define retry/idempotency/correlation and anti-loop budgets for channel-to-domain interactions.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold new execution until IAM, Gateway/contract and portfolio readiness gates are approved.

11. **AGREED_PLANNING_DIRECTION** — Define personalized communication orchestration with conversation continuity, approved communication preferences and strict presentation-versus-facts separation.
12. **AGREED_PLANNING_DIRECTION** — Define channel-neutral inbound structured domain requests/events and outbound structured communication intents with correlation and provenance.
13. **AGREED_PLANNING_DIRECTION** — Define consumption of customer-specific communication context without moving canonical customer profile, commercial policy or analytics into Telegram.
14. **AGREED_PLANNING_DIRECTION** — Define bounded clarification and structured Order Draft interaction using canonical Library/Calculator/domain constraints.
15. **AGREED_PLANNING_DIRECTION** — Define deterministic-to-context-to-AI-to-human escalation with replaceable model/provider slots and progress/contradiction based escalation.
16. **AGREED_PLANNING_DIRECTION** — Define Telegram consumption of historical customer asset retrieval results without live archive scanning or asset-index ownership.
17. **AGREED_PLANNING_DIRECTION** — Define Telegram as a communication participant for durable long-running business processes while process state/timers/deadlines/transitions remain with the eventual canonical Process Manager owner.

### `warehouse_service`

Role: Physical inventory/material-location truth and movement service

1. **AGREED_PLANNING_DIRECTION** — Reconcile warehouse stock, location, movement, material and defect/reprint evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm Warehouse ownership of physical inventory truth distinct from accounting valuation and Calculator planned consumption.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for stock facts, locations, lots, movements, reservations, shortages and counts.
4. **AGREED_PLANNING_DIRECTION** — Bind all stock/material records to Library canonical material IDs and controlled alias resolution.
5. **AGREED_OR_RECOVERED_TARGET** — Define receipts, issues, transfers, writeoffs and reservations against stable operational order/job references.
6. **AGREED_OR_RECOVERED_TARGET** — Define shortage and availability contracts for Calculator/OCR without letting Warehouse decide pricing or production rules.
7. **AGREED_OR_RECOVERED_TARGET** — Define internal-defect/reprint material consumption as traceable physical movements with reason/evidence.
8. **PROPOSED_TARGET_REFINEMENT** — Plan cycle counts, discrepancy workflows and audit trails with explicit human resolution.
9. **PROPOSED_TARGET_REFINEMENT** — Define Accounting handoff for valuation/documents while retaining physical quantity/location truth.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Hold automation until Library, operational registry and accounting contracts are accepted.

### `website`

Role: Customer web channel using shared Calculator/Identity/domain contracts

1. **AGREED_PLANNING_DIRECTION** — Reconcile legacy website capabilities, duplicated semantics and current channel evidence.
2. **AGREED_PLANNING_DIRECTION** — Confirm Website as customer channel using shared domain contracts, not owner of Calculator/catalog/order/accounting truth.
3. **AGREED_PLANNING_DIRECTION** — Complete self-inventory for account, calculation, order, file, payment and delivery customer surfaces.
4. **AGREED_PLANNING_DIRECTION** — Define authentication/session integration through IAM and shared business-context selection.
5. **AGREED_OR_RECOVERED_TARGET** — Replace duplicated calculation/configuration logic with Calculator contracts and Library canonical semantics.
6. **AGREED_OR_RECOVERED_TARGET** — Define order/request/status interactions through OCR rather than local shadow order truth.
7. **AGREED_OR_RECOVERED_TARGET** — Define file/prepress/payment/delivery views through accepted domain projections and explicit provenance.
8. **PROPOSED_TARGET_REFINEMENT** — Adopt Library shared UI design-system packages with versioned controlled adoption.
9. **PROPOSED_TARGET_REFINEMENT** — Plan modern self-service UX, observability, accessibility and exception handling without bypassing domain owners.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Keep implementation deferred until Calculator, IAM, Library and operational contracts are portfolio-ready.

## Proposed noncanonical review

### `forprint_semantic_retrieval_service`

Review-only. This is not a module promotion or execution plan.

1. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Reconcile the proposed semantic retrieval concept against Library, Inspector, CRM search and Blueprint capability boundaries.
2. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Run module-necessity/value test before any canonical promotion.
3. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Define candidate-only retrieval semantics: retrieval finds candidates; domain owner decides truth.
4. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Define source/index provenance, freshness and access-control requirements.
5. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Define bounded indexing/query interfaces without creating a second semantic authority.
6. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Define evaluation datasets and precision/recall acceptance evidence for realistic project queries.
7. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Define permission-aware retrieval and prevention of cross-domain data leakage.
8. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Compare implementation cost/complexity against simpler indexed lookup/search capabilities.
9. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — Choose PROMOTE, MERGE or RETIRE as an explicit portfolio decision.
10. **REVIEW_ONLY_PROPOSED_NONCANONICAL** — If promoted, only then create canonical identity, ownership policy, dependencies and implementation roadmap.

<!-- project-cleanliness-conformance-2026-09-01:start -->
## Project cleanliness conformance

Project cleanliness is now a portfolio requirement for all canonical module repositories.

- Blueprint owns the single canonical cleanliness policy and current conformance projection.
- Each module owns cleanliness inside its own repository.
- Project Inspector is the future cross-repository conformance auditor, not a semantic owner.
- Blueprint local automated cleanliness checks are already implemented.
- Other module-local cleanliness packs are required/planned but are not started by this planning update.
- Inspector cross-repository automation is planned but not yet implemented.
- No module may create a competing project-wide cleanliness standard.
- Future assistant distribution requires a recorded cleanliness-conformance roadmap/state for the module.
- This planning requirement does not open implementation or assistant-distribution gates.
<!-- project-cleanliness-conformance-2026-09-01:end -->

<!-- ai-execution-safety-gate-2026-09-01 -->
## AI Execution Safety & Runtime Governance gate

Before future assistant distribution can reopen, the portfolio must review the planning gate at
`coordination/roadmaps/details/forprint_system_blueprint/ai_execution_safety_runtime_governance_gate_v0_1.md`.

Current state: `PLANNING_REQUIRED_NOT_IMPLEMENTED`.

This requirement does not authorize implementation, assistant contact, prompt activation or H10 widening.

### `verification_lab`

- Identity state: `CANONICAL`
- Strategic priority: `P0`
- Role: Independent verification, adversarial testing, fault-injection and deterministic regression evidence module.
- Module value test: `KEEP`
- Inventory state: `CONFIRMED_NEW_MODULE_NOT_IMPLEMENTED`
- Roadmap status: `PLANNING_ONLY_NOT_DISTRIBUTED`

**Dependencies / inputs**

- `forprint_system_blueprint`
- `forprint_contract_registry`
- `forprint_project_inspector`
- `forprint_system_administration`

**Owns**

- `verification_campaign_definition`
- `synthetic_test_case_corpus`
- `test_plane_scenario`
- `adversarial_test_execution`
- `deterministic_regression_corpus`
- `verification_finding_evidence`
- `release_candidate_verification_result`
- `fault_injection_profile`

**Must not own**

- `architecture_policy`
- `business_domain_truth`
- `production_runtime_control`
- `deployment_approval`
- `live_external_side_effects`
- `unrestricted_shell_authority`
- `secrets`
- `foreign_module_semantic_rewrite`

**Target state — agreed / recovered**

- Verification Lab is a distinct canonical module that intentionally tries to prove the system wrong before customers or incidents do.

**Target state — synthetic / proposed**

- Mature Verification Lab should support black/gray/white-box Test Plane campaigns, adversarial/fault/concurrency testing, deterministic regression and release-gate evidence with synthetic side effects only.

**Roadmap approval steps**

1. **AGREED_PLANNING_DIRECTION** — Establish Verification Lab canonical identity, charter and strict separation from Project Inspector and Runtime Inspector.
2. **AGREED_PLANNING_DIRECTION** — Define BLACK_BOX, GRAY_BOX and WHITE_BOX read-only diagnostic modes and their evidence boundaries.
3. **AGREED_PLANNING_DIRECTION** — Define Test Plane isolation with fake/synthetic payment, courier, printer, email, cloud, Telegram and database side effects.
4. **PROPOSED_TARGET_REFINEMENT** — Define normal/invalid/boundary/malformed/combinatorial/multilingual/out-of-domain/auth/data-isolation test taxonomy.
5. **PROPOSED_TARGET_REFINEMENT** — Define prompt-adversarial, tool-misuse, state-machine, concurrency, idempotency, stale-cache and schema-fuzz campaigns.
6. **PROPOSED_TARGET_REFINEMENT** — Define fault/recovery, timeout, unavailable-resource, retry/dead-letter, load/performance and cost-regression campaigns.
7. **PROPOSED_TARGET_REFINEMENT** — Convert useful AI-discovered failures into owner-confirmed deterministic regression corpus rather than permanent stochastic-only tests.
8. **PROPOSED_TARGET_REFINEMENT** — Define change-triggered, nightly, weekly, manual, pre-release and post-release verification campaign policy.
9. **PROPOSED_TARGET_REFINEMENT** — Define trace-aware evaluation of intermediate contract/tool/state behavior, not only final user-visible answer.
10. **HOLD_FOR_FINAL_PORTFOLIO_APPROVAL** — Remain planning-only until Test Plane, Execution Policy Gate, IAM and explicit operator distribution/implementation approval are ready.

<!-- FORPRINT_U92_U107_CANONICAL_INTEGRATION_20260903:START -->
## 2026-09-03 u92/u107 architecture integration

Canonical module count after approved planning promotion: **23**.

New canonical module: `verification_lab`.

`forprint_semantic_retrieval_service` remains proposed/noncanonical.

Roadmap/governance narrative:
`coordination/internal_work/blueprint/evening_reviews/2026-09-03/2026-09-03__u92_architecture_governance_integration_v0_1.md`

This planning integration does **not** authorize module implementation, assistant distribution,
prompt activation, H10 widening, automatic acceptance/release, or cross-repository diagnostics.
<!-- FORPRINT_U92_U107_CANONICAL_INTEGRATION_20260903:END -->
```

### BLUEPRINT CONTEXT â€” coordination/roadmaps/details/forprint_system_blueprint/portfolio_module_roadmap_approval_matrix_v0_1.yaml

`SHA256=5305f0d74cbef25eb533909c80df14fbb4e134a17cace603cd1e97b07cded8fd`

```yaml
schema_version: forprint_portfolio_module_roadmap_approval_matrix_v0_1
date: '2026-09-01'
status: ACTIVE_INTERNAL_PORTFOLIO_ANALYSIS
authority: planning_projection_not_release_or_execution_authority
distribution_gate:
  state: CLOSED
  assistant_contact_allowed: false
  assistant_task_distribution_allowed: false
  prompt_activation_allowed: false
  module_implementation_allowed: false
  reopen_requires:
    - portfolio analysis complete
    - module roadmaps reviewed
    - dependency/readiness balance reviewed
    - semantic conflicts dispositioned
    - explicit operator approval
    - AI Execution Safety & Runtime Governance gate reviewed for assistant launch
  ai_execution_safety_runtime_governance_state: PLANNING_REQUIRED_NOT_IMPLEMENTED
approval_legend:
  AGREED_PLANNING_DIRECTION: Direction is established for planning only.
  AGREED_OR_RECOVERED_TARGET: Grounded in existing agreed/recovered target evidence.
  PROPOSED_TARGET_REFINEMENT: Blueprint synthesis for mature-state completeness; owner review required.
  HOLD_FOR_FINAL_PORTFOLIO_APPROVAL: Stop before any assistant distribution or execution.
  REVIEW_ONLY_PROPOSED_NONCANONICAL: Not canonical and not executable.
operator_decision:
  summary: First absorb all morning/evening information into Blueprint, deepen roadmaps and portfolio, finish analysis, then distribute tasks later.
  verbatim_quote: поки що ми нічого помічникам не даємо мені саме головне зафіксувати всі домовленості в нашому особистому проекті і розписати погодження кроків по родмап для помічників поки що помічників ми не чіпаємо ми тільки наповнюємо дорожні карти і оформлюємо скажімо так портфоліо і ну скажімо робимо розуміння нашого проекту більш глибше поки що нікого не запускаємо в роботу
modules:
  calculator_engine:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Canonical production calculation, quote-item semantics and production-filename interpretation engine.
    module_value_test: KEEP
    inventory_state: OWNER_DIRECTION_CLEAR_DEEP_INVENTORY_REQUIRED
    dependencies_or_inputs:
      - forprint_library
      - forprint_contract_registry
      - forprint_prepress_hub
      - warehouse_service
    owns:
      - calculation_logic
      - calculation_output_package
      - quote_draft
      - order_draft
      - price_breakdown
      - material_consumption_estimate
      - calculation_warnings
    must_not_own:
      - canonical_client_registry
      - canonical_order_registry
      - canonical_catalog_truth
      - accounting_truth
      - one_c_synchronization
      - warehouse_stock_truth
      - prepress_lifecycle
      - crm_workflow
    target_state:
      agreed_or_recovered:
        - Calculation/quote/order drafts, price/material/time estimates, early visual configuration, exact reference set recovered.
        - Calculator owns calculated quote/item semantics and production filename interpretation, not the whole customer basket or order.
      synthetic_or_proposed:
        - Reusable constructor family, outsourcing decisions and partner-adapter integration.
        - Mature Calculator should expose deterministic contracts, offline estimate rules with revalidation and Verification Lab regression surfaces.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: CALCULATOR_ENGINE-H01
        title: Preserve Calculator ownership of calculation, quote-item and production-filename semantics.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: CALCULATOR_ENGINE-H02
        title: Keep Library as vocabulary/profile source and avoid local shadow aliases/defaults.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: CALCULATOR_ENGINE-H03
        title: Separate calculated item/quote from CRM basket/checkout and OCR canonical operational order state.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: CALCULATOR_ENGINE-H04
        title: Define stable request/result contracts with provenance, assumptions and deterministic rounding rules.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: CALCULATOR_ENGINE-H05
        title: Define offline estimate behavior where allowed and mandatory server/current-norm revalidation before commitment.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: CALCULATOR_ENGINE-H06
        title: Define deterministic filename correction only for unambiguous cases and retain source/provenance.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: CALCULATOR_ENGINE-H07
        title: Define Prepress capability/probe handoff without Calculator owning file-repair execution.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: CALCULATOR_ENGINE-H08
        title: Provide deterministic fixtures and boundary cases to Verification Lab for regression.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: CALCULATOR_ENGINE-H09
        title: Use Runtime Inspector actuals only as proposal evidence for norm changes, never silent rewrite.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: CALCULATOR_ENGINE-H10
        title: Hold broader automation until Library/Contract Registry/consumer adoption evidence is portfolio-ready.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  cloud_backup_manager:
    identity_state: CANONICAL
    strategic_priority: SUPPORT
    role: Off-site backup, controlled one-way corporate-resource replication and recovery-evidence support service.
    module_value_test: REVIEW_MERGE_LATER
    inventory_state: IMPLEMENTED_SUPPORT_MODULE
    dependencies_or_inputs:
      - forprint_system_administration
      - forprint_library
    owns:
      - backup_jobs
      - backup_targets
      - backup_sources
      - backup_health_reports
    must_not_own:
      - business_workflow
      - client_registry
      - order_registry
      - accounting_truth
      - catalog_truth
    target_state:
      agreed_or_recovered:
        - Backup/health support; UI reference shell candidate.
        - Cloud Backup Manager covers off-site backup, controlled one-way corporate-resource replication and retention/integrity/recovery evidence.
      synthetic_or_proposed:
        - Possible absorption into System Administration if lifecycle evidence justifies it.
        - Mature backup operation should be provider-neutral, encrypted, checksum-verified, restore-tested and resilient to temporary network loss.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: CLOUD_BACKUP_MANAGER-H01
        title: Reconcile implemented backup utility capabilities and exact overlap with SysAdmin platform operations.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: CLOUD_BACKUP_MANAGER-H02
        title: Confirm Cloud Backup Manager owns backup/replication jobs and recovery evidence, not business data semantics.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: CLOUD_BACKUP_MANAGER-H03
        title: Define domain-owned prepared-artifact backup inputs with explicit source ownership and provenance.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: CLOUD_BACKUP_MANAGER-H04
        title: Define one canonical publisher → many consumers replication for approved corporate resources without overwriting user areas.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: CLOUD_BACKUP_MANAGER-H05
        title: Define retention, versioning/immutability options, encryption, checksum and centralized secret requirements.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: CLOUD_BACKUP_MANAGER-H06
        title: Define RPO/RTO objectives and periodic restore verification as first-class acceptance evidence.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: CLOUD_BACKUP_MANAGER-H07
        title: Define provider abstraction, quota/health reporting and safe credential rotation boundaries.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: CLOUD_BACKUP_MANAGER-H08
        title: Define persistent offline queue/retry so temporary internet loss becomes WAITING/RETRY, never silent loss.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: CLOUD_BACKUP_MANAGER-H09
        title: Define bandwidth scheduling, retry backoff, alerts and degraded-mode behavior.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: CLOUD_BACKUP_MANAGER-H10
        title: Reassess KEEP versus merge into SysAdmin only after capability overlap and migration evidence are explicit.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  forprint_accounting_registry_service:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Operational/commercial accounting registry and 1C compatibility boundary
    module_value_test: KEEP
    inventory_state: OWNER_DIRECTION_CLEAR_DECOMPOSITION_REQUIRED
    dependencies_or_inputs: &id001
      - forprint_operations_control_registry
      - forprint_library
      - warehouse_service
      - calculator_engine
    owns:
      - accounting_references
      - one_c_raw_snapshot
      - one_c_staging_record
      - one_c_mapping_record
      - import_job
      - export_job
      - reconciliation_job
      - sandbox_one_c_io
    must_not_own:
      - operational_client_registry
      - operational_order_registry
      - canonical_catalog_truth
      - crm_workflow
      - calculator_logic
      - warehouse_stock_truth
    target_state:
      agreed_or_recovered:
        - Invoices/payments/accounting documents/reconciliation/1C staging; supplier-document automation.
      synthetic_or_proposed:
        - Management accounting, settlements, safe conditional mandates and mature 1C exchange.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H01
        title: Reconcile current accounting registry, 1C staging, document and supplier-automation evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H02
        title: Confirm accounting ownership of accounting references/documents/reconciliation while excluding operational order and catalog truth.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H03
        title: Complete self-inventory for 1C snapshots, mappings, import/export/reconciliation jobs and accounting documents.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H04
        title: Define billing/customer/responsibility contexts and prevent proof/sample classifications from implying payment semantics.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id001
      - sequence: 5
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H05
        title: Define rounding, totals, taxes/fees and reconciliation boundaries so accounting never silently changes Calculator semantics.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H06
        title: Plan supplier-document parsing into reviewable staging rather than direct authoritative posting.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H07
        title: Define payment/reconciliation views and safe conditional mandates with explicit approval and audit boundaries.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H08
        title: Define management-accounting and settlement projections while preserving operational/accounting truth separation.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H09
        title: Plan mature 1C exchange, failure recovery and evidence without allowing 1C compatibility to dominate internal architecture.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_ACCOUNTING_REGISTRY_SERVICE-H10
        title: Hold automation expansion until operational, warehouse, calculator and identity dependencies are contractually ready.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id001
  forprint_contract_registry:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Versioned inter-module contract lifecycle registry
    module_value_test: KEEP
    inventory_state: DIRECTION_CLEAR_FOUNDATION_PENDING
    dependencies_or_inputs: &id002
      - forprint_system_blueprint
      - forprint_project_inspector
    owns:
      - inter_module_contract_registry
      - contract_manifest_schema
      - contract_id_namespace
      - interface_contract_version_history
      - producer_consumer_registration
      - contract_lifecycle_metadata
      - contract_compatibility_baselines
      - contract_compatibility_results
      - contract_examples_and_fixtures
      - contract_release_metadata
      - contract_deprecation_and_migration_metadata
      - generated_read_only_contract_catalog
    must_not_own:
      - business_workflow_decisions
      - runtime_request_routing
      - runtime_transport_execution
      - catalog_business_semantics
      - product_or_material_definitions
      - pricing_logic
      - module_internal_data_models
      - operational_data_truth
      - prompt_governance
      - project_priority_decisions
    target_state:
      agreed_or_recovered:
        - Contract manifests/revisions/compatibility/adoption; first pilot Calculator Job Specification -> OCR.
      synthetic_or_proposed:
        - Generated projections, migration/deprecation automation and compatibility view after proven pilots.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_CONTRACT_REGISTRY-H01
        title: Reconcile existing contract concepts, manifests, lifecycle states and governance references.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_CONTRACT_REGISTRY-H02
        title: Confirm Contract Registry as lifecycle/compatibility authority, not business semantics or runtime routing authority.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_CONTRACT_REGISTRY-H03
        title: Complete self-inventory for contract IDs, revisions, producer/consumer registration, fixtures and compatibility evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_CONTRACT_REGISTRY-H04
        title: Finalize lifecycle states and the rule that breaking revisions cannot become ACTIVE before mandatory consumers support them.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id002
      - sequence: 5
        step_id: FORPRINT_CONTRACT_REGISTRY-H05
        title: Use Calculator Job Specification to OCR/Prepress as the first full contract-lifecycle planning pilot.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_CONTRACT_REGISTRY-H06
        title: Define adoption matrix, compatibility checks, migration metadata and Inspector evidence expectations.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_CONTRACT_REGISTRY-H07
        title: Define deprecation, supported-legacy, revoked and retired handling with explicit operator/governance boundaries.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_CONTRACT_REGISTRY-H08
        title: Plan generated read-only contract catalogs and projections without creating a second semantic source of truth.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_CONTRACT_REGISTRY-H09
        title: Define Integration Gateway consumption of ACTIVE contracts only and prevent unilateral activation by producers or consumers.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_CONTRACT_REGISTRY-H10
        title: Hold runtime activation until pilot evidence and portfolio dependency gates are explicitly approved.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id002
  forprint_crm:
    identity_state: CANONICAL
    strategic_priority: P1
    role: Business workflow coordinator, Customer Portal composition layer and cross-domain human workspace.
    module_value_test: KEEP
    inventory_state: FIRST_PASS_PLUS_NEW_OWNER_DIRECTION
    dependencies_or_inputs:
      - forprint_operations_control_registry
      - calculator_engine
      - forprint_accounting_registry_service
      - warehouse_service
      - logistics_service
      - forprint_identity_access_service
    owns:
      - human_dashboard
      - workflow_coordination_ui
      - operator_decision_views
      - analytics_views
      - composite_cross_module_workflow_ui
      - configurable_operational_dashboards
      - cross_module_read_projections
      - variance_and_exception_views
    must_not_own:
      - internal_forprint_db
      - canonical_client_registry
      - calculator_logic
      - accounting_truth
      - catalog_truth
      - foreign_domain_write_authority
      - physical_persistence_platform
    target_state:
      agreed_or_recovered:
        - Owner-data aggregation without foreign-data ownership; dashboards/wallboards; composite workflows.
        - CRM may compose Customer Portal and basket/checkout workflow while domain-owned semantics remain with their actual owners.
      synthetic_or_proposed:
        - Customer/Supplier 360, universal search, saved role views, activity timeline, exception center.
        - Mature CRM should provide customer/supplier 360, exception/task workspaces, universal search, timeline and cross-domain projections without absorbing foreign truth.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_CRM-H01
        title: Reconcile CRM as business coordinator and human workspace rather than physical owner of all ForPrint data.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_CRM-H02
        title: Preserve person/organization/context semantics and phone as strong identifier/search aid, not immutable identity.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_CRM-H03
        title: Define Customer Portal composition with shared IAM and selected business context.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_CRM-H04
        title: Define basket/checkout orchestration around Calculator quote items without creating calculator or accounting truth.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_CRM-H05
        title: Define request/order handoff through Operations Control Registry with stable operational identifiers.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_CRM-H06
        title: Define payment/accounting/logistics/warehouse views through owner-provided projections and explicit provenance.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_CRM-H07
        title: Define Task/Case/Exception Center and role-specific workspaces as CRM-owned workflow composition.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_CRM-H08
        title: Define universal search/timeline/customer-supplier 360 over read models without cross-domain write ownership.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_CRM-H09
        title: Define analytics/variance views while strategic recommendation ownership remains with Strategic Control Plane.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_CRM-H10
        title: Keep cross-domain writes contract-bound and dependency-gated before assistant distribution.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
      - sequence: 11
        step_id: FORPRINT_CRM-H11
        title: >-
          Define the CRM customer-intelligence model as separate Seed Profile, Observed Customer Model and Effective Policy layers without absorbing canonical client identity or foreign domain truth.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 12
        step_id: FORPRINT_CRM-H12
        title: >-
          Define manager-selectable Seed Profiles as bootstrap presets with explicit scope, version and provenance.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 13
        step_id: FORPRINT_CRM-H13
        title: >-
          Define the Observed Customer Model with evidence provenance, recency, confidence, domain-specific coverage and safe handling of insufficient evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 14
        step_id: FORPRINT_CRM-H14
        title: >-
          Define Effective Policy composition so approved rules may consume customer-model evidence without silently expanding financial, commercial or operational authority.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 15
        step_id: FORPRINT_CRM-H15
        title: >-
          Implement baseline-to-shift semantics with exception, possible-shift, probable-shift and new-baseline states plus recency weighting, minimum evidence, hysteresis and contextual segmentation.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 16
        step_id: FORPRINT_CRM-H16
        title: >-
          Define multidimensional customer health and trajectory projections using owner-sourced payment, value, growth, margin, service-burden, clarity, dispute, stability and strategic-potential evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 17
        step_id: FORPRINT_CRM-H17
        title: >-
          Define event-driven customer-model updates plus periodic reconciliation, freshness checks and explicit conflict/staleness handling.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 18
        step_id: FORPRINT_CRM-H18
        title: >-
          Define immutable profile/policy transition history, provenance and auditable human override before customer-specific policy automation is considered mature.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 19
        step_id: FORPRINT_CRM-H19
        title: >-
          Define CRM views for active processes, current step, blockers, waiting state, deadlines, escalations and next authorized actions from Process Manager projections.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 20
        step_id: FORPRINT_CRM-H20
        title: >-
          Define structured operator commands for clarification, acknowledgement, override request and authorized intervention without creating shadow workflow state.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
  forprint_integration_gateway:
    identity_state: CANONICAL
    strategic_priority: P2
    role: Narrow-waist transport, schema/version routing, idempotency, correlation and delivery-state boundary.
    module_value_test: KEEP
    inventory_state: PAUSED_UNTIL_RUNTIME_NEED
    dependencies_or_inputs:
      - forprint_contract_registry
      - forprint_operations_control_registry
      - forprint_identity_access_service
    owns:
      - integration_request_envelope
      - integration_response_envelope
      - routing_rule
      - validation_error
      - idempotency_boundary
      - correlation_context
    must_not_own:
      - business_workflow_decisions
      - client_registry
      - order_registry
      - catalog_truth
      - accounting_truth
      - crm_dashboard
    target_state:
      agreed_or_recovered:
        - Routes/validates ACTIVE contracts without business ownership.
        - Gateway owns transport/contract mechanics, not domain truth or business decisions.
      synthetic_or_proposed:
        - Delivery ledger, observability and scalable routing when runtime need justifies activation.
        - Mature Gateway should expose explicit queue/busy/retry/degraded outcomes, backpressure, deadlines, circuit breaking and dead-letter evidence.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_INTEGRATION_GATEWAY-H01
        title: Reconcile Gateway as narrow-waist transport and contract-validation infrastructure only.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_INTEGRATION_GATEWAY-H02
        title: Confirm no domain truth, pricing, customer, accounting or workflow-decision ownership.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_INTEGRATION_GATEWAY-H03
        title: Bind routing to supported Contract Registry revisions and reject unsupported revisions deterministically.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_INTEGRATION_GATEWAY-H04
        title: Define request envelopes, idempotency keys, correlation/causation and persistent delivery-state ledger semantics.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_INTEGRATION_GATEWAY-H05
        title: Define shared outcomes OK/QUEUED/BUSY_RETRYABLE/TEMPORARILY_UNAVAILABLE/TIMEOUT/CONFLICT/NOT_FOUND/PERMISSION_DENIED/FAILED_PERMANENT.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_INTEGRATION_GATEWAY-H06
        title: Define WAITING_RESOURCE/WAITING_EXTERNAL_DEPENDENCY/RETRY_SCHEDULED and distinguish temporary unavailability from not-found.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_INTEGRATION_GATEWAY-H07
        title: Define bounded retries, exponential backoff, deadlines/TTL, circuit breaker, dead-letter and manual-review escalation.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_INTEGRATION_GATEWAY-H08
        title: Define backpressure/resource-queue behavior while domain owners retain transactional concurrency decisions.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_INTEGRATION_GATEWAY-H09
        title: Define observability projections without becoming operational event truth.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_INTEGRATION_GATEWAY-H10
        title: Remain PAUSED until concrete runtime traffic and portfolio approval demonstrate shared Gateway value.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
      - sequence: 11
        step_id: FORPRINT_INTEGRATION_GATEWAY-H11
        title: >-
          Define transport correlation between Gateway delivery attempts and Process Manager process/event identities without merging their state machines.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 12
        step_id: FORPRINT_INTEGRATION_GATEWAY-H12
        title: >-
          Keep Gateway retry/dead-letter decisions transport-scoped while business waiting, deadline and escalation truth remains in the hosted Process Manager capability.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
  forprint_identity_access_service:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Shared identity/authentication/authorization/access service
    module_value_test: KEEP
    inventory_state: CONFIRMED_NEW_MODULE_NOT_IMPLEMENTED
    dependencies_or_inputs: &id003
      - forprint_operations_control_registry
      - forprint_system_administration
    owns:
      - account_identity
      - authentication_factors
      - session_and_device_state
      - role_and_permission_policy
      - per_user_permission_override
      - account_recovery
      - access_decision_audit
      - shared_sso_boundary
      - security_authentication_audit
    must_not_own:
      - crm_relationship_truth
      - accounting_truth
      - operational_order_truth
      - external_provider_credentials
      - canonical_business_partner_relationship_truth
      - business_domain_authority
    target_state:
      agreed_or_recovered:
        - One shared identity/access capability; roles + user overrides; deny-by-default cross-client access.
      synthetic_or_proposed:
        - Sessions/devices/recovery/MFA/passkeys/SSO/admin access-review.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H01
        title: Reconcile the new IAM concept against current module identity, CRM business-person and SysAdmin security boundaries.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H02
        title: Confirm ownership of technical accounts/auth/session/authorization while CRM retains business person/customer relationships.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H03
        title: Complete self-inventory for account IDs, sessions, devices, roles, permissions, overrides, recovery and audit.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H04
        title: Define account_id to CRM person_id linkage and separate selected business context from authenticated technical identity.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id003
      - sequence: 5
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H05
        title: Define deny-by-default authorization, role baselines and per-user overrides with auditable access decisions.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H06
        title: Plan modern password hashing, MFA/passkeys, recovery and device/session controls.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H07
        title: Define SSO/shared-client boundary for web, mobile, Telegram/admin clients without duplicating business context.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H08
        title: Separate external partner credentials into centralized SysAdmin secrets infrastructure with least privilege and rotation.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H09
        title: Define admin access-review UI, security audit evidence and revocation/recovery procedures.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_IDENTITY_ACCESS_SERVICE-H10
        title: Keep module unimplemented until portfolio roadmap, SysAdmin and operational dependencies are approved.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id003
  forprint_library:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Canonical semantic/catalog/reference and shared UI publication authority
    module_value_test: KEEP
    inventory_state: OWNER_DIRECTION_CLEAR
    dependencies_or_inputs: &id004
      - forprint_contract_registry
    owns:
      - product_catalog_semantics
      - service_catalog_semantics
      - material_catalog_semantics
      - operation_catalog_semantics
      - aliases
      - templates
      - technical_cards
      - contract_definitions
      - ui_design_system_publication
      - shared_ui_component_catalog
      - ui_component_version_and_adoption_metadata
    must_not_own:
      - operational_orders
      - client_database
      - accounting_truth
      - production_runtime
      - crm_workflow
      - domain_business_rules_outside_library_semantics
    target_state:
      agreed_or_recovered:
        - Canonical products/materials/services/operations/aliases/profiles; shared UI package publication.
      synthetic_or_proposed:
        - Fast capability/semantic discovery and mature version/adoption lifecycle.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_LIBRARY-H01
        title: Reconcile current Library catalog, alias, template, naming-profile and UI publication evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_LIBRARY-H02
        title: Confirm Library ownership of product/material/service/operation semantics and shared UI publication, excluding business workflows.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_LIBRARY-H03
        title: Complete capability/self-inventory for canonical IDs, aliases, misspellings, production tokens, templates and technical cards.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_LIBRARY-H04
        title: Define versioned naming/profile/default semantics consumed by Calculator, Prepress and operations surfaces.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id004
      - sequence: 5
        step_id: FORPRINT_LIBRARY-H05
        title: Define material/product/service canonical identifiers and stable lookup contracts for Warehouse and other consumers.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_LIBRARY-H06
        title: 'Define UI design-system package lifecycle: lookup, proposal, prototype, Inspector review, operator approval, publish and adoption.'
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_LIBRARY-H07
        title: Add version/adoption metadata and compatibility rules without creating live global CSS or uncontrolled defaults.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_LIBRARY-H08
        title: Plan fast capability/semantic discovery while keeping retrieval candidate-only and domain-owner truth authoritative.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_LIBRARY-H09
        title: Define deprecation/migration paths for legacy aliases/profiles and evidence requirements for consumer adoption.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_LIBRARY-H10
        title: Hold broader implementation until Contract Registry and consumer readiness are reconciled in the portfolio.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id004
      - sequence: 11
        step_id: FORPRINT_LIBRARY-H11
        title: >-
          Define stable historical/reference asset metadata semantics including asset ID, source module, entity links, revision references, media type and provenance.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 12
        step_id: FORPRINT_LIBRARY-H12
        title: >-
          Define the boundary between Library-owned canonical reference media and customer/order/production assets owned by operational domains.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
  forprint_marketing_orchestrator:
    identity_state: CANONICAL
    strategic_priority: P3
    role: Brand, campaign and content operations orchestration with human-governed publication.
    module_value_test: KEEP
    inventory_state: NON_BLOCKING_FUTURE
    dependencies_or_inputs:
      - forprint_crm
      - website
      - forprint_library
      - forprint_accounting_registry_service
    owns:
      - marketing_content_plan
      - campaign_content_workflow
      - creative_brief
      - marketing_asset_review_context
      - campaign_performance_view
    must_not_own:
      - canonical_customer_history
      - sales_pipeline_truth
      - accounting_truth
      - unapproved_external_publication
    target_state:
      agreed_or_recovered:
        - Campaign/content planning and human-reviewed publication without becoming CRM.
        - Marketing Orchestrator is a distinct Brand & Content Operations capability, not merely a post generator and not CRM/customer truth.
      synthetic_or_proposed:
        - Multi-channel automation, AI creative routing, cost/performance learning and lead handoff.
        - Mature capability may orchestrate cross-channel campaigns, AI creative routing, brand-character consistency, reuse, analytics and bounded low-risk auto-publication.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H01
        title: Reconcile Marketing Orchestrator as brand/content operations distinct from CRM and Website ownership.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H02
        title: Confirm product/customer/accounting truth always comes from domain owners.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H03
        title: Define brand system, tone, visual rules and Brand Character Bible for persistent mascot/spokescharacter consistency.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H04
        title: Define website visual/content audit and handoff with Website/Prepress/Library.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H05
        title: Define multi-channel campaign plan, editorial calendar and reusable content asset lifecycle.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H06
        title: Define short-form image/video/content generation with provider abstraction, centralized secrets and cost budgets.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H07
        title: Define publication maturity DRAFT_ONLY → HUMAN_APPROVAL_REQUIRED → bounded low-risk auto-publish.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H08
        title: Define provenance, rollback and audit for all external publication.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H09
        title: Define campaign performance learning as advisory proposals and CRM lead/conversion handoff without duplicate customer history.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_MARKETING_ORCHESTRATOR-H10
        title: Remain non-blocking/future until core operations mature and operator explicitly approves activation.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  forprint_operations_assistant:
    identity_state: CANONICAL
    strategic_priority: P1
    role: Low-friction human entry point for guided operational and bounded technical assistance.
    module_value_test: KEEP
    inventory_state: FIRST_PASS_DIRECTION_RECORDED
    dependencies_or_inputs:
      - forprint_library
      - forprint_operations_control_registry
      - forprint_identity_access_service
      - forprint_system_administration
    owns:
      - operations_assistant_interaction_context
      - guided_form_interaction
      - knowledge_help_surface
      - operational_observation_capture
    must_not_own:
      - accounting_truth
      - canonical_order_registry
      - canonical_catalog_truth
      - crm_customer_pipeline
      - unbounded_business_decision_authority
    target_state:
      agreed_or_recovered:
        - Procedures/guided forms/Job Ticket assistance/physical observations.
        - Operations Assistant is a human entry surface and may route technical requests to SysAdmin without becoming technical-system authority.
      synthetic_or_proposed:
        - Role-aware training, visual SOPs, reprint/exception capture, bounded operational AI.
        - Mature capability may support voice/mobile/Telegram entry, fuzzy intent resolution, role-aware SOPs and bounded tool invocation.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H01
        title: Reconcile shop-floor assistant, SOP, guided form, Job Ticket and technical-help entry responsibilities.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H02
        title: Confirm Operations Assistant owns interaction context, not operational/order/accounting/technical platform truth.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H03
        title: Define role-aware guided forms, SOP discovery and visual instruction flows.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H04
        title: Define voice/mobile/Telegram entry as optional interfaces to the same bounded interaction model.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H05
        title: Define fuzzy intent/entity resolution with deterministic confirmation before sensitive action.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H06
        title: Define routing of technical requests to SysAdmin capabilities and business requests to domain owners.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H07
        title: Define IAM-aware capability checks and Execution Policy Gate before any tool side effect.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H08
        title: Define low-friction reprint/exception/observation capture with provenance.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H09
        title: Define bounded operational AI with repeat/hop/budget/manual-review limits.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_OPERATIONS_ASSISTANT-H10
        title: Keep autonomous high-impact action disabled until Verification Lab and portfolio gates pass.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  forprint_operations_control_registry:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Canonical operational party/order/task/control registry and write boundary
    module_value_test: KEEP
    inventory_state: FOUNDATION_EXISTS_DEEP_REVIEW_REQUIRED
    dependencies_or_inputs: &id005
      - calculator_engine
      - forprint_contract_registry
      - forprint_library
    owns:
      - internal_forprint_db
      - client_account_records
      - client_group_records
      - operational_orders
      - customer_requests
      - operational_events
      - operational_tasks
      - operational_blockers
      - logistics_addresses
      - stable_business_partner_reference_boundary
      - stable_order_identity_boundary
    must_not_own:
      - calculator_logic
      - canonical_catalog_semantics
      - one_c_adapter_logic
      - crm_dashboard
      - customer_channel_runtime
      - physical_postgresql_platform_operations
    target_state:
      agreed_or_recovered:
        - Operational orders/requests/events/tasks/blockers and stable shared party/order IDs.
      synthetic_or_proposed:
        - Mature operational lifecycle, Job Ticket state, reservations/obligations and resilient commands/events.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H01
        title: "Reconcile operational order/request/task/event/party concepts, historical aliases, and the historical Operational Registry → canonical Operations Control Registry repository/layout mapping while preserving immutable historical provenance."
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H02
        title: "Confirm stable operational identities and the authorized operational-truth/write boundary for clients/orders/jobs/tasks/status/events, with explicit Accounting/CRM/Library/Warehouse/Logistics/Prepress exclusions and no foreign-domain semantic absorption."
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H03
        title: "Complete current-worktree self-inventory for business-partner references, order IDs, requests, tasks, blockers, incidents, deadlines and current documentation/status; classify the persistent core separately from next-generation foundations."
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H04
        title: "Define the canonical operational order/Job Ticket lifecycle, including explicit HOLD, priority, proof, reprint and exception states; reconcile OrderRecord versus OperationalOrder generation while separating order, workflow/process, production, payment-fact/projection and dictionary/reference status axes."
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id005
      - sequence: 5
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H05
        title: "Define obligations, requirements, reservations, shortages and execution-context contracts with Warehouse, Accounting, Logistics and Prepress, preserving each domain's truth and making inbound fact/reference directions explicit."
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H06
        title: "Define command/query and event-contract boundaries plus outbox/inbox/idempotency/correlation rules for resilient cross-module interactions; once the project interaction-role taxonomy is canonical, distinguish semantic/domain ownership from message direction and transport/runtime state."
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H07
        title: "Define stable business-partner/person/organization/customer/billing/delivery identity and reference boundaries across Operations, CRM, IAM, Accounting and Logistics while preserving historical relationships, before promoting the rich ClientAccount foundation to canonical truth."
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H08
        title: Define read/write interfaces used by CRM and channels without transferring ownership of operational truth.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H09
        title: Plan reporting projections and exception/event evidence for dashboards without making read models authoritative.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H10
        title: Hold expanded execution until Calculator/Library/Contract Registry producer dependencies and portfolio gates are ready.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id005
      - sequence: 11
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H11
        title: >-
          Define the operational historical-asset link contract connecting asset references to order ID, job ID, revision and authoritative operational state.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 12
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H12
        title: >-
          Define explicit current/superseded/production-result and approval-related revision evidence required by historical asset consumers.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 13
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H13
        title: >-
          Expose operational revision/status projections for historical retrieval without transferring operational truth into the search/index layer.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 14
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H14
        title: >-
          Define the hosted Process Manager namespace and durable process-instance identity/state model inside Operations Control Registry.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 15
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H15
        title: >-
          Define current-step, waiting-condition, expected-event, timer, deadline, retry, escalation and transition semantics for long-running processes.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 16
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H16
        title: >-
          Define an append-only process transition/event ledger with correlation, idempotency, restart recovery and deterministic resume semantics.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 17
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H17
        title: >-
          Define operator-attention and authorized human-decision integration without letting unattended workflow state silently authorize foreign-domain actions.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 18
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H18
        title: >-
          Define domain adapters so CRM, Telegram, Logistics and other modules can observe or participate through typed process intents/events without owning the durable process instance.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 19
        step_id: FORPRINT_OPERATIONS_CONTROL_REGISTRY-H19
        title: >-
          Add explicit extraction-readiness criteria so the capability can later move to a standalone Process Manager service if scale, topology or ownership evidence justifies separation.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
  forprint_prepress_hub:
    identity_state: CANONICAL
    strategic_priority: P1
    role: Prepress/file preparation and production-readiness evidence
    module_value_test: KEEP
    inventory_state: FIRST_PASS_DIRECTION_RECORDED
    dependencies_or_inputs: &id006
      - calculator_engine
      - forprint_library
      - forprint_contract_registry
    owns:
      - prepress_file_readiness
      - prepress_requirements
      - prepress_blockers
      - station_preset_policy
      - hotfolder_direction
    must_not_own:
      - calculator_logic
      - accounting_truth
      - operational_order_registry
      - canonical_catalog_truth
      - crm_workflow
    target_state:
      agreed_or_recovered:
        - PDF/document probe and readiness evidence consuming Calculator + Library.
      synthetic_or_proposed:
        - Preflight/normalization/imposition/profile/hot-folder and future metadata projections.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_PREPRESS_HUB-H01
        title: Reconcile current PDF/document probe, readiness and prepress planning evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_PREPRESS_HUB-H02
        title: Confirm Prepress ownership of file preparation/readiness evidence, not Calculator logic, catalog truth or device identity.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_PREPRESS_HUB-H03
        title: Complete self-inventory for probes, requirements, blockers, corrections, profiles, imposition and production-package outputs.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_PREPRESS_HUB-H04
        title: Define consumption of accepted Calculator Job Spec and Library naming/material/profile contracts.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id006
      - sequence: 5
        step_id: FORPRINT_PREPRESS_HUB-H05
        title: Specify deterministic PDF validation/correction boundaries; ambiguous semantic repair must escalate rather than guess.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_PREPRESS_HUB-H06
        title: Plan imposition, normalization and production profile selection with explicit evidence and reproducible fixtures.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_PREPRESS_HUB-H07
        title: Define hot-folder/station preset policy while concrete device identity/capability remains SysAdmin-owned.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_PREPRESS_HUB-H08
        title: Define HOLD/reject/readiness evidence and handoff to operational Job Ticket/QC flows.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_PREPRESS_HUB-H09
        title: Plan production-file provenance and future metadata projections without making filenames the source of truth.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_PREPRESS_HUB-H10
        title: Hold implementation expansion until Calculator, Library and Contract Registry dependencies are accepted.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id006
      - sequence: 11
        step_id: FORPRINT_PREPRESS_HUB-H11
        title: >-
          Define a machine-readable technical Asset Fact Packet containing deterministic file facts, source revision, hashes and safe preview references.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 12
        step_id: FORPRINT_PREPRESS_HUB-H12
        title: >-
          Define deterministic fingerprint/probe outputs suitable for downstream candidate retrieval while keeping semantic match decisions outside Prepress.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 13
        step_id: FORPRINT_PREPRESS_HUB-H13
        title: >-
          Define historical-file provenance and master-versus-derived relationships without making Prepress the raw archive or historical search owner.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
  forprint_project_inspector:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Read-only structural, semantic, cleanliness, architecture and governance conformance verification.
    module_value_test: KEEP
    inventory_state: STRONG_DIRECTION
    dependencies_or_inputs:
      - forprint_system_blueprint
      - forprint_contract_registry
    owns:
      - project_structure_verification
      - module_makefile_standard_audit
      - coordination_metadata_audit
      - module_readiness_summary
      - cross_module_advisory_reports
      - module_self_inventory_conformance
      - duplicate_capability_detection
      - shared_ui_conformance
      - repository_cleanliness_audit
      - document_surface_conformance_audit
      - generated_surface_drift_detection
    must_not_own:
      - architecture_policy
      - module_business_logic
      - production_runtime_control
      - operational_order_truth
      - accounting_truth
      - warehouse_stock_truth
      - live_integrations
      - ui_design_system_semantics
      - capability_ownership_decision
      - foreign_module_semantic_rewrite
    target_state:
      agreed_or_recovered:
        - Detects drift/contradictions/ownership violations; never invents domain truth.
        - Project Inspector detects drift/conflicts/duplication candidates but never invents or activates domain truth.
      synthetic_or_proposed:
        - Self-inventory health, duplicate-capability detection, UI conformance, bounded semantic review.
        - Mature Inspector should verify dev/runtime boundary, module maturity, autonomy evidence and intake Verification Lab findings as conformance evidence.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_PROJECT_INSPECTOR-H01
        title: Reconcile Project Inspector scope against Blueprint, Runtime Inspector and Verification Lab.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_PROJECT_INSPECTOR-H02
        title: Confirm Inspector is read-only conformance authority and not an adversarial test executor or domain owner.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_PROJECT_INSPECTOR-H03
        title: 'Define deterministic checks first: schema, generators, indexes, ownership, cleanliness and contract adoption.'
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_PROJECT_INSPECTOR-H04
        title: Define duplicate/equivalent-capability candidate detection with owner-reviewed dispositions and no auto-delete.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_PROJECT_INSPECTOR-H05
        title: Define module current-state, roadmap, maturity M0-M9 and dependency-constrained readiness conformance.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_PROJECT_INSPECTOR-H06
        title: Define DEV/VERIFICATION/RELEASE/RUNTIME separation and immutable-runtime conformance checks.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_PROJECT_INSPECTOR-H07
        title: Define bounded semantic review after deterministic evidence with stable finding taxonomy.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_PROJECT_INSPECTOR-H08
        title: Define periodic/risk-triggered review and checkpoint-to-commit evidence packages.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_PROJECT_INSPECTOR-H09
        title: Ingest Verification Lab results as evidence while leaving intentional test generation to Verification Lab.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_PROJECT_INSPECTOR-H10
        title: Keep foreign-repo mutation, truth activation and autonomous deletion forbidden.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  forprint_strategic_control_plane:
    identity_state: CANONICAL
    strategic_priority: P3
    role: Long-horizon business decision intelligence, scenario analysis and strategy-memory plane.
    module_value_test: KEEP
    inventory_state: NON_BLOCKING_FUTURE
    dependencies_or_inputs:
      - forprint_system_blueprint
      - forprint_crm
      - forprint_accounting_registry_service
      - forprint_operations_control_registry
      - warehouse_service
      - production_runtime_inspector
    owns:
      - strategic_control_policy
      - ecosystem_status_aggregation
      - priority_control_rules
      - future_control_plane_workflows
    must_not_own:
      - runtime_orchestration_now
      - business_workflow_runtime_now
      - production_automation_now
      - accounting_posting
      - operational_db
    target_state:
      agreed_or_recovered:
        - Tracks goals/priorities and challenges stale direction without overriding Blueprint/operator.
        - Strategic Control Plane supports long-horizon quantified human decisions rather than acting as an autonomous strategic executor.
      synthetic_or_proposed:
        - Scenario analysis, strategic KPI aggregation and advisory loops.
        - Mature capability should maintain strategic objectives/KPIs, economics/capacity/market intelligence, scenarios, investment cases and forecast→decision→actual memory.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H01
        title: Reconcile Strategic Control Plane as decision intelligence, not dashboard duplication or operational control.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H02
        title: Confirm strategic recommendations remain human decisions and do not directly mutate operational truth.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H03
        title: Define strategic objectives registry and structured KPI catalog with provenance.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H04
        title: Define product/customer economics, capacity, bottleneck and investment evidence inputs from domain owners.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H05
        title: Define external market/search/competitor intelligence as sourced evidence, never invented fact.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H06
        title: Define scenario engine with assumptions, uncertainty, risk and sensitivity.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H07
        title: Define investment cases and measurable expected return/capacity/quality effects.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H08
        title: Define strategy memory linking forecast → recommendation → human decision → actual outcome.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H09
        title: Define monthly refresh, quarterly deep review, annual rebaseline and event-triggered recalculation cadence.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_STRATEGIC_CONTROL_PLANE-H10
        title: Keep autonomous execution forbidden; mature output is quantified options and evidence for operator decisions.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  forprint_system_administration:
    identity_state: CANONICAL
    strategic_priority: P1
    role: Recovery-first technical operations, device, endpoint, data-platform, secrets and offline-continuity administration.
    module_value_test: KEEP
    inventory_state: FIRST_PASS_DIRECTION_RECORDED
    dependencies_or_inputs:
      - cloud_backup_manager
      - forprint_project_inspector
      - forprint_operations_assistant
      - forprint_identity_access_service
    owns:
      - administration_portal
      - approved_software_catalog
      - endpoint_operation_contract
      - workstation_profile
      - administrative_health_view
      - postgresql_platform_operations
      - centralized_secrets_infrastructure
      - database_role_and_credential_operations
      - backup_restore_pitr
    must_not_own:
      - business_workflow
      - accounting_truth
      - canonical_order_registry
      - arbitrary_remote_shell_authority
      - license_entitlement_outside_authorized_policy
      - domain_schema_semantics
      - business_data_write_policy
    target_state:
      agreed_or_recovered:
        - Workstation/admin surface plus physical PostgreSQL and secrets-platform operations.
        - SysAdmin is the recovery-first technical operations helper and may integrate with voice/mobile/Telegram through bounded interfaces.
      synthetic_or_proposed:
        - Fleet onboarding, device capability inventory, backup/PITR, health and operational-readiness gates.
        - Mature SysAdmin should manage known-good endpoint state, software/driver lifecycle, recovery artifacts, diagnostics and bounded technical actions with offline continuity.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H01
        title: Reconcile device, endpoint, PostgreSQL, secrets, backup and recovery responsibilities into one technical-operations boundary.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H02
        title: Confirm SysAdmin owns technical platform/device administration but not business workflow or domain semantics.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H03
        title: Define stable device inventory, discovery and capability evidence distinct from concrete job assignment.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H04
        title: Define known-good workstation/device configuration profiles and drift evidence.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H05
        title: Define corporate software/workspace/plugin deployment packs while domain owners retain semantic ownership of business resources.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H06
        title: Define stable/pinned driver lifecycle, rollback and compatibility evidence rather than uncontrolled latest-driver upgrades.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H07
        title: Define recovery images/snapshots, offline artifact bank and restore procedures with measurable evidence.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H08
        title: Integrate Operations Assistant/voice/Telegram as human entry surfaces to bounded SysAdmin capabilities.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H09
        title: Define diagnostics and approved-manual troubleshooting with no invented repair procedures or arbitrary shell authority.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_SYSTEM_ADMINISTRATION-H10
        title: Hold broad autonomous IT actions until IAM, Execution Policy Gate, Verification Lab and operator approval criteria are satisfied.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  forprint_system_blueprint:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Portfolio architecture, ownership, governance, roadmap/dependency balancing and release/distribution gate authority.
    module_value_test: KEEP
    inventory_state: STRONG_EXISTING_FOUNDATION
    dependencies_or_inputs:
      - forprint_project_inspector
      - forprint_contract_registry
      - verification_lab
    owns:
      - architecture_policy
      - module_boundaries
      - execution_queue
      - coordination_standards
      - module_policy
      - module_source_registry
      - coordination_metadata_tools
      - project_cleanliness_governance
      - document_type_registry
      - surface_normalization_program
    must_not_own:
      - runtime_business_logic
      - production_order_processing
      - accounting_posting
      - customer_channel_runtime
      - foreign_module_business_semantics_during_normalization
    target_state:
      agreed_or_recovered:
        - Global architecture, boundaries, standards, Human Intent, dependency/readiness balance.
        - Blueprint must formalize managed autonomy, Verification Lab, development/runtime separation and a common module maturity path before future distribution.
      synthetic_or_proposed:
        - Stronger automated portfolio health/decision-support projections.
        - Mature Blueprint should reduce human control to a small number of portfolio/exception/approval surfaces while preserving explicit high-impact authority.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H01
        title: Integrate u92 architecture decisions into Human Intent, canonical portfolio roadmaps and governance without opening implementation.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H02
        title: Promote Verification Lab to canonical module identity while Semantic Retrieval remains proposed/noncanonical.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H03
        title: Formalize DEV → VERIFICATION → RELEASE → RUNTIME separation and immutable-runtime/self-evolution rules.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H04
        title: Formalize M0-M9 module maturity and production-entry sequence for all future modules.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H05
        title: Formalize shared resource concurrency/availability states, retry/backpressure/dead-letter semantics.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H06
        title: Formalize Execution Policy Gate, capability-shaped tools and risk-class authorization.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H07
        title: Formalize managed-autonomy levels, context checkpoint/handoff and AI budget-runway evidence.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H08
        title: Strengthen dependency-constrained readiness and assistant-distribution prerequisites using the 23-module canonical set.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H09
        title: Require Verification Lab and Project Inspector evidence before production promotion while keeping their roles separate.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H10
        title: Keep assistant distribution, module implementation, H10 widening and automatic acceptance closed until explicit operator approval.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
      - sequence: 11
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H11
        title: >-
          Define the cross-module Historical Asset Index contract over Library reference semantics, Prepress technical asset facts and Operations Control Registry order/job/revision state.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 12
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H12
        title: >-
          Define candidate retrieval stages as cheap scoped retrieval followed by deeper comparison of a small candidate set and explicit human/customer selection when ambiguity remains.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 13
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H13
        title: >-
          Resolve the final hosted-capability location only after comparing an existing-host implementation with the noncanonical Semantic Retrieval module candidate.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 14
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H14
        title: >-
          Govern the hosted Process Manager boundary so process truth, domain truth, transport state and human-facing workflow UI remain explicitly separated.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 15
        step_id: FORPRINT_SYSTEM_BLUEPRINT-H15
        title: >-
          Review extraction triggers after real usage evidence, including independent scaling, availability, topology, ownership pressure and cross-domain coupling.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
  logistics_service:
    identity_state: CANONICAL
    strategic_priority: P1
    role: Provider-neutral shipment/pickup/delivery/tracking truth
    module_value_test: KEEP
    inventory_state: IMPLEMENTATION_EXISTS_RUNTIME_SCOPE_GATED
    dependencies_or_inputs: &id007
      - forprint_operations_control_registry
      - forprint_accounting_registry_service
      - forprint_identity_access_service
    owns: []
    must_not_own: []
    target_state:
      agreed_or_recovered:
        - Provider adapters, shipment drafts/tracking/events; current H10 sole automation pilot.
      synthetic_or_proposed:
        - Mature carrier/taxi/courier adapters, evidence handoff, delivery exceptions and bounded automation.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: LOGISTICS_SERVICE-H01
        title: Reconcile Logistics provider-neutral shipment/pickup/delivery/tracking model and existing H10 pilot evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: LOGISTICS_SERVICE-H02
        title: Confirm Logistics truth boundaries against OCR operational identities, Accounting costs and IAM access.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: LOGISTICS_SERVICE-H03
        title: Complete self-inventory for shipment drafts, provider adapters, tracking events, delivery evidence and exceptions.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: LOGISTICS_SERVICE-H04
        title: Define stable shipment/order/address references and provider-neutral command/response contracts.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id007
      - sequence: 5
        step_id: LOGISTICS_SERVICE-H05
        title: Define carrier/taxi/courier adapter boundary, secrets usage, retries, idempotency and correlation.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: LOGISTICS_SERVICE-H06
        title: Define pickup/delivery/tracking event lifecycle plus evidence for failures, cancellation and manual takeover.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: LOGISTICS_SERVICE-H07
        title: Define cost/charge handoff to Accounting without making Logistics accounting authority.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: LOGISTICS_SERVICE-H08
        title: Define delivery exception and escalation workflows with Telegram/operator attention but no hidden auto-decisions.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: LOGISTICS_SERVICE-H09
        title: Evaluate the existing Logistics-only H10 automation pilot against cost, quality, retry and operator-intervention evidence.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: LOGISTICS_SERVICE-H10
        title: Do not widen H10 or authorize other modules until the pilot and full portfolio are explicitly approved.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id007
      - sequence: 11
        step_id: LOGISTICS_SERVICE-H11
        title: >-
          Define the boundary between Logistics shipment lifecycle state and a parent or linked cross-domain Process Manager instance.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 12
        step_id: LOGISTICS_SERVICE-H12
        title: >-
          Expose typed shipment events, waiting conditions and outcomes to Process Manager without transferring carrier/provider truth out of Logistics.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
  mobile_app:
    identity_state: CANONICAL
    strategic_priority: P2
    role: Deferred native mobile customer/staff channel that reuses shared domain contracts.
    module_value_test: KEEP
    inventory_state: DEFERRED
    dependencies_or_inputs:
      - calculator_engine
      - forprint_identity_access_service
      - forprint_integration_gateway
      - forprint_crm
      - forprint_library
    owns:
      - mobile_customer_channel_future
    must_not_own:
      - calculator_logic
      - operational_db
      - accounting_truth
      - catalog_truth
      - crm_workflow
    target_state:
      agreed_or_recovered:
        - Deferred until Calculator/Identity/API contracts mature.
        - Native mobile implementation remains paused until customer scale and native-only value justify it.
      synthetic_or_proposed:
        - Secure mobile self-service over the same domain contracts as web.
        - Mature native app may provide fast calculation, orders, push, camera/QR and offline non-authoritative cache over shared APIs.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: MOBILE_APP-H01
        title: Keep Mobile App in PAUSED/PROPOSED planning state and define measurable activation triggers.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: MOBILE_APP-H02
        title: Use responsive/mobile-first web and shared Customer Portal capabilities as the present customer-mobile baseline.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: MOBILE_APP-H03
        title: Define future native client as a channel only, with no local domain-truth ownership.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: MOBILE_APP-H04
        title: Define IAM/session/device security and shared selected business-context behavior before native implementation.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: MOBILE_APP-H05
        title: Plan fast Calculator and basket/order composition over the same contracts used by web.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: MOBILE_APP-H06
        title: Define offline cache/estimate behavior as non-authoritative and requiring server revalidation before commitment.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: MOBILE_APP-H07
        title: Plan push notifications and customer confirmations through audited shared messaging/event contracts.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: MOBILE_APP-H08
        title: Plan camera, QR and file-upload capabilities without making QR a permission mechanism.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: MOBILE_APP-H09
        title: Plan unified conversation/history through shared CRM/communication services rather than mobile-only shadow state.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: MOBILE_APP-H10
        title: Authorize native implementation only after usage, client-base and native-value evidence clears the portfolio gate.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  production_runtime_inspector:
    identity_state: CANONICAL
    strategic_priority: P1
    role: Runtime execution evidence, actuals, device-used, queue/retry/health and AI/tool-cost telemetry observer.
    module_value_test: KEEP
    inventory_state: DEEP_REVIEW_REQUIRED
    dependencies_or_inputs:
      - forprint_operations_control_registry
      - forprint_system_administration
      - forprint_library
    owns: []
    must_not_own: []
    target_state:
      agreed_or_recovered:
        - Records concrete device and actuals without silently rewriting approved norms.
        - Runtime Inspector records facts and actuals but never silently rewrites approved norms.
      synthetic_or_proposed:
        - Operation actuals, quality/variance signals, telemetry and norm-change proposals.
        - Mature runtime inspection should trace retries, waiting states, dead letters, AI/tool usage, latency, cost and deployment/canary evidence.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H01
        title: Reconcile runtime execution, device-used and actuals evidence scope.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H02
        title: Confirm Runtime Inspector observes facts but owns neither approved norms nor architecture policy.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H03
        title: Define end-to-end request/job trace identifiers across queue, tool, AI and external dependencies.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H04
        title: Define WAITING/RETRY/DEGRADED/dead-letter/stuck-work evidence and detection.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H05
        title: 'Define AI/tool telemetry: calls, repetitions, tokens, latency, cost, retries and escalation counts.'
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H06
        title: Define budget-runway and abnormal-cost signals without autonomously changing business strategy.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H07
        title: Define actual-vs-standard variance evidence and proposal-only norm-change feedback.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H08
        title: Define deployment/shadow/canary runtime evidence consumed by Verification Lab and release decisions.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H09
        title: 'Define privacy/retention boundaries: execution evidence, not hidden chain-of-thought capture.'
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: PRODUCTION_RUNTIME_INSPECTOR-H10
        title: Hold any active control-loop behavior until bounded autonomy and portfolio gates are explicitly approved.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  telegram_bot:
    identity_state: CANONICAL
    strategic_priority: P1
    role: Conversational customer/staff channel adapter
    module_value_test: KEEP
    inventory_state: ACTIVE_HISTORY_NEW_EXECUTION_HELD
    dependencies_or_inputs: &id008
      - calculator_engine
      - forprint_crm
      - forprint_identity_access_service
      - forprint_integration_gateway
    owns:
      - telegram_channel_adapter
      - telegram_dialog_flow
      - telegram_message_ui
      - telegram_user_interaction_shell
    must_not_own:
      - canonical_client_registry
      - canonical_order_registry
      - calculator_logic
      - accounting_truth
      - operational_db
      - catalog_truth
    target_state:
      agreed_or_recovered:
        - Structured request/response channel without owning CRM/order/accounting truth.
      synthetic_or_proposed:
        - Voice transcription, supplier enrichment, richer self-service, future TTS/voice.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: TELEGRAM_BOT-H01
        title: Reconcile current Telegram channel flows, identity/context handling and historical execution evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: TELEGRAM_BOT-H02
        title: Confirm Telegram as channel adapter only, never canonical CRM/order/calculation/accounting/catalog truth.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: TELEGRAM_BOT-H03
        title: Complete self-inventory for dialog flow, message UI, uploads, confirmations and channel context.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: TELEGRAM_BOT-H04
        title: Define authentication/linkage through IAM and visible customer/billing/business context selection.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id008
      - sequence: 5
        step_id: TELEGRAM_BOT-H05
        title: Define structured calculation/order request handoff to Calculator/OCR with audited confirmations.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: TELEGRAM_BOT-H06
        title: Define file/status/payment/delivery views as domain-owned read projections with clear freshness/provenance.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: TELEGRAM_BOT-H07
        title: Define context switching without duplicate CRM persons/orders and without phone becoming immutable identity.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: TELEGRAM_BOT-H08
        title: Plan voice transcription and richer interaction as bounded channel capabilities with fallback and operator visibility.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: TELEGRAM_BOT-H09
        title: Define retry/idempotency/correlation and anti-loop budgets for channel-to-domain interactions.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: TELEGRAM_BOT-H10
        title: Hold new execution until IAM, Gateway/contract and portfolio readiness gates are approved.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id008
      - sequence: 11
        step_id: TELEGRAM_BOT-H11
        title: Define personalized communication orchestration with conversation continuity, approved communication preferences and strict presentation-versus-facts separation.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 12
        step_id: TELEGRAM_BOT-H12
        title: >-
          Define channel-neutral inbound structured domain requests/events and outbound structured communication intents with correlation and provenance.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 13
        step_id: TELEGRAM_BOT-H13
        title: >-
          Define consumption of customer-specific communication context without moving canonical customer profile, commercial policy or analytics into Telegram.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 14
        step_id: TELEGRAM_BOT-H14
        title: >-
          Define bounded clarification and structured Order Draft interaction using canonical Library/Calculator/domain constraints.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 15
        step_id: TELEGRAM_BOT-H15
        title: Define deterministic-to-context-to-AI-to-human escalation with replaceable model/provider slots and progress/contradiction based escalation.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 16
        step_id: TELEGRAM_BOT-H16
        title: >-
          Define Telegram consumption of historical customer asset retrieval results without live archive scanning or asset-index ownership.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
      - sequence: 17
        step_id: TELEGRAM_BOT-H17
        title: >-
          Define Telegram as a communication participant for durable long-running business processes while process state/timers/deadlines/transitions remain with the eventual canonical Process Manager owner.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: operator_confirmed_evening_architecture_20260919
        execution_authority: false
        dependency_gate: []
  warehouse_service:
    identity_state: CANONICAL
    strategic_priority: P1
    role: Physical inventory/material-location truth and movement service
    module_value_test: KEEP
    inventory_state: DEEP_REVIEW_REQUIRED
    dependencies_or_inputs: &id009
      - forprint_library
      - forprint_operations_control_registry
      - forprint_accounting_registry_service
    owns: []
    must_not_own: []
    target_state:
      agreed_or_recovered:
        - Physical stock fact distinct from accounting valuation and Calculator planned need.
      synthetic_or_proposed:
        - Reservations, receipts/issues/writeoffs, locations, shortages, cycle count, traceable reprint consumption.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: WAREHOUSE_SERVICE-H01
        title: Reconcile warehouse stock, location, movement, material and defect/reprint evidence.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: current_evidence_reconciliation
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: WAREHOUSE_SERVICE-H02
        title: Confirm Warehouse ownership of physical inventory truth distinct from accounting valuation and Calculator planned consumption.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: ownership_and_role_boundary
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: WAREHOUSE_SERVICE-H03
        title: Complete self-inventory for stock facts, locations, lots, movements, reservations, shortages and counts.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: self_inventory_requirement
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: WAREHOUSE_SERVICE-H04
        title: Bind all stock/material records to Library canonical material IDs and controlled alias resolution.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: dependency_and_contract_planning
        execution_authority: false
        dependency_gate: *id009
      - sequence: 5
        step_id: WAREHOUSE_SERVICE-H05
        title: Define receipts, issues, transfers, writeoffs and reservations against stable operational order/job references.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: WAREHOUSE_SERVICE-H06
        title: Define shortage and availability contracts for Calculator/OCR without letting Warehouse decide pricing or production rules.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: WAREHOUSE_SERVICE-H07
        title: Define internal-defect/reprint material consumption as traceable physical movements with reason/evidence.
        approval_state: AGREED_OR_RECOVERED_TARGET
        source_basis: agreed_or_recovered_target_state
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: WAREHOUSE_SERVICE-H08
        title: Plan cycle counts, discrepancy workflows and audit trails with explicit human resolution.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: WAREHOUSE_SERVICE-H09
        title: Define Accounting handoff for valuation/documents while retaining physical quantity/location truth.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: proposed_mature_target
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: WAREHOUSE_SERVICE-H10
        title: Hold automation until Library, operational registry and accounting contracts are accepted.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: *id009
  website:
    identity_state: CANONICAL
    strategic_priority: P2
    role: Public web presence, SEO entry point and conversion router; not a business-truth owner.
    module_value_test: KEEP
    inventory_state: FIRST_PASS_DIRECTION_RECORDED
    dependencies_or_inputs:
      - calculator_engine
      - forprint_identity_access_service
      - forprint_library
      - forprint_operations_control_registry
      - forprint_crm
    owns:
      - website_customer_channel
    must_not_own:
      - calculator_logic
      - operational_db
      - accounting_truth
      - catalog_truth
    target_state:
      agreed_or_recovered:
        - Must not duplicate Calculator/catalog/order truth; legacy surface needs controlled reconciliation.
        - Website is the public façade and SEO entry point, not authentication, pricing, payment, cart or canonical order truth.
      synthetic_or_proposed:
        - Modern self-service, account/order/calculation/files/payment/delivery views.
        - Mature public web should maximize organic discovery and route customers into shared Calculator and Customer Portal/domain workflows.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: WEBSITE-H01
        title: Reconcile Website strictly as public façade, SEO entry point and service discovery surface.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: WEBSITE-H02
        title: Confirm Website owns no authentication, price truth, payment truth, basket truth or canonical order state.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: WEBSITE-H03
        title: Define explicit routing from public service/product pages into Calculator, design tools and Customer Portal workflows.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: WEBSITE-H04
        title: Define crawl/index hygiene, canonical URLs, sitemap, robots and structured-data rules.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: WEBSITE-H05
        title: Define mobile-first performance and Core Web Vitals targets without duplicating native-app functionality.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: WEBSITE-H06
        title: Define service/product landing semantics from Library/Calculator truth with no local shadow catalog.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: WEBSITE-H07
        title: Define Search Console, analytics, conversion and query-to-order measurement with privacy-aware evidence.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: WEBSITE-H08
        title: Plan content freshness, internal linking and authority-building as governed marketing/website collaboration.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: WEBSITE-H09
        title: Plan organic-query → landing → calculation → customer-workflow optimization with measurable funnel evidence.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: WEBSITE-H10
        title: Keep business logic external and implementation deferred until required shared contracts are portfolio-ready.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
  verification_lab:
    identity_state: CANONICAL
    strategic_priority: P0
    role: Independent verification, adversarial testing, fault-injection and deterministic regression evidence module.
    module_value_test: KEEP
    inventory_state: CONFIRMED_NEW_MODULE_NOT_IMPLEMENTED
    dependencies_or_inputs:
      - forprint_system_blueprint
      - forprint_contract_registry
      - forprint_project_inspector
      - forprint_system_administration
    owns:
      - verification_campaign_definition
      - synthetic_test_case_corpus
      - test_plane_scenario
      - adversarial_test_execution
      - deterministic_regression_corpus
      - verification_finding_evidence
      - release_candidate_verification_result
      - fault_injection_profile
    must_not_own:
      - architecture_policy
      - business_domain_truth
      - production_runtime_control
      - deployment_approval
      - live_external_side_effects
      - unrestricted_shell_authority
      - secrets
      - foreign_module_semantic_rewrite
    target_state:
      agreed_or_recovered:
        - Verification Lab is a distinct canonical module that intentionally tries to prove the system wrong before customers or incidents do.
      synthetic_or_proposed:
        - Mature Verification Lab should support black/gray/white-box Test Plane campaigns, adversarial/fault/concurrency testing, deterministic regression and release-gate evidence with synthetic side effects only.
    roadmap_status: PLANNING_ONLY_NOT_DISTRIBUTED
    steps:
      - sequence: 1
        step_id: VERIFICATION_LAB-H01
        title: Establish Verification Lab canonical identity, charter and strict separation from Project Inspector and Runtime Inspector.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: VERIFICATION_LAB-H02
        title: Define BLACK_BOX, GRAY_BOX and WHITE_BOX read-only diagnostic modes and their evidence boundaries.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: VERIFICATION_LAB-H03
        title: Define Test Plane isolation with fake/synthetic payment, courier, printer, email, cloud, Telegram and database side effects.
        approval_state: AGREED_PLANNING_DIRECTION
        source_basis: u92_owner_confirmed_architecture_direction
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: VERIFICATION_LAB-H04
        title: Define normal/invalid/boundary/malformed/combinatorial/multilingual/out-of-domain/auth/data-isolation test taxonomy.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: VERIFICATION_LAB-H05
        title: Define prompt-adversarial, tool-misuse, state-machine, concurrency, idempotency, stale-cache and schema-fuzz campaigns.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: VERIFICATION_LAB-H06
        title: Define fault/recovery, timeout, unavailable-resource, retry/dead-letter, load/performance and cost-regression campaigns.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: VERIFICATION_LAB-H07
        title: Convert useful AI-discovered failures into owner-confirmed deterministic regression corpus rather than permanent stochastic-only tests.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: VERIFICATION_LAB-H08
        title: Define change-triggered, nightly, weekly, manual, pre-release and post-release verification campaign policy.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: VERIFICATION_LAB-H09
        title: Define trace-aware evaluation of intermediate contract/tool/state behavior, not only final user-visible answer.
        approval_state: PROPOSED_TARGET_REFINEMENT
        source_basis: u92_mature_target_synthesis_for_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: VERIFICATION_LAB-H10
        title: Remain planning-only until Test Plane, Execution Policy Gate, IAM and explicit operator distribution/implementation approval are ready.
        approval_state: HOLD_FOR_FINAL_PORTFOLIO_APPROVAL
        source_basis: operator_distribution_gate
        execution_authority: false
        dependency_gate: []
proposed_noncanonical_modules:
  forprint_semantic_retrieval_service:
    identity_state: PROPOSED_NONCANONICAL_REVIEW_ONLY
    roadmap_status: REVIEW_ONLY_DO_NOT_DISTRIBUTE
    module_value_test: REVIEW_BEFORE_PROMOTION
    human_intent_count: 9
    steps:
      - sequence: 1
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R01
        title: Reconcile the proposed semantic retrieval concept against Library, Inspector, CRM search and Blueprint capability boundaries.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 2
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R02
        title: Run module-necessity/value test before any canonical promotion.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 3
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R03
        title: 'Define candidate-only retrieval semantics: retrieval finds candidates; domain owner decides truth.'
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 4
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R04
        title: Define source/index provenance, freshness and access-control requirements.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 5
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R05
        title: Define bounded indexing/query interfaces without creating a second semantic authority.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 6
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R06
        title: Define evaluation datasets and precision/recall acceptance evidence for realistic project queries.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 7
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R07
        title: Define permission-aware retrieval and prevention of cross-domain data leakage.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 8
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R08
        title: Compare implementation cost/complexity against simpler indexed lookup/search capabilities.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 9
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R09
        title: Choose PROMOTE, MERGE or RETIRE as an explicit portfolio decision.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
      - sequence: 10
        step_id: FORPRINT_SEMANTIC_RETRIEVAL_SERVICE-R10
        title: If promoted, only then create canonical identity, ownership policy, dependencies and implementation roadmap.
        approval_state: REVIEW_ONLY_PROPOSED_NONCANONICAL
        source_basis: module_value_and_boundary_review
        execution_authority: false
        dependency_gate: []
project_cleanliness_conformance:
  status: ACTIVE_PORTFOLIO_REQUIREMENT
  single_policy_point: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
  policy_owner: forprint_system_blueprint
  cross_repository_auditor: forprint_project_inspector
  module_local_cleanliness_owner: each_module_owner
  blueprint_automation_status: IMPLEMENTED
  blueprint_automation_evidence:
    - coordination/standards/governance/document_type_registry_v0_1.yaml
    - scripts/validation/validate_document_surface_registry_v0_1.py
    - make surface-normalization-check
    - make check
  inspector_cross_repository_automation_status: PLANNED_NOT_IMPLEMENTED
  other_module_local_pack_status: REQUIRED_PLANNED_NOT_STARTED
  required_before_future_assistant_distribution: true
  required_before_module_maturity: true
  no_duplicate_global_cleanliness_standards: true
  modules:
    calculator_engine:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    cloud_backup_manager:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_accounting_registry_service:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_contract_registry:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_crm:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_integration_gateway:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_identity_access_service:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_library:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_marketing_orchestrator:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_operations_assistant:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_operations_control_registry:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_prepress_hub:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_project_inspector:
      status: PLANNED_LOCAL_PACK_PLUS_CROSS_REPO_AUDITOR
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: plan module-local cleanliness pack and future bounded cross-repository audit pack
    forprint_strategic_control_plane:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_system_administration:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    forprint_system_blueprint:
      status: IMPLEMENTED_BLUEPRINT_LOCAL_CORE
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: continue class-by-class normalization and keep automated checks green
    logistics_service:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    mobile_app:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    production_runtime_inspector:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    telegram_bot:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    warehouse_service:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
    website:
      status: REQUIRED_PLANNED_MODULE_LOCAL_PACK
      policy_ref: coordination/standards/governance/project_cleanliness_and_machine_surface_normalization_standard_v0_1.md
      local_repository_owner_responsible: true
      parallel_global_standard_allowed: false
      assistant_distribution_authorized: false
      implementation_authorized: false
      next_action: record local cleanliness inventory/check roadmap before future assistant distribution
```

### BLUEPRINT CONTEXT â€” coordination/roadmaps/details/forprint_system_blueprint/portfolio_rebuild_inputs/2026-08-27__forprint_accounting_registry_service__revision1_owner_review_v0_1.md

`SHA256=919e285c5a2785c39b3c646ad1e1bbe911921385f75eb5b96fb2fe17f9f39275`

```md
# Accounting Registry Revision-1 Owner Review — Rebuild Input — 2026-08-27

Status: AGREED OWNER/THEORY INPUT; READY FOR DEEP DECOMPOSITION; NOT EXECUTION AUTHORITY.

## Accounting Registry Service — Revision 1 Owner Notes

Status: `REVISION_1_DISCUSSED`
Next: `TARGET_DIRECTION_CLEAR_READY_FOR_DEEP_DECOMPOSITION`

### Strategic role — AGREED_WITH_OWNER

Build ForPrint's own operational/commercial accounting registry and gradually move daily business work away from dependence on 1C.

Initial target is not full statutory/tax accounting.

Core scope:
- goods/material movement;
- purchases;
- sales;
- invoices;
- payments;
- settlements;
- write-offs;
- management reporting;
- document state;
- reconciliation.

### 1C relationship — AGREED_WITH_OWNER

Accountants will continue using 1C for statutory/reporting needs.

ForPrint needs connectors/import-export/synchronization so accountants can see the relevant live picture without repeating operational work manually.

Expected exchanged classes:
- payments;
- purchases;
- sales;
- goods movement;
- material write-offs;
- invoices / accounting-document data.

Long-term direction:
ForPrint's own registry becomes the primary operational commercial system.
1C remains a compatibility/downstream accounting environment as long as needed.

### Functional benchmark — AGREED_WITH_OWNER direction

Use useful 1C management/commercial-accounting capabilities as a benchmark, but do not copy 1C architecture or poor UX blindly.

The next deep decomposition should identify the closest functional 1C scope for:
- management/commercial accounting;
- sales/purchases;
- warehouse;
- money/payments;
- settlements;
- production/business analytics;
without making statutory accounting the initial core.

### Candidate capability families — SYNTHETIC_CANDIDATE

- counterparties and financial attributes;
- orders/invoices/realization;
- procurement and goods receipt;
- payments and settlements;
- goods/material movement;
- planned/actual write-offs;
- returns/corrections;
- cost and financial result;
- document lifecycle;
- reconciliation;
- 1C import/export/sync;
- management reports;
- exception workflows.

### Warehouse boundary — PROVISIONAL_BOUNDARY

Warehouse owns physical fact:
- what;
- how much;
- where physically.

Accounting Registry owns:
- documentary/accounting movement;
- financial value;
- accounting state;
- reconciliation records.

A mismatch between system stock and physical stock is a reconciliation incident, not permission for silent competing truths.

### Calculator boundary — PROVISIONAL_BOUNDARY

Calculator provides:
- planned materials;
- planned technical waste;
- calculated price;
- structured order/commercial specification.

Actual consumption must remain distinguishable from planned consumption.

### Human involvement — AGREED_WITH_OWNER

Normal workflow should be highly automated.

Human is needed mainly for:
- physical vs system stock conflict;
- ambiguous mapping;
- unresolved reconciliation;
- exceptional correction;
- other cases where automatic facts cannot be trusted.

Fast exception handling should later be possible through UI and potentially a governed Telegram admin/emergency channel.

### 1C sync authority — OPEN_QUESTION

Must later define:
- what flows ForPrint -> 1C automatically;
- what, if anything, may flow back;
- conflict rules;
- duplicate prevention;
- idempotency;
- whether 1C may ever override canonical operational state.

Working preference:
ForPrint is operational authority; 1C is primarily downstream for accountant/statutory needs.

### Stabilization — AGREED_WITH_OWNER direction

Accounting needs a longer proving period than Calculator.

Candidate:
one or two quarters of stable operation after tuning.

Metrics should be class-specific:
- money reconciles essentially exactly;
- documents are not lost/duplicated;
- payment posting is reliable;
- 1C exchange is idempotent;
- material/accounting discrepancies are controlled and visible;
- manual corrections are rare and auditable.

### Remaining gray zones

- exact Warehouse/Accounting contract;
- exact Calculator planned-vs-actual flow;
- 1C sync/conflict rules;
- canonical accounting entity model;
- report scope;
- correction/reversal/reconciliation lifecycle.
```

### BLUEPRINT CONTEXT â€” coordination/roadmaps/details/forprint_system_blueprint/portfolio_rebuild_seeds/forprint_accounting_registry_service.yaml

`SHA256=9cc382436c7df2a11568a950cbe013989762c797d642b97c1679edb1780063e4`

```yaml
schema_version: forprint_portfolio_roadmap_rebuild_seed_v0_1
module_id: forprint_accounting_registry_service
role_summary: accounting/1C boundary and registry
status: PROVISIONAL_SYNTHETIC_REBUILD_SEED_NOT_AUTHORITY
authority: provisional_planning_input_not_release_or_execution_authority
source_action: rebuild_needed_owner_review_priority
note: This is a rebuild process seed, not a claim that the module's business delivery roadmap is fully known. Existing
  policy/prompts/code/roadmaps must be reconciled before execution.
steps:
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-01
    title: Reconcile current evidence and canonical module identity
    work_weight: 5
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-02
    title: Complete Module Charter and ownership boundaries
    work_weight: 5
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-03
    title: Build/repair Capability Catalog and target finish state
    work_weight: 10
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-04
    title: Map current implementation/evidence to capabilities
    work_weight: 10
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-05
    title: Build full delivery roadmap from current state to target
    work_weight: 20
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-06
    title: Perform end-to-end completeness and gray-zone review
    work_weight: 20
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-07
    title: Map dependencies, contracts and dependency timing
    work_weight: 20
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-08
    title: Assign weights, portfolio value and blocking class
    work_weight: 10
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-09
    title: Create baseline progress assessment and confidence
    work_weight: 10
    status: planned
    confidence: low
  - step_id: FP-ACCOUNTING-REGISTRY-SERVICE-10
    title: Semantic review and publish execution-ready roadmap
    work_weight: 10
    status: planned
    confidence: low
```

### BLUEPRINT CONTEXT â€” machine/data_objects.yaml

`SHA256=8c84d9eb1276d3091699766210f48a7ebd5affb8ea490c2ad4b9093be673cde7`

```yaml
schema_version: forprint_machine_data_objects_v0_1
status: CURRENT_MACHINE_AUTHORITY
authority: forprint_system_blueprint
data_objects:
  - id: architecture_decision
    owner: forprint_system_blueprint
    description: Архітектурне рішення, яке впливає на побудову системи.
    canonical_fields:
      - adr_id
      - title
      - status
      - date
      - context
      - decision
      - consequences
  - id: module_definition
    owner: forprint_system_blueprint
    description: Канонічний опис модуля в архітектурі ForPrint.
    canonical_fields:
      - module_id
      - title
      - type
      - status
      - role
      - owns
      - consumes
      - provides
      - must_not_own
  - id: data_flow_definition
    owner: forprint_system_blueprint
    description: Опис потоку даних між модулями.
    canonical_fields:
      - flow_id
      - source
      - target
      - data_objects
      - contract
      - status
      - criticality
  - id: contract_definition
    owner: forprint_system_blueprint
    description: Опис контракту між модулями.
    canonical_fields:
      - contract_id
      - provider
      - consumer
      - version
      - data_objects
      - status
  - id: impact_rule
    owner: forprint_system_blueprint
    description: Правило визначення модулів, яких зачіпає зміна об'єкта або контракту.
    canonical_fields:
      - rule_id
      - when_changed
      - notify_modules
      - required_actions
  - id: module_guide
    owner: forprint_system_blueprint
    description: Людський guide / prompt для окремого модуля.
    canonical_fields:
      - module_id
      - role
      - allowed_responsibilities
      - forbidden_responsibilities
      - contracts
      - open_questions
  - id: mermaid_diagram
    owner: forprint_system_blueprint
    description: Автоматично або напівавтоматично згенерована Mermaid-діаграма.
    canonical_fields:
      - diagram_id
      - source_yaml
      - generated_at
      - content
  - id: architecture_change_prompt
    owner: forprint_system_blueprint
    description: Промт / завдання для модуля після зміни архітектури.
    canonical_fields:
      - prompt_id
      - target_modules
      - reason
      - source_change
      - requested_actions
      - status
  - id: module_manifest
    owner: forprint_project_inspector
    description: Файл декларації реального модуля, який порівнюється з Blueprint.
    canonical_fields:
      - module_id
      - implemented_contracts
      - provided_objects
      - consumed_objects
      - status
  - id: module_status_report
    owner: forprint_project_inspector
    description: Звіт модуля про стан реалізації.
    canonical_fields:
      - module_id
      - progress_summary
      - tests
      - integration_contracts
      - open_questions
  - id: inspection_report
    owner: forprint_project_inspector
    description: Результат перевірки модуля або групи модулів.
    canonical_fields:
      - inspection_id
      - module_id
      - result
      - findings
      - recommendations
  - id: architecture_health_report
    owner: forprint_project_inspector
    description: Загальний звіт про стан архітектурного здоров'я системи.
    canonical_fields:
      - report_id
      - checked_at
      - ok_modules
      - warning_modules
      - critical_modules
      - gaps
  - id: integration_gap_report
    owner: forprint_project_inspector
    description: Звіт про невідповідність або відсутній інтеграційний контракт.
    canonical_fields:
      - gap_id
      - source_module
      - target_module
      - expected_contract
      - actual_state
  - id: runtime_health_event
    owner: production_runtime_inspector
    description: Подія здоров'я живої продакшен-системи.
    canonical_fields:
      - event_id
      - module_id
      - severity
      - message
      - detected_at
  - id: production_health_report
    owner: production_runtime_inspector
    description: Звіт про стан живої системи.
    canonical_fields:
      - report_id
      - generated_at
      - incidents
      - degraded_modules
      - recommendations
  - id: crm_dashboard_view
    owner: forprint_crm
    description: Представлення даних для людського інтерфейсу CRM.
    canonical_fields:
      - view_id
      - user_role
      - widgets
      - filters
      - source_modules
  - id: business_workflow_state
    owner: forprint_crm
    description: Робочий стан бізнес-процесу на рівні диригування.
    canonical_fields:
      - workflow_id
      - related_order_id
      - current_step
      - responsible_module
      - next_actions
  - id: management_report
    owner: forprint_crm
    description: Управлінський звіт для людини.
    canonical_fields:
      - report_id
      - period
      - metrics
      - risks
      - recommendations
  - id: business_command
    owner: forprint_crm
    description: Команда, яку CRM надсилає предметному модулю.
    canonical_fields:
      - command_id
      - target_module
      - action
      - payload
      - created_by
      - status
  - id: human_dashboard
    owner: forprint_crm
    description: Людський dashboard для перегляду стану бізнесу або архітектури.
    canonical_fields:
      - dashboard_id
      - title
      - sections
      - source_reports
  - id: workflow_decision
    owner: forprint_crm
    description: Рішення в бізнес-процесі, яке направляє подальші дії.
    canonical_fields:
      - decision_id
      - workflow_id
      - selected_option
      - reason
      - created_at
  - id: client
    owner: forprint_operations_control_registry
    description: Клієнт або організація, яка замовляє продукт.
    canonical_fields:
      - client_id
      - name
      - contact_channels
      - status
      - created_at
  - id: order
    owner: forprint_operations_control_registry
    description: Підтверджене або робоче замовлення.
    canonical_fields:
      - order_id
      - client_id
      - status
      - items
      - total_amount
      - created_at
  - id: client_interaction
    owner: forprint_operations_control_registry
    description: Історія взаємодії з клієнтом.
    canonical_fields:
      - interaction_id
      - client_id
      - channel
      - message_summary
      - created_at
  - id: order_status_history
    owner: forprint_operations_control_registry
    description: Історія зміни статусів замовлення.
    canonical_fields:
      - event_id
      - order_id
      - old_status
      - new_status
      - changed_at
      - reason
  - id: order_context
    owner: forprint_operations_control_registry
    description: Контекст замовлення для інших модулів.
    canonical_fields:
      - order_id
      - client_id
      - product_configuration
      - current_status
      - linked_files
  - id: client_history
    owner: forprint_operations_control_registry
    description: Агрегована історія клієнта.
    canonical_fields:
      - client_id
      - orders
      - interactions
      - financial_summary
  - id: client_context
    owner: forprint_operations_control_registry
    description: Мінімальний контекст клієнта для розрахунків, сайту або бота.
    canonical_fields:
      - client_id
      - client_type
      - pricing_profile
      - communication_preferences
  - id: material_catalog
    owner: forprint_library
    description: Канонічний каталог матеріалів.
    canonical_fields:
      - material_id
      - name
      - category
      - thickness
      - density
      - compatible_machines
      - status
  - id: product_catalog
    owner: forprint_library
    description: Каталог продуктів / рекламно-інформаційних виробів.
    canonical_fields:
      - product_id
      - name
      - category
      - configurable_options
      - status
  - id: machine_capability
    owner: forprint_library
    description: Можливості обладнання, режими, обмеження, сумісність.
    canonical_fields:
      - machine_id
      - capability_id
      - supported_materials
      - max_size
      - print_modes
  - id: print_mode
    owner: forprint_library
    description: Режим друку або виробничої операції.
    canonical_fields:
      - mode_id
      - name
      - machine_id
      - quality_profile
      - constraints
  - id: document_template
    owner: forprint_library
    description: Шаблон документа, бланку або звіту.
    canonical_fields:
      - template_id
      - title
      - version
      - status
      - file_ref
  - id: technical_card
    owner: forprint_library
    description: Технічна карта виконання продукту або операції.
    canonical_fields:
      - technical_card_id
      - product_id
      - steps
      - materials
      - machine_modes
  - id: quote_draft
    owner: calculator_engine
    description: Попередній розрахунок вартості.
    canonical_fields:
      - quote_id
      - client_id
      - product_configuration
      - price
      - material_consumption
      - validity_period
  - id: price_breakdown
    owner: calculator_engine
    description: Деталізація ціни.
    canonical_fields:
      - quote_id
      - components
      - margin
      - discounts
      - total
  - id: material_consumption_estimate
    owner: calculator_engine
    description: Оцінка витрат матеріалів для замовлення або кошторису.
    canonical_fields:
      - estimate_id
      - quote_id
      - material_id
      - quantity
      - unit
      - waste_percent
  - id: product_configuration
    owner: calculator_engine
    description: Обрана конфігурація продукту для розрахунку.
    canonical_fields:
      - configuration_id
      - product_id
      - options
      - quantities
      - constraints
  - id: prepress_file
    owner: forprint_prepress_hub
    description: Вхідний файл клієнта або робочий файл для додрукарської підготовки.
    canonical_fields:
      - file_id
      - order_id
      - source
      - file_type
      - checksum
      - status
  - id: prepress_report
    owner: forprint_prepress_hub
    description: Результат аналізу файлу.
    canonical_fields:
      - report_id
      - file_id
      - readiness
      - issues
      - recommended_actions
  - id: print_ready_file
    owner: forprint_prepress_hub
    description: Файл, підготовлений до друку.
    canonical_fields:
      - file_id
      - order_id
      - output_profile
      - checksum
      - generated_at
  - id: file_preview
    owner: forprint_prepress_hub
    description: Прев'ю результату обробки файлу.
    canonical_fields:
      - preview_id
      - file_id
      - image_ref
      - generated_at
  - id: invoice
    owner: forprint_accounting_registry_service
    description: Рахунок на оплату.
    canonical_fields:
      - invoice_id
      - order_id
      - client_id
      - amount
      - status
      - issued_at
  - id: payment_status
    owner: forprint_accounting_registry_service
    description: Стан оплати.
    canonical_fields:
      - payment_id
      - invoice_id
      - order_id
      - amount
      - status
      - paid_at
  - id: accounting_document
    owner: forprint_accounting_registry_service
    description: Акт, видаткова, бухгалтерський документ або інший фінансовий запис.
    canonical_fields:
      - document_id
      - document_type
      - order_id
      - client_id
      - status
      - external_ref
  - id: one_c_sync_event
    owner: forprint_accounting_registry_service
    description: Подія експорту або синхронізації з 1С.
    canonical_fields:
      - event_id
      - external_system
      - entity_type
      - entity_id
      - status
      - error_message
  - id: accounting_export
    owner: forprint_accounting_registry_service
    description: Експортований пакет даних для бухгалтерії або 1С.
    canonical_fields:
      - export_id
      - format
      - period
      - file_ref
      - generated_at
  - id: telegram_dialog_state
    owner: telegram_bot
    description: Стан діалогу з клієнтом у Telegram.
    canonical_fields:
      - chat_id
      - client_id
      - current_step
      - last_intent
      - updated_at
  - id: bot_action_log
    owner: telegram_bot
    description: Лог дій, які ініціював Telegram Bot.
    canonical_fields:
      - action_id
      - chat_id
      - action
      - target_module
      - status
      - created_at
  - id: client_request
    owner: telegram_bot
    description: Запит клієнта, прийнятий через Telegram.
    canonical_fields:
      - request_id
      - client_id
      - raw_text
      - detected_intent
      - created_at
  - id: workflow_command
    owner: telegram_bot
    description: Команда робочого сценарію, ініційована ботом.
    canonical_fields:
      - command_id
      - target_module
      - scenario
      - payload
      - confidence
  - id: ai_assisted_task_request
    owner: telegram_bot
    description: Запит до AI для нестандартної задачі через дозволені інструменти бота.
    canonical_fields:
      - task_id
      - context
      - requested_action
      - allowed_tools
      - safety_limits
  - id: website_content
    owner: website
    description: Контент сайту.
    canonical_fields:
      - content_id
      - page
      - title
      - body
      - status
  - id: public_product_page
    owner: website
    description: Публічна сторінка продукту.
    canonical_fields:
      - page_id
      - product_id
      - seo_title
      - content
      - status
  - id: website_request
    owner: website
    description: Запит, отриманий через сайт.
    canonical_fields:
      - request_id
      - client_id
      - form_type
      - payload
      - created_at
  - id: material_stock
    owner: warehouse_service
    description: Залишок матеріалу на складі.
    canonical_fields:
      - stock_id
      - material_id
      - location
      - quantity
      - unit
      - updated_at
  - id: material_reservation
    owner: warehouse_service
    description: Резерв матеріалу під замовлення.
    canonical_fields:
      - reservation_id
      - order_id
      - material_id
      - quantity
      - status
  - id: inventory_movement
    owner: warehouse_service
    description: Рух матеріалу на складі.
    canonical_fields:
      - movement_id
      - material_id
      - quantity
      - movement_type
      - reason
      - created_at
  - id: purchase_request
    owner: warehouse_service
    description: Заявка на закупівлю матеріалу.
    canonical_fields:
      - request_id
      - material_id
      - requested_quantity
      - reason
      - status
  - id: inventory_availability_report
    owner: warehouse_service
    description: Звіт про доступність матеріалів.
    canonical_fields:
      - report_id
      - generated_at
      - items
      - risks
  - id: delivery_request
    owner: logistics_service
    description: Запит на доставку.
    canonical_fields:
      - delivery_id
      - order_id
      - provider
      - destination
      - package_description
      - status
  - id: delivery_status
    owner: logistics_service
    description: Статус доставки.
    canonical_fields:
      - delivery_id
      - provider
      - status
      - tracking_number
      - updated_at
  - id: logistics_provider_adapter
    owner: logistics_service
    description: Адаптер до Нової пошти, Укрпошти, таксі або кур'єра.
    canonical_fields:
      - adapter_id
      - provider
      - capabilities
      - auth_profile
      - status
  - id: delivery_label
    owner: logistics_service
    description: Етикетка / ТТН / документ доставки.
    canonical_fields:
      - label_id
      - delivery_id
      - file_ref
      - generated_at
  - id: delivery_cost_estimate
    owner: logistics_service
    description: Попередня оцінка вартості доставки.
    canonical_fields:
      - estimate_id
      - provider
      - package_description
      - cost
      - currency
  - id: package_description
    owner: logistics_service
    description: Опис пакування для доставки; у майбутньому може перейти в окремий packaging module.
    canonical_fields:
      - package_id
      - order_id
      - dimensions
      - weight
      - fragility
      - notes
  - id: backup_plan
    owner: cloud_backup_manager
    description: План резервного копіювання.
    canonical_fields:
      - plan_id
      - sources
      - targets
      - schedule
      - retention
  - id: backup_snapshot
    owner: cloud_backup_manager
    description: Конкретний backup-знімок.
    canonical_fields:
      - snapshot_id
      - plan_id
      - created_at
      - size
      - checksum
      - target
  - id: backup_inventory
    owner: cloud_backup_manager
    description: Інвентаризація наявних backup-знімків.
    canonical_fields:
      - inventory_id
      - target
      - snapshots
      - generated_at
  - id: backup_source_descriptor
    owner: cloud_backup_manager
    description: Опис джерела, яке треба резервувати.
    canonical_fields:
      - source_id
      - path
      - type
      - priority
      - include_rules
      - exclude_rules
  - id: backup_status_report
    owner: cloud_backup_manager
    description: Звіт про стан резервного копіювання.
    canonical_fields:
      - report_id
      - generated_at
      - ok_targets
      - failed_targets
      - warnings
  - id: integration_request
    owner: forprint_integration_gateway
    description: Уніфікований вхідний запит між модулями або з зовнішнього інтерфейсу.
    canonical_fields:
      - request_id
      - source_module
      - target_capability
      - contract_id
      - payload
      - correlation_id
      - idempotency_key
      - created_at
  - id: routed_module_request
    owner: forprint_integration_gateway
    description: Запит, який пройшов валідацію і готовий до передачі конкретному модулю.
    canonical_fields:
      - request_id
      - source_module
      - target_module
      - target_action
      - validated_payload
      - correlation_id
      - route_id
  - id: integration_response
    owner: forprint_integration_gateway
    description: Стандартизована відповідь на міжмодульний запит.
    canonical_fields:
      - response_id
      - request_id
      - status
      - result_payload
      - error_code
      - correlation_id
      - created_at
  - id: validation_error
    owner: forprint_integration_gateway
    description: Помилка валідації запиту до передачі в цільовий модуль.
    canonical_fields:
      - error_id
      - request_id
      - field
      - message
      - severity
      - suggested_action
  - id: routing_rule
    owner: forprint_integration_gateway
    description: Правило маршрутизації запиту до потрібного модуля або capability.
    canonical_fields:
      - route_id
      - source_module
      - target_module
      - contract_id
      - condition
      - status
  - id: correlation_context
    owner: forprint_integration_gateway
    description: Контекст трасування одного бізнес-сценарію через кілька модулів.
    canonical_fields:
      - correlation_id
      - root_request_id
      - related_requests
      - created_at
      - status
  - id: idempotency_record
    owner: forprint_integration_gateway
    description: Запис для захисту від повторного виконання одного і того самого запиту.
    canonical_fields:
      - idempotency_key
      - request_hash
      - first_seen_at
      - last_result_ref
      - status
  - id: integration_audit_event
    owner: forprint_integration_gateway
    description: Аудит-подія маршрутизації, відмови, повтору або помилки інтеграційного шару.
    canonical_fields:
      - event_id
      - request_id
      - source_module
      - target_module
      - event_type
      - severity
      - created_at
  - id: security_filter_event
    owner: forprint_integration_gateway
    description: 'Подія захисного фільтра: підозрілий payload, injection-like input, rate-limit або заблокований запит.'
    canonical_fields:
      - event_id
      - request_id
      - source_module
      - risk_type
      - action_taken
      - created_at
```

### BLUEPRINT CONTEXT â€” machine/modules.yaml

`SHA256=f38886cc0e49960726788d968f7f30c5bcdb83d369f93702f6c4bc1cc3e319f6`

```yaml
schema_version: forprint_machine_modules_v0_1
status: CURRENT_MACHINE_AUTHORITY
authority: forprint_system_blueprint
modules:
  - id: forprint_system_blueprint
    title: ForPrint System Blueprint
    type: architecture_truth_layer
    status: active_development
    role: 'Верхній шар архітектурної правди: модулі, межі, дані, контракти, потоки, правила впливу змін, module guides.'
    owns:
      - architecture_decision
      - module_definition
      - data_flow_definition
      - contract_definition
      - impact_rule
    consumes: []
    provides:
      - module_guide
      - mermaid_diagram
      - architecture_change_prompt
    must_not_own:
      - client
      - order
      - invoice
      - material_stock
  - id: forprint_project_inspector
    title: ForPrint Project Inspector
    type: architecture_compliance_checker
    status: planned
    role: 'Перевіряє відповідність реальних модулів Blueprint: manifests, reports, контракти, інтеграційні розриви, architecture
      drift.'
    owns:
      - inspection_report
    consumes:
      - module_definition
      - contract_definition
      - data_flow_definition
      - module_manifest
      - module_status_report
    provides:
      - architecture_health_report
      - integration_gap_report
    must_not_own:
      - module_definition
      - client
      - order
  - id: production_runtime_inspector
    title: ForPrint Production Runtime Inspector
    type: production_monitoring
    status: future
    role: 'Майбутній інспектор продакшену: контроль живої системи, помилок, деградацій, проблем інтеграції, runtime-подій.'
    owns:
      - runtime_health_event
    consumes:
      - architecture_health_report
      - module_status_report
    provides:
      - production_health_report
    must_not_own:
      - architecture_decision
  - id: forprint_integration_gateway
    title: ForPrint Integration Gateway
    type: integration_gateway_and_message_router
    status: planned
    role: 'Транспортно-контрактний шар між модулями: приймає запити, перевіряє їх за контрактами, нормалізує payload, додає
      correlation/idempotency context, маршрутизує до цільових модулів і повертає стандартизовані відповіді або помилки. Не
      приймає бізнес-рішень і не володіє предметними даними.'
    owns:
      - integration_request
      - routed_module_request
      - integration_response
      - validation_error
      - routing_rule
      - correlation_context
      - idempotency_record
      - integration_audit_event
      - security_filter_event
    consumes:
      - contract_definition
      - data_flow_definition
      - website_request
      - client_request
      - workflow_command
      - business_command
      - quote_draft
      - price_breakdown
      - material_consumption_estimate
    provides:
      - routed_module_request
      - integration_response
      - validation_error
      - integration_audit_event
      - security_filter_event
    must_not_own:
      - client
      - order
      - quote_draft
      - invoice
      - payment_status
      - material_catalog
      - material_stock
      - prepress_file
      - print_ready_file
      - business_workflow_state
  - id: forprint_crm
    title: ForPrint CRM
    type: business_orchestration_ui
    status: planned
    role: Бізнес-диригент, людський інтерфейс, прикладний оркестратор процесів, аналітика, звіти, контроль заявок і статусів.
      Не є фізичним сховищем усіх клієнтів і замовлень.
    owns:
      - crm_dashboard_view
      - business_workflow_state
      - management_report
    consumes:
      - client
      - order
      - quote_draft
      - prepress_report
      - invoice
      - payment_status
      - material_reservation
      - delivery_status
    provides:
      - business_command
      - human_dashboard
      - workflow_decision
    must_not_own:
      - canonical_client_registry
      - canonical_order_registry
      - material_catalog
      - accounting_document
      - print_ready_file
  - id: forprint_operations_control_registry
    title: ForPrint Operations Control Registry
    type: operational_data_registry
    status: planned
    role: 'Канонічний реєстр операційного стану та control-контексту ForPrint: замовлення, взаємодії, робочі статуси, історія
      виконання та авторизований operational write boundary; фізична persistence topology лишається централізованою і не є
      власністю одного модуля.'
    owns:
      - client
      - order
      - client_interaction
      - order_status_history
    consumes:
      - quote_draft
      - prepress_report
      - payment_status
      - delivery_status
    provides:
      - client
      - order
      - order_context
      - client_history
    must_not_own:
      - material_catalog
      - invoice
      - machine_capability
  - id: forprint_library
    title: ForPrint Library
    type: canonical_reference_library
    status: active_development
    role: Джерело правди для довідників, матеріалів, технічних карт, шаблонів документів, номенклатури, режимів друку, машинних
      можливостей.
    owns:
      - material_catalog
      - product_catalog
      - machine_capability
      - print_mode
      - document_template
      - technical_card
    consumes: []
    provides:
      - material_catalog
      - product_catalog
      - machine_capability
      - print_mode
      - document_template
    must_not_own:
      - client
      - order
      - invoice
      - payment_status
  - id: calculator_engine
    title: ForPrint Calculator Engine
    type: calculation_service
    status: active_development
    role: 'Прикладна математика: калькуляції, попередні кошториси, розрахунок вартості, витрат матеріалів, конфігурацій продукту.'
    owns:
      - quote_draft
      - price_breakdown
      - material_consumption_estimate
      - product_configuration
    consumes:
      - material_catalog
      - product_catalog
      - machine_capability
      - print_mode
      - client_context
    provides:
      - quote_draft
      - price_breakdown
      - material_consumption_estimate
    must_not_own:
      - client
      - order
      - invoice
      - payment_status
      - prepress_file
  - id: forprint_prepress_hub
    title: ForPrint Prepress Hub
    type: prepress_file_service
    status: active_development
    role: 'Прийом, аналіз і підготовка файлів до друку: перевірка готовності, автоматична обробка, прев''ю, print-ready файли.'
    owns:
      - prepress_file
      - prepress_report
      - print_ready_file
      - file_preview
    consumes:
      - order_context
      - material_catalog
      - machine_capability
      - print_mode
    provides:
      - prepress_report
      - print_ready_file
      - file_preview
    must_not_own:
      - client
      - invoice
      - material_stock
  - id: forprint_accounting_registry_service
    title: ForPrint Accounting Registry Service
    type: accounting_registry
    status: active_development
    role: 'Бухгалтерський і 1С-сумісний контур: рахунки, оплати, акти, бухгалтерські документи, експорт або синхронізація
      з 1С.'
    owns:
      - invoice
      - payment_status
      - accounting_document
      - one_c_sync_event
    consumes:
      - order
      - client
      - quote_draft
    provides:
      - invoice
      - payment_status
      - accounting_export
    must_not_own:
      - material_catalog
      - prepress_file
      - print_ready_file
  - id: telegram_bot
    title: ForPrint Telegram Bot
    type: client_interface_and_action_runner
    status: active_development
    role: Клієнтський інтерфейс, оператор сценаріїв і AI-assisted виконавець дій через дозволені контракти інших модулів.
      Не є джерелом правди.
    owns:
      - telegram_dialog_state
      - bot_action_log
    consumes:
      - client_context
      - order_context
      - quote_draft
      - prepress_report
      - delivery_status
    provides:
      - client_request
      - workflow_command
      - ai_assisted_task_request
    must_not_own:
      - material_catalog
      - canonical_client_registry
      - canonical_order_registry
      - invoice
      - payment_status
  - id: website
    title: ForPrint Website
    type: public_and_client_web_interface
    status: existing_basic
    role: Публічний сайт і майбутній клієнтський веб-інтерфейс. Має використовувати CRM / registry / calculator / prepress
      через адаптери, а не тримати дубльовану правду.
    owns:
      - website_content
      - public_product_page
    consumes:
      - product_catalog
      - client_context
      - order_context
      - quote_draft
    provides:
      - website_request
    must_not_own:
      - canonical_client_registry
      - canonical_order_registry
      - material_catalog
  - id: warehouse_service
    title: ForPrint Warehouse Service
    type: warehouse_and_inventory_service
    status: planned
    role: 'Склад: залишки, резервування, рух матеріалів, списання, мінімальні залишки, заявки на закупівлю.'
    owns:
      - material_stock
      - material_reservation
      - inventory_movement
      - purchase_request
    consumes:
      - material_catalog
      - order
      - material_consumption_estimate
    provides:
      - material_stock
      - material_reservation
      - inventory_availability_report
    must_not_own:
      - material_catalog
      - invoice
      - client
  - id: logistics_service
    title: ForPrint Logistics Service
    type: delivery_and_logistics_service
    status: planned
    role: 'Доставка і логістика: Нова пошта, Укрпошта, таксі, кур''єри, статуси відправок, інтеграційні ключі і адаптери.'
    owns:
      - delivery_request
      - delivery_status
      - logistics_provider_adapter
    consumes:
      - order
      - client
      - package_description
    provides:
      - delivery_status
      - delivery_label
      - delivery_cost_estimate
    must_not_own:
      - invoice
      - material_catalog
      - order
  - id: cloud_backup_manager
    title: Cloud Backup Manager
    type: backup_service
    status: active_development
    role: 'Резервне копіювання локальних і хмарних даних: бази даних, файли клієнтів, архіви, конфігурації, контроль наявності
      backup-знімків.'
    owns:
      - backup_plan
      - backup_snapshot
      - backup_inventory
    consumes:
      - backup_source_descriptor
    provides:
      - backup_status_report
      - backup_inventory
    must_not_own:
      - client
      - order
      - invoice
  - id: mobile_app
    title: ForPrint Mobile App
    type: customer_channel
    status: deferred_planned
    layer: customer_channels
    priority: deferred_until_calculator_ready
    description: Майбутній мобільний клієнтський канал ForPrint. Поки не бере участі в активній розробці. Розробка стартує
      тільки після повноцінного запуску Calculator Engine.
    owns: []
    consumes: []
    provides: []
    must_not_own: []
  - id: forprint_operations_assistant
    title: ForPrint Operations Assistant
    type: internal_operational_assistant
    status: planned
    role: 'Внутрішній operational assistant: швидкий доступ до процедур, guided forms, knowledge library та структурованого
      збору фізичних операційних спостережень.'
    owns: []
    consumes: []
    provides: []
    must_not_own: []
  - id: forprint_system_administration
    title: ForPrint System Administration
    type: it_workplace_administration
    status: planned
    role: 'Майбутній IT/workplace administration модуль: централізовані approved software, endpoint operations, backups/health
      integration та workstation consistency.'
    owns: []
    consumes: []
    provides: []
    must_not_own: []
  - id: forprint_marketing_orchestrator
    title: ForPrint Marketing Orchestrator
    type: marketing_content_orchestrator
    status: future
    role: Майбутній marketing/content orchestration модуль для campaign planning, social channels, AI media providers та marketing
      analytics.
    owns: []
    consumes: []
    provides: []
    must_not_own: []
```

## Semantic-analysis instruction

Classify evidence into current implemented capability, current policy/intent,
historical/superseded material, partial foundation, contradiction, unknown or
future candidate. Do not turn findings into implementation authority.
