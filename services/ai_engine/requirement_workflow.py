
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from services.ai_engine.requirements_analyzer import (
    RequirementAnalysis,
    analyze_requirement,
)
from services.ai_engine.test_case_generator import (
    GeneratedTestCase,
    generate_test_cases,
)


class RequirementState(TypedDict):
    requirement: str
    analysis: RequirementAnalysis
    test_cases: list[GeneratedTestCase]


def analyze_requirement_node(
    state: RequirementState,
) -> RequirementState:
    """Analyze the submitted software requirement."""

    result = analyze_requirement(state["requirement"])

    return {
        **state,
        "analysis": result,
    }


def generate_test_cases_node(
    state: RequirementState,
) -> RequirementState:
    """Generate structured test cases from the analysis."""

    test_cases = generate_test_cases(state["analysis"])

    return {
        **state,
        "test_cases": test_cases,
    }


def build_requirement_workflow():
    """Build and compile the complete requirement workflow."""

    workflow = StateGraph(RequirementState)

    workflow.add_node(
        "analyze_requirement",
        analyze_requirement_node,
    )

    workflow.add_node(
        "generate_test_cases",
        generate_test_cases_node,
    )

    workflow.add_edge(START, "analyze_requirement")
    workflow.add_edge(
        "analyze_requirement",
        "generate_test_cases",
    )
    workflow.add_edge("generate_test_cases", END)

    return workflow.compile()


requirement_workflow = build_requirement_workflow()
