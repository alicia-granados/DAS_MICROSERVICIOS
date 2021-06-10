# Import the required Python modules and Flask libraries
from flask import Flask, jsonify, request, Response, render_template
from flask_cors import CORS,cross_origin
import flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import json_util
from bson.objectid import ObjectId
import json
import pika


# Create a Flask app object
app = Flask(__name__)

cors= CORS(app)
app.config['CORS_HEADERS']= 'Content-Type'
# Configure the Flask application to connect with the MongoDB server
app.config['MONGO_URI'] = "mongodb://foo:bar123@mongo_db:27017/Libreria?authSource=admin"
app.config['MONGO_HOST'] = 'mongo_db'
app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = 'Libreria'
app.config['MONGO_USERNAME'] = 'foo'
app.config['MONGO_PASSWORD'] = 'bar123'
app.config['MONGO_AUTH_SOURCE'] = 'admin'


# Connect to MongoDB using Flask's PyMongo wrapper
mongo = PyMongo(app)

#Render and show the template "home.html"
@app.route('/')
def home():
    return render_template('home.html')

# Insert Book
@app.route('/libros', methods=['POST'])
@cross_origin()
def create_book():
    #///////////////////////////RabbitMQ ConfiguracionInicial////////////////////////
    credentials=pika.PlainCredentials('foo','baz123')
    parameters=pika.ConnectionParameters(host='rabbit',port=5672,virtual_host='/',credentials=credentials)
    connection=pika.BlockingConnection(parameters)


    channel=connection.channel()
    channel.queue_declare(queue='libros')
    # Receiving Data
    title = request.json['title']
    subtitle = request.json['subtitle']
    authors = request.json['authors']
    publisher = request.json['publisher']
    publishedDate = request.json['publishedDate']
    description = request.json['description']
    pageCount = request.json['pageCount']
    categories = request.json['categories']
    # If the previous variables are true, Insert to Mongo
    if title and subtitle and authors and publisher and publishedDate and description and pageCount and categories:
        #////////////Se crea mensaje para rabbit y se manda en caso de querer hacerlo sin rabbit comentar esta parte y descomentar la sigueinte////////////////////////////////
        message={
                'title': title, 
                'subtitle': subtitle, 
                'authors': authors,
                'publisher': publisher, 
                'publishedDate': publishedDate, 
                'description': description,
                'pageCount': pageCount, 
                'categories': categories
            }
        channel.basic_publish(exchange='',routing_key='libros',body=json.dumps(message))
        connection.close()
#//////////////////////////////////////////////////////////////////////////////////////////

#        id = mongo.db.libros.insert_one(
 #           {   # Assigns values of JSON variables
  #              'title': title, 
   #             'subtitle': subtitle, 
    #            'authors': authors,
     #           'publisher': publisher, 
      #          'publishedDate': publishedDate, 
       #         'description': description,
        #        'pageCount': pageCount, 
         #       'categories': categories
          #  })
        # Serializes data to JSON
        response = jsonify({
            '_id': str(id),
            'title': title, 
            'subtitle': subtitle, 
            'authors': authors,
            'publisher': publisher, 
            'publishedDate': publishedDate, 
            'description': description,
            'pageCount': pageCount, 
            'categories': categories
        })
        # Add the status of the request
        response.status_code = 201
        return response # Return JSON
    else:
        return not_found()

# Show all books
@app.route('/libros', methods=['GET'])
@cross_origin()
def get_libros():
    books = mongo.db.libros.find() # Search  books
    response = json_util.dumps(books, indent=2) ## Return a "pretty json"
    return Response(response, mimetype="application/json")  # Content type will be returned

# Show a book
@app.route('/libros/<id>', methods=['GET'])
@cross_origin()
def get_libro(id):
    print(id)# imprime id
    book = mongo.db.libros.find_one({'_id': ObjectId(id), }) # Search a book
    response = json_util.dumps(book, indent=2) ## Return JSON
    return Response(response, mimetype="application/json")  # Content type will be returned

# Delet a book
@app.route('/libros/<id>', methods=['DELETE'])
@cross_origin()
def delete_libro(id):
    mongo.db.libros.delete_one({'_id': ObjectId(id)}) #Delete a book
    response = jsonify({'message': 'Book' + id + ' Deleted Successfully'}) # Response id book deleted
    response.status_code = 200  # Add the status of the request
    return response   # Return JSON

# Update a book
@app.route('/libros/<_id>', methods=['PUT'])
@cross_origin()
def update_libro(_id):
    # Receiving Data
    title = request.json['title']
    subtitle = request.json['subtitle']
    authors = request.json['authors']
    publisher = request.json['publisher']
    publishedDate = request.json['publishedDate']
    description = request.json['description']
    pageCount = request.json['pageCount']
    categories = request.json['categories']
    # If the previous variables are true, Update to Mongo
    if title and subtitle and authors and publisher and publishedDate and description and pageCount and categories and _id:
        mongo.db.libros.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
            {'$set': {
                'title': title, 
                 'subtitle': subtitle, 
                 'authors': authors,
                 'publisher': publisher, 
                 'publishedDate': publishedDate, 
                 'description': description,
                 'pageCount': pageCount, 
                 'categories': categories
                }
            })
        # Serializes data to JSON
        response = jsonify({'message': 'Book' + _id + 'Updated Successfuly'})
        response.status_code = 200 # Add the status of the request
        return response  # Return JSON of the book update
    else:
       return not_found()

# Show a "not found" message
@app.errorhandler(404)
@cross_origin()
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404 # Add the status of the request
    }
    response = jsonify(message)   # Serializes data to JSON
    response.status_code = 404  #  Add the status of the request
    return response  # Return JSON 

#Show a "not found page" template
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('not_found.html'), 404


if __name__ == "__main__":
    
    app.run(debug=True) # The run configuration




 