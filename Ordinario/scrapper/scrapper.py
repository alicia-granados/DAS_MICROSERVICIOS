from db import db
import json,urllib.request


dictlibros = {} 

# Se conecta a la API de Google y la abre como un archivo, después lo que se trae de la API lo convierte en un JSON

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=search+terms&AIzaSyDqHYhoLtp0dR28gILA4OJFWoxYxJiDu6Q") as url:
    
    data = json.loads(url.read().decode())
    # print(data)

# Después a la variable dictlibros, le agrega la llave "ítems" del json data
dictlibros = data['items']

dictLibrosDos = {}

# Itera el diccionario dictlibros para agregar más valores al nuevo diccionario dictLibrosDos
for i in range(dictlibros.__len__() - 1):
    dictLibrosDos[i] = dictlibros[i]

for l in range(dictLibrosDos.__len__() - 1):
    print(db.libros.insert_one(dictLibrosDos[l]))  # Inserta a mongo
