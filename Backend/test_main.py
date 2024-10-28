from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the landing page!"}

def test_submit_data():
    response = client.post("/submit", json={"title": "Test Title", "description": "Test Description"})
    assert response.status_code == 200
    assert response.json() == {"message": "Data received: Test Title - Test Description"}
