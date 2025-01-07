from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

'''def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Student Performance Reviewer API"}


from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app

client = TestClient(app)  # Initialize the test client'''

def test_predict_student_performance():
    response = client.post("/predict/", json={
        "student_id": "0022",
        "name": "Benny",
        "math_score": 85.0,
        "reading_score": 95.0,
        "writing_score": 90.0
    })
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response matches the expected structure
    expected_response = {
        "student_id": "0022",
        "predicted_performance": "Below Average"
    }
    
    # Assert the response is as expected
    assert response.json() == expected_response
