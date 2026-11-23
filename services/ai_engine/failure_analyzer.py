
from typing import TypedDict


class FailureAnalysis(TypedDict):
    failure_type: str
    severity: str
    confidence: float
    exception_type: str
    failure_message: str
    root_cause: str
    recommendation: str


def analyze_failure(error_message: str) -> FailureAnalysis:
    """
    Classify an automated test failure and suggest a debugging action.
    """

    if not error_message or not error_message.strip():
        raise ValueError("Error message cannot be empty.")

    message = error_message.strip()
    text = message.lower()

    exception_type = "Unknown"

    if "timeoutexception" in text:
        exception_type = "TimeoutException"
    elif "nosuchelementexception" in text:
        exception_type = "NoSuchElementException"
    elif "assertionfailederror" in text:
        exception_type = "AssertionFailedError"
    elif "webdriverexception" in text:
        exception_type = "WebDriverException"
    elif "connectionerror" in text or "connection refused" in text:
        exception_type = "ConnectionError"

    if exception_type == "TimeoutException":
        failure_type = "Timeout"
        severity = "High"
        confidence = 0.95
        root_cause = (
            "An element or browser operation did not complete "
            "within the configured waiting time."
        )
        recommendation = (
            "Check page loading, network conditions, element visibility, "
            "and Selenium explicit wait settings."
        )

    elif exception_type == "NoSuchElementException":
        failure_type = "Locator"
        severity = "High"
        confidence = 0.95
        root_cause = (
            "Selenium could not locate the requested element."
        )
        recommendation = (
            "Inspect the page DOM and verify the element locator. "
            "Check whether the element is dynamically loaded."
        )

    elif exception_type == "AssertionFailedError":
        failure_type = "Assertion"
        severity = "Medium"
        confidence = 0.99
        root_cause = (
            "The actual application result did not match "
            "the expected test result."
        )
        recommendation = (
            "Compare expected and actual values. Verify whether "
            "the test expectation or application behaviour is incorrect."
        )

    elif exception_type == "WebDriverException":
        failure_type = "Infrastructure"
        severity = "Critical"
        confidence = 0.85
        root_cause = (
            "The browser automation driver encountered an error."
        )
        recommendation = (
            "Check browser-driver compatibility, browser availability, "
            "and WebDriver configuration."
        )

    elif exception_type == "ConnectionError":
        failure_type = "Network"
        severity = "High"
        confidence = 0.90
        root_cause = (
            "The test runner could not establish a network connection."
        )
        recommendation = (
            "Check network connectivity, target availability, "
            "DNS resolution, and server health."
        )

    else:
        failure_type = "Unknown"
        severity = "Medium"
        confidence = 0.40
        root_cause = (
            "The failure does not match a currently supported "
            "classification rule."
        )
        recommendation = (
            "Inspect the complete stack trace and application logs "
            "to identify the underlying issue."
        )

    return {
        "failure_type": failure_type,
        "severity": severity,
        "confidence": confidence,
        "exception_type": exception_type,
        "failure_message": message,
        "root_cause": root_cause,
        "recommendation": recommendation,
    }
