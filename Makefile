PYTHON=.venv_accounting_registry/bin/python
PIP=.venv_accounting_registry/bin/pip

.PHONY: install test lint check check-report run health

install:
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check app tests scripts

check: lint test

check-report:
	$(PYTHON) scripts/run_accounting_registry_checks.py

run:
	$(PYTHON) -m uvicorn forprint_accounting_registry_service.main:app --app-dir app --host 0.0.0.0 --port 8015 --reload

health:
	curl http://127.0.0.1:8015/health



# =============================================================================
# ForPrint governance alignment
# =============================================================================

.PHONY: status-report
status-report:
	@echo "== Accounting Registry status report =="
	@mkdir -p reports
	@printf '{\n' > reports/accounting_registry_module_status.json
	@printf '  "module_name": "forprint_accounting_registry_service",\n' >> reports/accounting_registry_module_status.json
	@printf '  "module_status": "active",\n' >> reports/accounting_registry_module_status.json
	@printf '  "current_phase": "governance_alignment_v0_1",\n' >> reports/accounting_registry_module_status.json
	@printf '  "boundary": "sandbox_import_export_only_no_live_1c_write"\n' >> reports/accounting_registry_module_status.json
	@printf '}\n' >> reports/accounting_registry_module_status.json
	@echo "📄 Module status report: reports/accounting_registry_module_status.json"

.PHONY: blueprint-pull
blueprint-pull:
	git -C /srv/software_development/forprint-project/forprint_system_blueprint pull --ff-only

.PHONY: blueprint-check
blueprint-check:
	@test -d /srv/software_development/forprint-project/forprint_system_blueprint/coordination/global_policy
	@test -d /srv/software_development/forprint-project/forprint_system_blueprint/coordination/standards
	@test -f /srv/software_development/forprint-project/forprint_system_blueprint/coordination/module_policy/accounting_registry_service/module_policy.md || \
	 test -f /srv/software_development/forprint-project/forprint_system_blueprint/coordination/module_policy/forprint_accounting_registry_service/module_policy.md || \
	 echo "WARN: Accounting Registry module policy file not found under expected Blueprint paths."
	@echo "✅ Blueprint paths checked."

.PHONY: blueprint-sync-directives
blueprint-sync-directives:
	@echo "DEFERRED: Accounting Registry directive sync is not implemented yet."

.PHONY: coordination-check
coordination-check:
	@test -f coordination/status/current_status.yaml
	@test -f coordination/status/current_status.md
	@test -f coordination/prompts/index.yaml
	@test -f coordination/reports/index.yaml
	@test -f coordination/status/next_questions_for_blueprint.md
	@echo "✅ Coordination files exist."

.PHONY: coordination-fix
coordination-fix:
	@echo "DEFERRED: automatic Accounting Registry coordination fix is not implemented yet."

.PHONY: module-policy-check
module-policy-check: blueprint-check

.PHONY: governance-check
governance-check:
	@echo "== ForPrint Accounting Registry governance check =="
	$(MAKE) blueprint-pull
	$(MAKE) blueprint-check
	$(MAKE) blueprint-sync-directives
	$(MAKE) module-policy-check
	$(MAKE) coordination-check
	$(MAKE) status-report

