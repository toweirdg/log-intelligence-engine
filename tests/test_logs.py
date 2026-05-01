from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_log():
	response = client.post("/logs", json={
		"message": "test error",
		"level": "ERROR"
	})

	assert response.status_code == 200
	assert "id" in response.json()
