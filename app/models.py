from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    student_id: str
    name: str
    math_score: Optional[int] = None
    reading_score: Optional[int] = None
    writing_score: Optional[int] = None
