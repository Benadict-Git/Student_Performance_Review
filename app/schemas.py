from pydantic import BaseModel
from typing import List, Optional

class StudentSchema(BaseModel):
    student_id: str
    name: str
    math_score: int
    reading_score: int
    writing_score: int

    class Config:                   # attribute-based parsing
        from_attributes = True

class PredictionSchema(BaseModel):
    student_id: str
    predicted_performance: str