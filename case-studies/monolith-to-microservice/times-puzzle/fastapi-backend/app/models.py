from __future__ import annotations
from pydantic import BaseModel, conint
from typing import List, Optional

class RoundCreate(BaseModel):
    min: conint(ge=1) = 2
    max: conint(ge=1) = 12
    size: conint(ge=2, le=16) = 9
    retry_wrong_answers: bool = False
    seed: Optional[int] = None

class RoundOut(BaseModel):
    round_id: str
    product: int
    numbers: List[int]

class GuessIn(BaseModel):
    round_id: str
    a: int
    b: int

class GuessOut(BaseModel):
    correct: bool

class StatusOut(BaseModel):
    round_id: str
    all_numbers_used: bool
    used_pairs: int
    total_pairs: int
