# /backend/app/services/zone_service.py
from typing import List, Dict
from uuid import uuid4
from zoneinfo import ZoneInfo
from pydantic import ValidationError

from ..schemas.zone import ZoneCreate, Zone

# Simple in-memory storage (replace with real DB in production)
_zone_storage: Dict[int, Zone] = {}
_id_counter = 0

class ZoneService:
    
    @staticmethod
    def _validate_timezone(timezone_string: str) -> bool:
        """Verifies if the timezone string is valid IANA format."""
        try:
            ZoneInfo(timezone_string)
            return True
        except Exception:
            return False

    def create_zone(self, zone_in: ZoneCreate) -> Zone:
        """Creates a new time zone entry with validation."""
        if not self._validate_timezone(zone_in.timezone_string):
            raise ValueError("Invalid IANA time zone string provided.")
            
        global _id_counter
        _id_counter += 1
        
        # Create output schema model, assigning a simulated ID
        new_zone = Zone(id=_id_counter, **zone_in.model_dump())
        _zone_storage[_id_counter] = new_zone
        return new_zone

    def get_all_zones(self) -> List[Zone]:
        """Returns all stored time zone entries."""
        return list(_zone_storage.values())
    
    def get_zone_by_id(self, zone_id: int) -> Zone | None:
        """Retrieves a specific time zone entry by ID."""
        return _zone_storage.get(zone_id)
