
from fastapi.testclient import TestClient

from services.api_gateway.main import app

client = TestClient(app)


# Requirement analysis API tests

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


# Test case generation API tests

def test_generate_login_test_cases():
    response = client.post(
        "/api/v1/requirements/generate-tests",
        json={
            "requirement": (
                "Users should be able to log in using "
                "their registered email and password."
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["analysis"]["feature"] == "User Authentication"
    assert data["total_test_cases"] == 3
    assert len(data["test_cases"]) == 3


def test_generated_test_case_ids():
    response = client.post(
        "/api/v1/requirements/generate-tests",
        json={
            "requirement": (
                "Users should be able to log in using "
                "their registered email and password."
            )
        },
    )

    assert response.status_code == 200

    test_cases = response.json()["test_cases"]

    test_case_ids = [
        test_case["test_case_id"]
        for test_case in test_cases
    ]

    assert test_case_ids == ["TC-001", "TC-002", "TC-003"]


def test_generated_test_case_types():
    response = client.post(
        "/api/v1/requirements/generate-tests",
        json={
            "requirement": (
                "Users should be able to log in using "
                "their registered email and password."
            )
        },
    )

    assert response.status_code == 200

    test_cases = response.json()["test_cases"]

    assert test_cases[0]["test_type"] == "Positive"
    assert test_cases[1]["test_type"] == "Negative"
    assert test_cases[2]["test_type"] == "Negative"


def test_generated_test_cases_contain_required_fields():
    response = client.post(
        "/api/v1/requirements/generate-tests",
        json={
            "requirement": (
                "Users should be able to log in using "
                "their registered email and password."
            )
        },
    )

    assert response.status_code == 200

    required_fields = {
        "test_case_id",
        "title",
        "test_type",
        "priority",
        "preconditions",
        "test_steps",
        "test_data",
        "expected_result",
    }

    for test_case in response.json()["test_cases"]:
        assert required_fields.issubset(test_case.keys())


def test_generate_test_cases_with_empty_requirement():
    response = client.post(
        "/api/v1/requirements/generate-tests",
        json={"requirement": ""},
    )

    assert response.status_code == 422
