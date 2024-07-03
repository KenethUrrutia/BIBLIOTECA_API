from src.controllers.libro_controller import LibroController, LibroControllerById   
from flask_restx import Namespace

def LibroRoutes(api):
    #namespace para notas
    ns_libro = Namespace('libro', description='EndPoints para Libro')

    #endpoint para listar libros - - GET  
    #endpoint para crear libro - - POST 
    #endpoint para actualizar libro - - PUT 
    ns_libro.add_resource(LibroController, '')

    #endpoint para eliminar libro por id - - DELETE
    #endpoint para obtener libro por id - - GET
    ns_libro.add_resource(LibroControllerById, '/<int:idlibro>')

    #agregar namespace a la api
    api.add_namespace(ns_libro)
