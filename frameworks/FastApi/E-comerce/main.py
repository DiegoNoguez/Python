from fastapi import FastAPI

app = FastAPI()

productos = []

@app.get("/productos")
def listar_productos():
    return {"productos":["laptop", "Movil", "Tablet"]}

@app.post("/productos")
def agregar_producto(nombre:str):
    productos.append(nombre)
    return {"message":"Producto agregado", "producto": nombre}

@app.put("/productos/{id}")
def actualizar_producto(id : int, nombre:str):
    productos[id] = nombre
    return {"message":"Producto actualizado", "producto": nombre}

@app.delete("/producto/{id}")
def eliminar_producto(id:int):
    eliminado = productos.pop(id)
    return {"message":"Producto Eliminado", "producto": eliminado}