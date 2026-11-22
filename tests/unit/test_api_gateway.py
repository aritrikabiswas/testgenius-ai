
from fastapi.testclient import TestClient

from services.api_gateway.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to TestGenius AI"
    assert response.json()["status"] == "running"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["service"] == "testgenius-api-gateway"


def test_database_health_endpoint():
    response = client.get("/health/database")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["database"] == "connected"
    assert response.json()["service"] == "testgenius-postgresql"
