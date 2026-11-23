
import pytest

from services.ai_engine.failure_analyzer import analyze_failure


def test_timeout_failure():
    result = analyze_failure(
        "TimeoutException: element did not load"
    )

    assert result["failure_type"] == "Timeout"
    assert result["severity"] == "High"


def test_locator_failure():
    result = analyze_failure(
        "NoSuchElementException: login button not found"
    )

    assert result["failure_type"] == "Locator"
    assert result["severity"] == "High"


def test_assertion_failure():
    result = analyze_failure(
        "AssertionFailedError: expected A but was B"
    )

    assert result["failure_type"] == "Assertion"
    assert result["severity"] == "Medium"
    assert result["confidence"] == 0.99


def test_infrastructure_failure():
    result = analyze_failure(
        "WebDriverException: browser session failed"
    )

    assert result["failure_type"] == "Infrastructure"
    assert result["severity"] == "Critical"


def test_network_failure():
    result = analyze_failure(
        "ConnectionError: connection refused"
    )

    assert result["failure_type"] == "Network"
    assert result["severity"] == "High"


def test_unknown_failure():
    result = analyze_failure(
        "SomeUnexpectedError: something went wrong"
    )

    assert result["failure_type"] == "Unknown"
    assert result["severity"] == "Medium"


def test_empty_error_message():
    with pytest.raises(ValueError):
        analyze_failure("")


def test_whitespace_error_message():
    with pytest.raises(ValueError):
        analyze_failure("   ")
