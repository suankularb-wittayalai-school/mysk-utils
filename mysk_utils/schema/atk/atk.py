from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

from ..people.person import Person


class _ATKMethodEnum(str, Enum):
    oral = "oral"
    rt = "rtpcr"
    nasal = "nasal"
    other = "other"


class AtkRecord(BaseModel):
    id: int
    tester: Person
    result: bool
    date: str
    method: _ATKMethodEnum
    place: str
    evidence: str
