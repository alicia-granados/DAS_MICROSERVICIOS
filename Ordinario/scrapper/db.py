import pymongo

# Conectarnos con el contenedor de mongo
mongo_cliente =pymongo.MongoClient()

# Pasar las credenciales para acceder
mongo_cliente =pymongo.MongoClient("mongodb://mongo_db:27017/",username='foo',password='bar123') 

# Crear base de datos
db = mongo_cliente["Libreria"]