
from fastapi import FastAPI, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from services.api_gateway.api.v1.endpoints.organizations import (
    router as organizations_router,
)
from services.api_gateway.core.config import get_settings
from services.api_gateway.db.database import engine

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Autonomous Selenium Testing and Intelligent Debugging Platform",
    version=settings.app_version,
)

app.include_router(
    organizations_router,
    prefix="/api/v1/organizations",
    tags=["Organizations"],
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to TestGenius AI",
        "platform": "Autonomous Testing and Intelligent Debugging",
        "version": settings.app_version,
        "status": "running",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "testgenius-api-gateway",
        "environment": settings.environment,
    }

@app.get("/health/database")
def database_health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed.",
        ) from exc

    return {
        "status": "healthy",
        "database": "connected",
        "service": "testgenius-postgresql",
    }

