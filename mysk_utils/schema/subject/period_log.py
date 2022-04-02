from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import date

from enum import Enum

from .room_subject import RoomSubject


class TeachingMedium(Enum):
    meet = "meet"
    tape = "pre-record"
    material = "material"
    assignment = "assignment"
    onsite = "onsite"


class PeriodLog(BaseModel):
    id: int
    date: date
    topic: str
    medium: List[TeachingMedium]
    participation_level: int
    room_subject: RoomSubject

    @validator("participation_level")
    def check_participation_level(cls, v):
        if v < 1 or v > 5:
            raise ValueError("Participation level must be between 1 and 5")
        return v
