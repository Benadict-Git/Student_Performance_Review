from fastapi import APIRouter, HTTPException
from app.schemas import StudentSchema, PredictionSchema
from database.connection import get_db
from app.ml.models import predict_performance

router = APIRouter()

@router.post("/students/")
def add_student(student: StudentSchema):
    db = get_db()
    db.students.insert_one(student.dict())
    return {"message": "Student added successfully"}

@router.get("/students/")
def get_students():
    db = get_db()
    students = list(db.students.find({}, {"_id": 0}))
    return students

@router.post("/predict/", response_model=PredictionSchema)
def predict_student_performance(student: StudentSchema):
    features = [student.math_score, student.reading_score, student.writing_score]
    performance = predict_performance(features)  # Already returns a string

    return PredictionSchema(
        student_id=student.student_id,
        predicted_performance=performance
    )
