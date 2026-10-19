def calcular_descuento(precio, porcentaje):
    # Error intencional: suma el descuento en lugar de restarlo
    return precio + (precio * (porcentaje / 100))
def calcular_iva(precio, tasa_iva=16):
    return precio + (precio * (tasa_iva / 100))
