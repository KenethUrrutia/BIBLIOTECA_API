from src.controllers.estado_controller import EstadoController, EstadoControllerById
from flask_restx import Namespace

def EstadoRoutes(api):
    #namespace para notas
    ns_nota = Namespace('estado', description='EndPoints para Estado')

    #endpoint para listar estados - - GET  
    #endpoint para crear estado - - POST 
    #endpoint para actualizar estado - - PUT 
    ns_nota.add_resource(EstadoController, '')


    #endpoint para eliminar estado por id - - DELETE 
    #endpoint para obtener estado por id - - GET  
    ns_nota.add_resource(EstadoControllerById, '/<int:idestado>')

    #agregar namespace a la api
    api.add_namespace(ns_nota)