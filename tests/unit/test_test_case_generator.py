
import pytest

from services.ai_engine.requirements_analyzer import analyze_requirement
from services.ai_engine.test_case_generator import generate_test_cases


def test_generates_three_login_test_cases():
    analysis = analyze_requirement(
        "Users should be able to log in using their email and password."
    )

    test_cases = generate_test_cases(analysis)

    assert len(test_cases) == 3


def test_test_case_ids_are_unique():
    analysis = analyze_requirement(
        "Users should be able to log in using their email and password."
    )

    test_cases = generate_test_cases(analysis)
    test_case_ids = [case["test_case_id"] for case in test_cases]

    assert test_case_ids == ["TC-001", "TC-002", "TC-003"]
    assert len(test_case_ids) == len(set(test_case_ids))


def test_invalid_login_is_negative():
    analysis = analyze_requirement(
        "Users should be able to log in using their email and password."
    )

    test_cases = generate_test_cases(analysis)

    invalid_case = next(
        case for case in test_cases
        if "invalid" in case["title"].lower()
    )

    assert invalid_case["test_type"] == "Negative"
    assert invalid_case["priority"] == "High"


def test_test_cases_contain_required_fields():
    analysis = analyze_requirement(
        "Users should be able to log in using their email and password."
    )

    test_cases = generate_test_cases(analysis)

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

    for test_case in test_cases:
        assert required_fields.issubset(test_case.keys())


def test_generator_rejects_missing_scenarios():
    analysis = analyze_requirement(
        "The application should display a dashboard."
    )

    with pytest.raises(ValueError):
        generate_test_cases(analysis)
