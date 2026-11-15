from fastapi.testclient import TestClient
from api import app
client = TestClient(app)
def test_compra_exitosa():
    response = client.post("/compra", json={"precio": 200, "descuento": 25})
    assert response.status_code == 200
    assert response.json() == {"total": 174.0}
def test_compra_precio_invalido():
    response = client.post("/compra", json={"precio": -50, "descuento": 10})
    assert response.status_code == 400
def test_compra_descuento_invalido():
    response = client.post("/compra", json={"precio": 100, "descuento": 150})
    assert response.status_code == 400
