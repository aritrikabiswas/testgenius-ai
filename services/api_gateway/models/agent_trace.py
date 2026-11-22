
import uuid

from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.api_gateway.models.base import (
    Base,
    TimestampMixin,
    UUIDMixin,
)


class AgentTrace(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "agent_traces"

    test_run_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("test_runs.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    agent_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    agent_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pending",
        nullable=False,
        index=True,
    )

    input_data: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    output_data: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    execution_order: Mapped[int] = mapped_column(
        Integer,
        default=1,
        nullable=False,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    test_run = relationship("TestRun")

    def __repr__(self) -> str:
        return f"<AgentTrace(agent={self.agent_name!r}, status={self.status!r})>"
