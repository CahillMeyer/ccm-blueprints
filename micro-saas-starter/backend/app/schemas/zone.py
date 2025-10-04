# /backend/app/schemas/zone.py

from pydantic import BaseModel, Field

# Schema for creating a new time zone entry (Input model)
class ZoneCreate(BaseModel):
    # Name the user gives to the time zone entry (e.g., 'London Office')
    name: str = Field(..., max_length=50)
    
    # The timezone string (e.g., 'America/Los_Angeles' or 'Europe/London')
    # Validation of this string would happen in the service layer
    timezone_string: str = Field(..., max_length=60)
    
    # Optional field to associate this entry with a specific user (future proofing for auth)
    user_id: str | None = None

# Schema for reading a time zone entry (Output model)
class Zone(ZoneCreate):
    # Unique identifier, typically from the database
    id: int
    
    # Configuration to allow SQLAlchemy/ORM style access
    class Config:
        from_attributes = True
