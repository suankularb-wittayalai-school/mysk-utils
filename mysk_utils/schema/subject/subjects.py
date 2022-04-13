from enum import Enum
from pydantic import BaseModel
from typing import List, Optional

from ..people.teacher import Teacher
from ..subject.subject_group import SubjectGroup


class _SubjectTypesTH(str, Enum):
    """
    SubjectTypes
    """

    core = "รายวิชาพื้นฐาน"
    elective = "รายวิชาเลือก"
    additional = "รายวิชาเพิ่มเติม"
    development = "กิจกรรมพัฒนาผู้เรียน"


class _SubjectTypesEN(str, Enum):
    """
    SubjectTypes
    """

    core = "Core Courses"
    elective = "Elective Courses"
    additional = "Additional Courses"
    development = "Learner's Development Activities"


class Subject(BaseModel):
    id: int
    name_th: str
    name_en: str
    code_th: str
    code_en: str
    type_th: _SubjectTypesTH  # รายวิชาเพิ่มเติม | รายวิชาพื้นฐาน | กิจกรรมพัฒนาผู้เรียน | วิชาเลือก
    type_en: _SubjectTypesEN
    credit: float
    # this include every teacher who teach this subject
    teacher: List[Teacher]
    coteachers: Optional[List[Teacher]] = None

    description_th: Optional[str]
    description_en: Optional[str]
    year: int
    semester: int
    group: SubjectGroup
    syllabus: Optional[str]  # url to the syllabus
