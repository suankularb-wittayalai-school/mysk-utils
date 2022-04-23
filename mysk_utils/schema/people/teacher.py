from optparse import Option
from pydantic import BaseModel
from typing import List, Optional

from ..people.person import Person, QueryPerson, _EnglishPrefix, _ThaiPrefix
from ..subject.subject_group import SubjectGroup


class Teacher(Person):
    """
    Teacher model
    """

    id: str
    teacher_id: str
    subject_groups: Optional[List[SubjectGroup]] = None


class QueryTeacher(QueryPerson):
    prefix_th: _ThaiPrefix
    prefix_en: _EnglishPrefix
    teacher_id: str
