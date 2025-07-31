# tests/test_tasks.py

from fastapi.testclient import TestClient
from app import app
import pytest
from auth.azure_auth import verify_azure_identity

def mock_verify_azure_identity():
    return True
app.dependency_overrides[verify_azure_identity] = mock_verify_azure_identity
client = TestClient(app)


@pytest.fixture(autouse=True)
def patch_auth(monkeypatch):
    monkeypatch.setattr("routes.tasks.verify_azure_identity", mock_verify_azure_identity)

def test_create_task():
    payload = {
        "title": "Test Task",
        "description": "Test Description",
        "completed": False
    }
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    assert response.json() == {
        "message": "Task created",
        "task": payload
    }

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert "tasks" in response.json()
