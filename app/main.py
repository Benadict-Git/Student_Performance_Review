from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Student Performance Reviewer")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Student Performance Reviewer API"}
