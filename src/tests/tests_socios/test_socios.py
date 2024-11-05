from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_listar_socios():
    response = client.get("/socios/")
    assert response.status_code == 200
    print(response.json())
       
