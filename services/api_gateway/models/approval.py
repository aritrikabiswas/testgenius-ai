
import uuid

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.api_gateway.models.base import (
    Base,
    TimestampMixin,
    UUIDMixin,
)


class Approval(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "approvals"

    failure_event_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("failure_events.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    locator_history_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("locator_history.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    approval_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False,
        index=True,
    )

    reviewer: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    comments: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    decision_details: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    failure_event = relationship("FailureEvent")
    locator_history = relationship("LocatorHistory")

    def __repr__(self) -> str:
        return f"<Approval(type={self.approval_type!r}, status={self.status!r})>"
