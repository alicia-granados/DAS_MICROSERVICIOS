import pika
import pymongo
import json

# Conectarnos con el contenedor de mongo
mongo_cliente =pymongo.MongoClient()

# Pasar las credenciales para acceder
mongo_cliente =pymongo.MongoClient("mongodb://mongo_db:27017/",username='foo',password='bar123') 

# Crear base de datos
db = mongo_cliente["Libreria"]

#Se configura la conexion para el consumidor en rabbitmq
credentials=pika.PlainCredentials('foo','baz123')
parameters=pika.ConnectionParameters(host='rabbit',port=5672,virtual_host='/',credentials=credentials)
connection=pika.BlockingConnection(parameters)


channel=connection.channel()
channel.queue_declare(queue='libros')

def callback(ch,method,properties,body):
    print(f' [x] received {body}')
    data=json.loads(body)
    id = db.libros.insert_one(data)

channel.basic_consume(queue='libros',on_message_callback=callback,auto_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()