# /backend/app/api/endpoints/time_zones.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from ...schemas.zone import Zone, ZoneCreate
from ...services.zone_service import ZoneService

router = APIRouter()

# Dependency for ZoneService to show clean dependency injection practice
def get_zone_service() -> ZoneService:
    return ZoneService()

@router.post("/", response_model=Zone, status_code=status.HTTP_201_CREATED)
def create_new_zone(
    zone_in: ZoneCreate,
    service: ZoneService = Depends(get_zone_service)
):
    """Creates a new time zone entry."""
    try:
        return service.create_zone(zone_in)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", response_model=List[Zone])
def read_all_zones(
    service: ZoneService = Depends(get_zone_service)
):
    """Retrieves all stored time zone entries."""
    return service.get_all_zones()

@router.get("/{zone_id}", response_model=Zone)
def read_zone_by_id(
    zone_id: int,
    service: ZoneService = Depends(get_zone_service)
):
    """Retrieves a specific time zone entry."""
    zone = service.get_zone_by_id(zone_id)
    if not zone:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zone not found")
    return zone
