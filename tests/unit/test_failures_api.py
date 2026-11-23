
from fastapi.testclient import TestClient

from services.api_gateway.main import app


client = TestClient(app)


# Failure Analysis API tests

def test_analyze_assertion_failure():
    response = client.post(
        "/api/v1/failures/analyze",
        json={
            "error_message": (
                "AssertionFailedError: expected Wrong Page Title "
                "but was Example Domain"
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["failure_type"] == "Assertion"
    assert data["severity"] == "Medium"
    assert data["exception_type"] == "AssertionFailedError"
    assert data["confidence"] == 0.99
    assert "root_cause" in data
    assert "recommendation" in data


def test_analyze_timeout_failure():
    response = client.post(
        "/api/v1/failures/analyze",
        json={
            "error_message": (
                "TimeoutException: element did not appear"
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["failure_type"] == "Timeout"
    assert data["severity"] == "High"
    assert data["exception_type"] == "TimeoutException"


def test_analyze_locator_failure():
    response = client.post(
        "/api/v1/failures/analyze",
        json={
            "error_message": (
                "NoSuchElementException: element not found"
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["failure_type"] == "Locator"
    assert data["exception_type"] == "NoSuchElementException"


def test_analyze_infrastructure_failure():
    response = client.post(
        "/api/v1/failures/analyze",
        json={
            "error_message": (
                "WebDriverException: browser driver failed"
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["failure_type"] == "Infrastructure"
    assert data["severity"] == "Critical"


def test_analyze_network_failure():
    response = client.post(
        "/api/v1/failures/analyze",
        json={
            "error_message": (
                "ConnectionError: connection refused"
            )
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["failure_type"] == "Network"
    assert data["exception_type"] == "ConnectionError"


def test_analyze_unknown_failure():
    response = client.post(
        "/api/v1/failures/analyze",
        json={
            "error_message": "Unexpected application error"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["failure_type"] == "Unknown"


def test_empty_error_message():
    response = client.post(
        "/api/v1/failures/analyze",
        json={"error_message": ""},
    )

    assert response.status_code == 422


def test_whitespace_error_message():
    response = client.post(
        "/api/v1/failures/analyze",
        json={"error_message": "   "},
    )

    assert response.status_code == 422


def test_missing_error_message():
    response = client.post(
        "/api/v1/failures/analyze",
        json={},
    )

    assert response.status_code == 422
