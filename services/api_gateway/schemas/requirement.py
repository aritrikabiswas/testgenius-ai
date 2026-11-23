
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
