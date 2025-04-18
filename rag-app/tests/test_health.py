from fastapi.testclient import TestClient
from server.src.main import app     # <- fuld sti

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

