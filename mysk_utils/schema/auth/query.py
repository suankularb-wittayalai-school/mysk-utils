from pydantic import BaseModel
from .user import _RoleChoice


class QueryUser(BaseModel):
    password: str
    email: str
    role: _RoleChoice
    std_id: str


class QueryUserTeacher(BaseModel):
    password: str
    email: str
    role: _RoleChoice
    teacher_id: str


class QueryLogin(BaseModel):
    username: str
    password: str
