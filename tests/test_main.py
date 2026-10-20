
from fastapi.testclient import TestClient

from app.main import app, complaints, complaint_ids

client = TestClient(app)


def setup_function():
    complaints.clear()
    # Reset the ID generator so tests are reproducible.
    global complaint_ids
    complaint_ids = iter(range(1, 1000000))


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_complaint():
    response = client.post(
        "/complaints",
        json={
            "student_id": "STU001",
            "room_number": "A-101",
            "category": "plumbing",
            "description": "Water leakage in bathroom",
        },
    )

    assert response.status_code == 201
    assert response.json()["category"] == "plumbing"
    assert response.json()["status"] == "open"


def test_invalid_category_is_rejected():
    response = client.post(
        "/complaints",
        json={
            "student_id": "STU001",
            "room_number": "A-101",
            "category": "painting",
            "description": "Wall needs repainting",
        },
    )

    assert response.status_code == 400


def test_missing_complaint_returns_404():
    response = client.get("/complaints/999999")

    assert response.status_code == 404
