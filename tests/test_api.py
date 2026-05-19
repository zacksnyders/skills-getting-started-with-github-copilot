from fastapi.testclient import TestClient
from src.app import app


client = TestClient(app)


def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert "Chess Club" in data


def test_signup_for_activity():
    email = "test_student@mergington.edu"
    resp = client.post("/activities/Chess Club/signup", params={"email": email})
    assert resp.status_code == 200
    assert f"Signed up {email} for Chess Club" in resp.json().get("message", "")