from calculos import calcular_descuento, calcular_iva
def test_calcular_descuento():
    assert calcular_descuento(100, 20) == 80
    assert calcular_descuento(500, 10) == 450
def test_calcular_iva():
    assert calcular_iva(100) == 116
    assert calcular_iva(200, 16) == 232
