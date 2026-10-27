import pytest
from main import procesar_venta
def test_integracion_venta_exitosa():
    # Caso donde el flujo completa el try
    resultado = procesar_venta(100, 20, 16)
    assert resultado["estado"] == "exito"
    assert resultado["total"] == 92.80
def test_integracion_venta_excepcion_precio_negativo():
    # Caso donde se dispara el except por validacion
    resultado = procesar_venta(-100, 10, 16)
    assert resultado["estado"] == "error"
    assert "El precio base no puede ser negativo" in resultado["mensaje"]
def test_integracion_venta_excepcion_descuento_invalido():
    # Caso except por descuento mayor a 100
    resultado = procesar_venta(200, 150, 16)
    assert resultado["estado"] == "error"
    assert "El descuento debe estar entre 0 y 100" in resultado["mensaje"]
