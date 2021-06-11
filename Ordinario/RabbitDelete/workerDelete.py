import pika
import pymongo
from bson.objectid import ObjectId
import json

# Connect to Mongo
mongo_cliente =pymongo.MongoClient()

# Pass Mongo Credentials
mongo_cliente =pymongo.MongoClient("mongodb://mongo_db:27017/",username='foo',password='bar123') 

# Create or get the database
db = mongo_cliente["Libreria"]

#Configuration for the RabbitMQ consumer
credentials=pika.PlainCredentials('foo','baz123')
parameters=pika.ConnectionParameters(host='rabbit',port=5672,virtual_host='/',credentials=credentials)
connection=pika.BlockingConnection(parameters)


channel=connection.channel()
channel.queue_declare(queue='librosDelete')

def callback(ch,method,properties,body):
    print(f' [x] received {body}')
    data=json.loads(body)
    id = db.libros.delete_one({'_id': ObjectId(data['_id'])})

channel.basic_consume(queue='librosDelete',on_message_callback=callback,auto_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()