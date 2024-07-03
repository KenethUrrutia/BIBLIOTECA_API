from src.controllers.genero_controller import GeneroController, GeneroControllerById
from flask_restx import Namespace

def GeneroRoutes(api):
    #
    ns_genero = Namespace('genero', description='EndPoints para Genero')

    #endpoint para listar generos - - GET
    #endpoint para crear genero - - POST
    #endpoint para actualizar genero - - PUT
    ns_genero.add_resource(GeneroController, '')

    #endpoint para obtener genero por id - - GET
    #endpoint para eliminar genero por id - - DELETE
    ns_genero.add_resource(GeneroControllerById, '/<int:idgenero>')

    api.add_namespace(ns_genero)