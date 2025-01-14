from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):           # Basic model
    student_id: str
    name: str
    math_score: Optional[int] = None
    reading_score: Optional[int] = None
    writing_score: Optional[int] = None
