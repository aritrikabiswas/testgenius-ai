
import re
from typing import TypedDict


class RequirementAnalysis(TypedDict):
    requirement: str
    feature: str
    actors: list[str]
    preconditions: list[str]
    test_scenarios: list[str]
    expected_outcomes: list[str]
    ambiguities: list[str]


def analyze_requirement(requirement: str) -> RequirementAnalysis:
    """Convert plain-English requirements into test-planning information."""

    if not requirement or not requirement.strip():
        raise ValueError("Requirement cannot be empty.")

    normalized_requirement = requirement.strip()
    text = normalized_requirement.lower()

    analysis: RequirementAnalysis = {
        "requirement": normalized_requirement,
        "feature": "General software feature",
        "actors": [],
        "preconditions": [],
        "test_scenarios": [],
        "expected_outcomes": [],
        "ambiguities": [],
    }

    # Authentication detection must happen before registration detection.
    is_authentication = bool(
        re.search(r"\b(login|log in|sign in|sign-in)\b", text)
    )

    is_registration = bool(
        re.search(r"\b(register|registration|sign up|sign-up)\b", text)
        or "create an account" in text
    )

    if is_authentication:
        analysis["feature"] = "User Authentication"
        analysis["actors"] = ["Registered user"]
        analysis["preconditions"] = [
            "User account exists",
            "Application is accessible",
        ]
        analysis["test_scenarios"] = [
            "Login with valid credentials",
            "Login with invalid credentials",
            "Submit login form with empty fields",
        ]
        analysis["expected_outcomes"] = [
            "Valid users can access their accounts",
            "Invalid credentials are rejected",
            "Required field validation is displayed",
        ]

    elif is_registration:
        analysis["feature"] = "User Registration"
        analysis["actors"] = ["New user"]
        analysis["preconditions"] = [
            "Registration page is accessible",
        ]
        analysis["test_scenarios"] = [
            "Register with valid information",
            "Register with an existing email",
            "Submit registration with missing fields",
        ]
        analysis["expected_outcomes"] = [
            "A valid account is created",
            "Duplicate email registration is rejected",
            "Missing required fields are validated",
        ]

    else:
        analysis["ambiguities"] = [
            "Feature type could not be identified automatically",
            "More detail may be needed to generate precise test scenarios",
        ]

    return analysis
