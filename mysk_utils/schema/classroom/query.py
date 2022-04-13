from pydantic import BaseModel


class QueryClassroom(BaseModel):
    room_number: str
    year: int
    semester: int
