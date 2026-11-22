
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from services.api_gateway.models.base import (
    Base,
    TimestampMixin,
    UUIDMixin,
)


class Organization(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        default=True,
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<Organization(name={self.name!r}, slug={self.slug!r})>"
