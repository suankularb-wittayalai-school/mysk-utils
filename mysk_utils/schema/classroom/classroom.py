from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from ..people.teacher import Teacher
from ..people.student import Student

from ..schedule.schedule import Schedule
from ..people.contacts import Contact

from ..subject.room_subject import RoomSubject


class Classroom(BaseModel):
    id: int
    number: int
    year: int
    term: int
    students: List[Student]
    advisors: List[Teacher]
    schedule: Schedule
    contacts: List[Contact]
    subjects: List[RoomSubject]
