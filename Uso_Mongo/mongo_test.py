from pymongo import MongoClient  # importacion de la libreria de pymongo para hacer peticiones y  modificaciones a la bd


# Establecenos la conexion a la base 
#client = MongoClient("mongodb://localhost:27017")

# Linea de conexion cuando se solicita contra de root en mongo 
client = MongoClient("mongodb://root:1234@localhost:27017/")
# Probar la conexion 
#print(f'Base de datos disponibles: ')
#print(client.list_database_names())


# Creacion de una BD en mongo 

# Lo siguiente no crea nada de basee de datos aun solo dice con que y como trabjar . 
# Seleccion de un bd
db = client["prueba1"]

# Seleccionar coleccion
user = db["users"]

print("Conectado correctamente")

user = {
    "nombre":"Diego",
    "edad"
}

