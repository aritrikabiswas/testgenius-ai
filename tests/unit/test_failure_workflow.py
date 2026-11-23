
import pytest

from services.ai_engine.failure_workflow import failure_workflow


def test_workflow_identifies_assertion_failure():
    result = failure_workflow.invoke({
        "error_message": (
            "AssertionFailedError: "
            "expected Wrong Page Title but was Example Domain"
        )
    })

    assert result["analysis"]["failure_type"] == "Assertion"
    assert result["analysis"]["severity"] == "Medium"
    assert result["analysis"]["confidence"] == 0.99


def test_workflow_identifies_timeout_failure():
    result = failure_workflow.invoke({
        "error_message": "TimeoutException: element did not load"
    })

    assert result["analysis"]["failure_type"] == "Timeout"
    assert result["analysis"]["severity"] == "High"


def test_workflow_identifies_locator_failure():
    result = failure_workflow.invoke({
        "error_message": "NoSuchElementException: button not found"
    })

    assert result["analysis"]["failure_type"] == "Locator"


def test_workflow_identifies_infrastructure_failure():
    result = failure_workflow.invoke({
        "error_message": "WebDriverException: browser session failed"
    })

    assert result["analysis"]["failure_type"] == "Infrastructure"
    assert result["analysis"]["severity"] == "Critical"


def test_workflow_generates_debugging_recommendation():
    result = failure_workflow.invoke({
        "error_message": "ConnectionError: connection refused"
    })

    assert result["analysis"]["failure_type"] == "Network"
    assert result["analysis"]["recommendation"]
    assert result["analysis"]["root_cause"]


def test_workflow_rejects_empty_error_message():
    with pytest.raises(ValueError):
        failure_workflow.invoke({
            "error_message": ""
        })
