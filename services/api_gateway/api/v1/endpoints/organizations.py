
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from services.api_gateway.db.database import get_db
from services.api_gateway.models.organization import Organization
from services.api_gateway.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_organization(
    organization_data: OrganizationCreate,
    db: Session = Depends(get_db),
):
    organization = Organization(
        name=organization_data.name,
        slug=organization_data.slug,
    )

    db.add(organization)

    try:
        db.commit()
        db.refresh(organization)
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An organization with this slug already exists.",
        ) from exc

    return organization


@router.get(
    "/",
    response_model=list[OrganizationResponse],
)
def list_organizations(
    db: Session = Depends(get_db),
):
    organizations = (
        db.query(Organization)
        .order_by(Organization.created_at.desc())
        .all()
    )

    return organizations


@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def get_organization(
    organization_id: UUID,
    db: Session = Depends(get_db),
):
    organization = (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )

    if organization is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Organization not found.",
        )

    return organization
