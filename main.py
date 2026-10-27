from calculos import calcular_descuento, calcular_iva
def procesar_venta(precio_base, porcentaje_descuento, tasa_iva=16):
    """
    Calcula el total a pagar aplicando primero descuento y luego IVA.
    Lanza ValueError si los datos son invalidos.
    """
    try:
        if precio_base < 0:
            raise ValueError("El precio base no puede ser negativo")
        if porcentaje_descuento < 0 or porcentaje_descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        
        precio_con_desc = calcular_descuento(precio_base, porcentaje_descuento)
        total = calcular_iva(precio_con_desc, tasa_iva)
        return {"estado": "exito", "total": round(total, 2)}
    except Exception as e:
        return {"estado": "error", "mensaje": str(e)}
if __name__ == "__main__":
    # Caso Try (Exitoso)
    print("Venta normal:", procesar_venta(100, 20))
    # Caso Except (Error controlado)
    print("Venta con error:", procesar_venta(-50, 10))
