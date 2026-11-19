from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
VERSION = "2.0.0"
app = FastAPI(title="Tienda API", version=VERSION)
class Compra(BaseModel):
    precio: float
    descuento: float
@app.get("/health")
def health_check():
    return {"status": "ok", "servicio": "tienda-api"}
@app.get("/version")
def get_version():
    return {"version": VERSION, "descripcion": "Version 2 con mejoras en respuesta de estado"}
@app.post("/compra")
def procesar_compra(compra: Compra):
    if compra.precio < 0:
        raise HTTPException(400, "Precio invalido")
    if not 0 <= compra.descuento <= 100:
        raise HTTPException(400, "Descuento invalido")
    subtotal = compra.precio * (1 - compra.descuento / 100)
    total = round(subtotal * 1.16, 2)
    return {"total": total, "version": VERSION}
