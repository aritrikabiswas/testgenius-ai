
import pytest

from services.ai_engine.requirements_analyzer import analyze_requirement


def test_login_requirement():
    result = analyze_requirement(
        "Users should be able to log in using email and password."
    )

    assert result["feature"] == "User Authentication"
    assert result["actors"] == ["Registered user"]
    assert len(result["test_scenarios"]) == 3


def test_registration_requirement():
    result = analyze_requirement(
        "New users should register with their email."
    )

    assert result["feature"] == "User Registration"
    assert result["actors"] == ["New user"]


def test_unknown_requirement():
    result = analyze_requirement(
        "The application should display a dashboard."
    )

    assert result["feature"] == "General software feature"
    assert len(result["ambiguities"]) > 0


def test_empty_requirement():
    with pytest.raises(ValueError):
        analyze_requirement("")


def test_whitespace_requirement():
    with pytest.raises(ValueError):
        analyze_requirement("   ")
