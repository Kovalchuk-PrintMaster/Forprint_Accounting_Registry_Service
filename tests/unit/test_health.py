from fastapi.testclient import TestClient
from forprint_accounting_registry_service.main import app


def test_health_endpoint_returns_service_status() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "forprint_accounting_registry_service"
    assert data["title"] == "ForPrint Accounting Registry Service"
    assert data["version"] == "0.1.0"


def test_openapi_schema_is_available() -> None:
    client = TestClient(app)

    response = client.get("/openapi.json")

    assert response.status_code == 200

    data = response.json()
    assert data["info"]["title"] == "ForPrint Accounting Registry Service"
    assert data["info"]["version"] == "0.1.0"