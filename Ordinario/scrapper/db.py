import pymongo

# Connect with the mongo container
mongo_cliente =pymongo.MongoClient()

# Pass the credentials to access
mongo_cliente =pymongo.MongoClient("mongodb://mongo_db:27017/",username='foo',password='bar123') 

# Create database
db = mongo_cliente["Libreria"]