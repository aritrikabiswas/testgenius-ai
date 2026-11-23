
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from services.ai_engine.failure_analyzer import (
    FailureAnalysis,
    analyze_failure,
)


class FailureState(TypedDict):
    error_message: str
    analysis: FailureAnalysis


def analyze_failure_node(state: FailureState) -> FailureState:
    """Analyze and classify the supplied test failure."""

    result = analyze_failure(state["error_message"])

    return {
        **state,
        "analysis": result,
    }


def build_failure_workflow():
    """Build and compile the failure analysis workflow."""

    workflow = StateGraph(FailureState)

    workflow.add_node(
        "analyze_failure",
        analyze_failure_node,
    )

    workflow.add_edge(START, "analyze_failure")
    workflow.add_edge("analyze_failure", END)

    return workflow.compile()


failure_workflow = build_failure_workflow()
