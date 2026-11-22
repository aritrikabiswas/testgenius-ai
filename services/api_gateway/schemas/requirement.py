
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
