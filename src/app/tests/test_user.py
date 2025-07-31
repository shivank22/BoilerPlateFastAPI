# tests/test_users.py

from fastapi.testclient import TestClient
from app import app
import pytest

client = TestClient(app)

def fake_verify_azure_identity():
    return True

@pytest.fixture(autouse=True)
def patch_auth(monkeypatch):
    monkeypatch.setattr("routes.users.verify_azure_identity", fake_verify_azure_identity)

def test_create_user():
    payload = {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 30
    }

    response = client.post("/users/", json=payload)
    assert response.status_code == 201
    assert response.json()["user"]["email"] == "alice@example.com"
