#Para hacer una API hay que instalar en el visual studio code el flask

from flask import Flask, jsonify, request, render_template
import sys
import logging
app = Flask (__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

#importar los datos libros
from libros import libros

#ruta de saludar a la pagina
@app.route('/')
def saludo():
    print('Bienvenido a mi API REST')
#ruta.
@app.route('/libreria')
#mostrar los datos de mi json.
def getLibreria():
    return jsonify({"libros": libros, 'mensaje': 'Lista de libros'})

# Sacar la informacion de un objeto pidiendo el nombre del titulo del libro.
@app.route('/libreria/<string:libros_titulo>')
def getLibros(libros_titulo): 
    buscartitulo = [libro for libro in libros if libro['titulo'] == libros_titulo]

    if (len(buscartitulo) > 0):
       return jsonify({"libros": buscartitulo[0]})
    return jsonify({"mensaje": 'El titulo introducido no encontrado'})

#añadir datos en la tabla libros.
@app.route('/libreria', methods=['POST'])
def añadirLibros():
    añadir_lista = {
        'titulo': request.json['titulo'],
        'autor': request.json['autor'],
        'editorial': request.json['editorial'],
        'ISBN': request.json['ISBN']
    }
    libros.append(añadir_lista)
    return jsonify({'mensaje': 'El libro fue añadido', 'libros': libros})

#Actualizar datos de libros del atributo ISBN
@app.route('/libreria/<string:libros_autor>', methods=['PUT'])
def ISBNlibros(libros_autor):
    buscarautor= [libro for libro in libros if libro['ISBN'] == libros_autor]
    if (len(buscarautor) > 0):
        buscarautor[0] ['ISBN'] = request.json['ISNB']
        buscarautor[0]['titulo'] = request.json['titulo']
        buscarautor[0]['autor'] = request.json['autor']
        buscarautor[0]['editorial'] = request.json['editorial']
        return jsonify ({'mensaje': 'La lista actualizada', 
                         'libros': buscarautor[0]
        })
    return jsonify({'mensaje': 'Libro no encontrado'})

#Eliminar la lista libros
@app.route('/libreria/<string:libros_autor>', methods=["delete"])
def eliminarlibros(libros_autor):
    buscarlibros=[libro for libro in libros if libro['autor'] == libros_autor]
    if (len(buscarlibros) > 0):
        libros.remove(buscarlibros[0])
        return jsonify({
            'mensaje': 'libro eliminado',
            'libros': libros
        })
    return jsonify({'mensaje': 'producto no encontrado'})

if __name__ == '__main__':
    app.debug = True
    app.run()
    api = api(app)