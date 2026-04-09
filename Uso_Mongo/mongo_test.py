from pymongo import MongoClient 

# Establecenos la conexion a la base 
client = MongoClient("mongodb://localhost:27017")

# Probar la conexion 
print(f'Base de datos disponibles: ')
print(client.list_database_names())