
from fastapi import APIRouter, HTTPException, status

from services.ai_engine.failure_workflow import failure_workflow

from services.api_gateway.schemas.failure import (
    FailureAnalysisRequest,
    FailureAnalysisResponse,
)


router = APIRouter()


@router.post(
    "/analyze",
    response_model=FailureAnalysisResponse,
    status_code=status.HTTP_200_OK,
)
def analyze_failure_endpoint(
    payload: FailureAnalysisRequest,
):
    """Analyze a Selenium or JUnit test failure."""

    try:
        result = failure_workflow.invoke(
            {"error_message": payload.error_message}
        )

        return result["analysis"]

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc
