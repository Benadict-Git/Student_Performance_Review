from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb://localhost:27017/")  # MongoDB URI
    db = client.student_performance
    return db
