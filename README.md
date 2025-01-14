Student Performance Reviewer :
The Student Performance Reviewer project uses FastAPI, Machine Learning, and MongoDB to predict the performance of students based on their academic scores. This project allows you to analyze student performance by predicting whether a student will perform well or poorly based on their scores in Math, Reading, and Writing.

Features :
API Endpoints -> Expose an endpoint for predicting student performance based on their scores.
Machine Learning -> A Random Forest Classifier is trained to predict performance based on historical student data.
Database Integration -> Store student performance data in MongoDB for persistent storage.
Predictive Analytics -> Predict the performance outcome based on Math, Reading, and Writing scores.

Tech Stack :

Backend :

FastAPI -> Python web framework for building APIs.
Uvicorn -> ASGI server for FastAPI applications.
Pydantic -> Data validation and settings management.

Machine Learning:

scikit-learn -> For model building and evaluation.
RandomForestClassifier -> Used to train the prediction model on student scores.

Database :
MongoDB -> NoSQL database to store student performance data.

Testing:
pytest -> Framework for testing the API and application logic.

Requirements :
To run this project, you need to install the following dependencies:
Python 3.xx , MongoDB (Make sure you have a MongoDB instance running or use a cloud-based service like MongoDB Atlas) .
