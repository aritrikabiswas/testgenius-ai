
from pydantic import BaseModel, Field, field_validator


class FailureAnalysisRequest(BaseModel):
    error_message: str = Field(
        min_length=1,
        max_length=20000,
        description="Selenium or JUnit failure message or stack trace.",
    )

    @field_validator("error_message")
    @classmethod
    def validate_error_message(cls, value: str) -> str:
        if not value.strip():
            raise ValueError(
                "Error message cannot be empty or whitespace."
            )
        return value.strip()


class FailureAnalysisResponse(BaseModel):
    failure_type: str
    severity: str
    confidence: float
    exception_type: str
    failure_message: str
    root_cause: str
    recommendation: str
