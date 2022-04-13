from pydantic import BaseModel
from typing import List, Optional

from ..student_teacher.person import Person, QueryPerson, _EnglishPrefix, _ThaiPrefix
from ..subject.subject_group import SubjectGroup


class Teacher(BaseModel):
    """
    Teacher model
    """

    id: str
    people: Person
    teacher_id: str
    subject_groups: List[SubjectGroup]


class QueryTeacher(QueryPerson):
    prefix_th: _ThaiPrefix
    prefix_en: _EnglishPrefix
    teacher_id: str
