from os import times
from db import db
import json
import urllib.request
 
# It connects to the Google API and opens it as a file, then what is brought from the API converts it into a JSON
 
with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=search+terms&AIzaSyDqHYhoLtp0dR28gILA4OJFWoxYxJiDu6Q") as url:
 
    data = json.loads(url.read().decode()) # Convert the JSON to string
    # print(data) Print data
 
# After the variable dictlibros, add the key "items" of the json data
dictlibros = {}

dictlibros = data['items']
 
dictLibrosDos = {}
 
dictLibrosTres = {}

# Iterate the dictionary dictlibros to add more values ​​to the new dictionary dictLibrosDos
for i in range(dictlibros.__len__() - 1):
     dictLibrosDos[i] = dictlibros[i]

# Add all books to dicLibrosDos
for l in range(dictLibrosDos.__len__()):
    
    # Extract the required fields from the API
    title = dictLibrosDos[l]["volumeInfo"].get("title", "")
    subtitle = dictLibrosDos[l]["volumeInfo"].get("subtitle", "")
    authors = dictLibrosDos[l]["volumeInfo"].get("authors", "")
    publisher = dictLibrosDos[l]["volumeInfo"].get("publisher", "")
    publishedDate = dictLibrosDos[l]["volumeInfo"].get("publishedDate", "")
    description = dictLibrosDos[l]["volumeInfo"].get("description", "")
    pageCount = dictLibrosDos[l]["volumeInfo"].get("pageCount", "")
    categories = dictLibrosDos[l]["volumeInfo"].get("categories", "")
   
    # The extracted data is saved to the new dictionary
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
    
  
for j in range(dictLibrosTres.__len__() - 1):  # Go through the dictionary of dicLibrosTres

    print(db.libros.insert_one(dictLibrosTres[j]))  # Insert books to the collection