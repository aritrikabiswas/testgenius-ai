
from typing import TypedDict

from services.ai_engine.requirements_analyzer import RequirementAnalysis


class GeneratedTestCase(TypedDict):
    test_case_id: str
    title: str
    test_type: str
    priority: str
    preconditions: list[str]
    test_steps: list[str]
    test_data: dict[str, str]
    expected_result: str


def generate_test_cases(
    analysis: RequirementAnalysis,
) -> list[GeneratedTestCase]:
    """Generate structured test cases from analyzed requirements."""

    feature = analysis["feature"]
    scenarios = analysis["test_scenarios"]
    outcomes = analysis["expected_outcomes"]
    preconditions = analysis["preconditions"]

    if not scenarios:
        raise ValueError(
            "No test scenarios available for test case generation."
        )

    test_cases: list[GeneratedTestCase] = []

    for index, scenario in enumerate(scenarios, start=1):
        scenario_lower = scenario.lower()

        if "invalid" in scenario_lower or "existing" in scenario_lower:
            test_type = "Negative"
            priority = "High"
        elif "empty" in scenario_lower or "missing" in scenario_lower:
            test_type = "Negative"
            priority = "Medium"
        else:
            test_type = "Positive"
            priority = "High"

        expected_result = (
            outcomes[index - 1]
            if index <= len(outcomes)
            else "Application responds according to the requirement."
        )

        test_cases.append(
            {
                "test_case_id": f"TC-{index:03d}",
                "title": f"{feature}: {scenario}",
                "test_type": test_type,
                "priority": priority,
                "preconditions": preconditions.copy(),
                "test_steps": [
                    f"Open the application.",
                    f"Navigate to the {feature} page.",
                    f"Execute the scenario: {scenario}.",
                    "Verify the application response.",
                ],
                "test_data": {},
                "expected_result": expected_result,
            }
        )

    return test_cases
