from fastapi.testclient import TestClient

from ragforge.main import app


def test_liveness_endpoint() -> None:
    with TestClient(app) as client:
        response = client.get("/health/live")
        assert response.status_code == 200
        assert response.json() == {
            "status": "ok",
            "service": "ragforge-api",
        }