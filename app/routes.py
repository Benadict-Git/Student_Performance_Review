from fastapi import APIRouter, HTTPException
from app.schemas import StudentSchema, PredictionSchema
from database.connection import get_db
from app.ml.model import predict_performance

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

@router.post("/predict/")
def predict_student_performance(student: StudentSchema):
    features = [student.math_score, student.reading_score, student.writing_score]
    prediction = predict_performance(features)
    performance_map = {0: "Below Average", 1: "Average", 2: "Above Average"}
    return PredictionSchema(
        student_id=student.student_id,
        predicted_performance=performance_map[prediction],
    )
