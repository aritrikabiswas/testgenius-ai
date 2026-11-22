
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from services.api_gateway.core.config import get_settings
from services.api_gateway.models.base import Base

settings = get_settings()

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    echo=False,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
