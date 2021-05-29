import pymongo
import json,urllib.request

conn=pymongo.MongoClient()
conn=pymongo.MongoClient("mongodb://mongo_db:27017/",username='foo',password='bar123')
db=conn["Libreria"]

dictlibros={}

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=search+terms&AIzaSyDqHYhoLtp0dR28gILA4OJFWoxYxJiDu6Q") as url:
    data=json.loads(url.read().decode())
    #print(data)

dictlibros=data['items']

dictLibrosDos={}

for i in range(dictlibros.__len__() - 1):
    dictLibrosDos[i]=dictlibros[i]

for l in range(dictLibrosDos.__len__() - 1):
    print(db.libros.insert_one(dictLibrosDos[l]))

#for libroInfo in dictLibrosDos:
 #   print(libroInfo)
    # informacion=libroInfo['volumeInfo']
    # autor=informacion['authors']
    # print(db.libros.insert_one(
    #     [
    #         {
    #             "Titulo":informacion['title'],
    #             "Autor":autor[0],
    #             "Publicador":informacion['publisher'],
    #             "FechaDePublicacion":informacion['publishedDate'],
    #             "Descripcion":informacion['description']
    #         }
    #     ]
    # ))