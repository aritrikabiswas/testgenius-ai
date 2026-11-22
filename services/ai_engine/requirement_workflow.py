
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from services.ai_engine.requirements_analyzer import (
    RequirementAnalysis,
    analyze_requirement,
)


class RequirementState(TypedDict):
    requirement: str
    analysis: RequirementAnalysis


def analyze_requirement_node(
    state: RequirementState,
) -> RequirementState:
    """Run the requirements analyzer."""

    result = analyze_requirement(state["requirement"])

    return {
        "requirement": state["requirement"],
        "analysis": result,
    }


def build_requirement_workflow():
    """Build and compile the LangGraph workflow."""

    workflow = StateGraph(RequirementState)

    workflow.add_node(
        "analyze_requirement",
        analyze_requirement_node,
    )

    workflow.add_edge(START, "analyze_requirement")
    workflow.add_edge("analyze_requirement", END)

    return workflow.compile()


requirement_workflow = build_requirement_workflow()
