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