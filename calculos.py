def calcular_descuento(precio, porcentaje):
    # Formula corregida: resta correctamente el descuento
    return precio - (precio * (porcentaje / 100))
def calcular_iva(precio, tasa_iva=16):
    return precio + (precio * (tasa_iva / 100))
