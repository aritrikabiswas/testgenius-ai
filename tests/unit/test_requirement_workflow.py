
import pytest

from services.ai_engine.requirement_workflow import requirement_workflow


def test_workflow_identifies_login_requirement():
    result = requirement_workflow.invoke({
        "requirement": (
            "Users should be able to log in using "
            "their email and password."
        )
    })

    assert result["analysis"]["feature"] == "User Authentication"
    assert result["analysis"]["actors"] == ["Registered user"]


def test_workflow_generates_test_scenarios():
    result = requirement_workflow.invoke({
        "requirement": (
            "Users should be able to log in using "
            "their email and password."
        )
    })

    scenarios = result["analysis"]["test_scenarios"]

    assert len(scenarios) == 3
    assert "Login with valid credentials" in scenarios
    assert "Login with invalid credentials" in scenarios


def test_workflow_identifies_registration_requirement():
    result = requirement_workflow.invoke({
        "requirement": (
            "New users should register with their email."
        )
    })

    assert result["analysis"]["feature"] == "User Registration"


def test_workflow_rejects_empty_requirement():
    with pytest.raises(ValueError):
        requirement_workflow.invoke({
            "requirement": ""
        })


def test_workflow_returns_expected_outcomes():
    result = requirement_workflow.invoke({
        "requirement": (
            "Users should be able to log in using "
            "their email and password."
        )
    })

    outcomes = result["analysis"]["expected_outcomes"]

    assert len(outcomes) == 3
    assert "Invalid credentials are rejected" in outcomes
