
from fastapi import APIRouter, HTTPException, status

from services.ai_engine.requirement_workflow import requirement_workflow

router = APIRouter()


@router.post("/analyze")
def analyze_requirement_endpoint(payload: dict):
    """Analyze a software requirement using the LangGraph workflow."""

    requirement = payload.get("requirement")

    if not isinstance(requirement, str) or not requirement.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="A non-empty requirement is required.",
        )

    try:
        result = requirement_workflow.invoke(
            {"requirement": requirement}
        )
        return result["analysis"]

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc
