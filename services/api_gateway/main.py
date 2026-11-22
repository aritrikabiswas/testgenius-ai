
from fastapi import FastAPI, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from services.api_gateway.api.v1.endpoints.organizations import (
    router as organizations_router,
)
from services.api_gateway.api.v1.endpoints.requirements import (
    router as requirements_router,
)
from services.api_gateway.core.config import get_settings
from services.api_gateway.db.database import engine

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="TestGenius AI - Autonomous Selenium Testing and Intelligent Debugging Platform",
)


# Organization API
app.include_router(
    organizations_router,
    prefix="/api/v1/organizations",
    tags=["Organizations"],
)


# Requirements Analysis API
app.include_router(
    requirements_router,
    prefix="/api/v1/requirements",
    tags=["Requirements"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to TestGenius AI",
        "version": settings.app_version,
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "testgenius-api-gateway",
    }


@app.get("/health/database")
def database_health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
            "service": "testgenius-postgresql",
        }

    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed.",
        ) from exc
