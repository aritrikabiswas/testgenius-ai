
import uuid

from sqlalchemy import ForeignKey, String, Text, Float
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.api_gateway.models.base import (
    Base,
    TimestampMixin,
    UUIDMixin,
)


class DebuggingReport(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "debugging_reports"

    failure_event_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("failure_events.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    root_cause: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    suggested_fix: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    confidence_score: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    analysis_details: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    model_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="generated",
        nullable=False,
    )

    failure_event = relationship("FailureEvent")

    def __repr__(self) -> str:
        return f"<DebuggingReport(status={self.status!r})>"
