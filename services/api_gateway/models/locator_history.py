
import uuid

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.api_gateway.models.base import (
    Base,
    TimestampMixin,
    UUIDMixin,
)


class LocatorHistory(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "locator_history"

    test_case_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("test_cases.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    original_locator: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    suggested_locator: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    locator_strategy: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    approval_status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False,
    )

    approval_notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    evidence: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    test_case = relationship("TestCase")

    def __repr__(self) -> str:
        return f"<LocatorHistory(status={self.approval_status!r})>"
