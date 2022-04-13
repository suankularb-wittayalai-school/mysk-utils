from pydantic import BaseModel
from typing import List, Optional

from ..people.person import Person


class VaccineProvider(BaseModel):
    id: int
    name: str


class Vaccine(BaseModel):
    id: int
    taker: Person
    dose: int
    provider: VaccineProvider
    date: str
    note: Optional[str]
