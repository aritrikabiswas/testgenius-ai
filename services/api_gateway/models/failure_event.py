
import uuid

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.api_gateway.models.base import (
    Base,
    TimestampMixin,
    UUIDMixin,
)


class FailureEvent(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "failure_events"

    test_result_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("test_results.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    failure_type: Mapped[str] = mapped_column(
        String(50),
        default="unknown",
        nullable=False,
    )

    severity: Mapped[str] = mapped_column(
        String(20),
        default="medium",
        nullable=False,
    )

    error_message: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    stack_trace: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    browser_logs: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    screenshot_path: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    root_cause: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    analysis_status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False,
    )

    test_result = relationship("TestResult")

    def __repr__(self) -> str:
        return f"<FailureEvent(type={self.failure_type!r}, severity={self.severity!r})>"
