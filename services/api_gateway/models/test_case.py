
import uuid

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.api_gateway.models.base import (
    Base,
    TimestampMixin,
    UUIDMixin,
)


class TestCase(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "test_cases"

    requirement_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("requirements.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    test_type: Mapped[str] = mapped_column(
        String(30),
        default="functional",
        nullable=False,
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        default="medium",
        nullable=False,
    )

    steps: Mapped[list] = mapped_column(
        JSONB,
        nullable=False,
        default=list,
    )

    expected_result: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    estimated_duration_seconds: Mapped[int] = mapped_column(
        Integer,
        default=60,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="draft",
        nullable=False,
    )

    requirement = relationship("Requirement")

    def __repr__(self) -> str:
        return f"<TestCase(title={self.title!r}, status={self.status!r})>"
