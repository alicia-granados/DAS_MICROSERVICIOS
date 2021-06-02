from os import times
from db import db
import json
import urllib.request
 
# Se conecta a la API de Google y la abre como un archivo, después lo que se trae de la API lo convierte en un JSON
 
with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=search+terms&AIzaSyDqHYhoLtp0dR28gILA4OJFWoxYxJiDu6Q") as url:
 
    data = json.loads(url.read().decode()) # Convierte el JSON a string
    # print(data) Imprime data
 
# Después a la variable dictlibros, le agrega la llave "ítems" del json data
dictlibros = {}

dictlibros = data['items']
 
dictLibrosDos = {}
 
dictLibrosTres = {}

# Itera el diccionario dictlibros para agregar más valores al nuevo diccionario dictLibrosDos
for i in range(dictlibros.__len__() - 1):
     dictLibrosDos[i] = dictlibros[i]

# Agrega todos los libros al dicLibrosDos 
for l in range(dictLibrosDos.__len__()):
    
    # Extrae los campos necesarios de la API
    title = dictLibrosDos[l]["volumeInfo"].get("title", "No title here")
    subtitle = dictLibrosDos[l]["volumeInfo"].get("subtitle", "No subtitle here")
    authors = dictLibrosDos[l]["volumeInfo"].get("authors", "No authors here")
    publisher = dictLibrosDos[l]["volumeInfo"].get("publisher", "No publisher here")
    publishedDate = dictLibrosDos[l]["volumeInfo"].get("publishedDate", "No published date here")
    description = dictLibrosDos[l]["volumeInfo"].get("description", "No description here")
    pageCount = dictLibrosDos[l]["volumeInfo"].get("pageCount", "No pages count here")
    categories = dictLibrosDos[l]["volumeInfo"].get("categories", "No categories here")
   
    # Se guardan los datos extraidos al nuevo diccionario
    dictLibrosTres[l] = {
        "title": title,
        "subtitle":subtitle,
        "authors": authors,
        "publisher":publisher,
        "publishedDate":publishedDate,
        "description": description,
        "pageCount": pageCount,
        "categories": categories
    }
    
  
for j in range(dictLibrosTres.__len__() - 1):  # Recorre diccinario de dicLibrosTres 

    print(db.libros.insert_one(dictLibrosTres[j]))  # Inserta libros a la colección