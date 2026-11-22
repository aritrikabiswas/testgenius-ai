
from fastapi.testclient import TestClient

from services.api_gateway.main import app

client = TestClient(app)


def test_analyze_login_requirement():
    response = client.post(
        "/api/v1/requirements/analyze",
        json={
            "requirement": (
                "Users should be able to log in using "
                "their registered email and password."
            )
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["feature"] == "User Authentication"
    assert "Registered user" in data["actors"]
    assert len(data["test_scenarios"]) == 3
    assert len(data["expected_outcomes"]) == 3


def test_analyze_registration_requirement():
    response = client.post(
        "/api/v1/requirements/analyze",
        json={
            "requirement": (
                "New users should be able to register "
                "using their email address."
            )
        },
    )

    assert response.status_code == 200
    assert response.json()["feature"] == "User Registration"


def test_empty_requirement():
    response = client.post(
        "/api/v1/requirements/analyze",
        json={"requirement": ""},
    )
    assert response.status_code == 422


def test_whitespace_requirement():
    response = client.post(
        "/api/v1/requirements/analyze",
        json={"requirement": "   "},
    )
    assert response.status_code == 422


def test_missing_requirement():
    response = client.post(
        "/api/v1/requirements/analyze",
        json={},
    )
    assert response.status_code == 422
