from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    r = client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "123456"
    })
    assert r.status_code == 200

    r = client.post("/auth/login", data={
        "username": "test@test.com",
        "password": "123456"
    })
    assert "access_token" in r.json()
