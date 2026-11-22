
import uuid

from sqlalchemy import ForeignKey, Float, String, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.api_gateway.models.base import (
    Base,
    TimestampMixin,
    UUIDMixin,
)


class MLPrediction(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "ml_predictions"

    test_result_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("test_results.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    prediction_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    predicted_label: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    confidence_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    model_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    model_version: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    explanation: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    prediction_details: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    test_result = relationship("TestResult")

    def __repr__(self) -> str:
        return (
            f"<MLPrediction(type={self.prediction_type!r}, "
            f"label={self.predicted_label!r})>"
        )
