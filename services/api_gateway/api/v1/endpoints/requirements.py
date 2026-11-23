
from fastapi import APIRouter, HTTPException, status

from services.ai_engine.requirement_workflow import requirement_workflow

from services.api_gateway.schemas.requirement import (
    RequirementAnalysisRequest,
    RequirementAnalysisResponse,
)


router = APIRouter()


@router.post(
    "/analyze",
    response_model=RequirementAnalysisResponse,
    status_code=status.HTTP_200_OK,
)
def analyze_requirement_endpoint(
    payload: RequirementAnalysisRequest,
):
    """Analyze a software requirement using the LangGraph workflow."""

    try:
        result = requirement_workflow.invoke(
            {"requirement": payload.requirement}
        )

        return result["analysis"]

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc


@router.post(
    "/generate-tests",
    status_code=status.HTTP_200_OK,
)
def generate_test_cases_endpoint(
    payload: RequirementAnalysisRequest,
):
    """Analyze a requirement and generate structured test cases."""

    try:
        result = requirement_workflow.invoke(
            {"requirement": payload.requirement}
        )

        return {
            "requirement": result["requirement"],
            "analysis": result["analysis"],
            "test_cases": result["test_cases"],
            "total_test_cases": len(result["test_cases"]),
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc


from pydantic import BaseModel, Field, field_validator


class RequirementAnalysisRequest(BaseModel):
    requirement: str = Field(
        min_length=1,
        max_length=10000,
        description="Plain-English software requirement to analyze.",
    )

    @field_validator("requirement")
    @classmethod
    def validate_requirement(cls, value: str) -> str:
        if not value.strip():
            raise ValueError(
                "Requirement cannot be empty or whitespace."
            )
        return value.strip()


class RequirementAnalysisResponse(BaseModel):
    requirement: str
    feature: str
    actors: list[str]
    preconditions: list[str]
    test_scenarios: list[str]
    expected_outcomes: list[str]
    ambiguities: list[str]
