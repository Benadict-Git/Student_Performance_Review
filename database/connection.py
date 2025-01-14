from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI (ATLAS cloud can be used)
    db = client.student_performance
    return db
