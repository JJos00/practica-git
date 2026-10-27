import pytest
from main import procesar_venta
def test_sistema_flujo_completo_sin_descuento():
    # Sistema operando con 0% de descuento
    res = procesar_venta(500, 0, 16)
    assert res["estado"] == "exito"
    assert res["total"] == 580.0
def test_sistema_flujo_completo_con_descuento_maximo():
    # Sistema operando con 100% de descuento
    res = procesar_venta(300, 100, 16)
    assert res["estado"] == "exito"
    assert res["total"] == 0.0
