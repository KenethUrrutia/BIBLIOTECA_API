from src.controllers.prestamo_controller import PrestamoController
from flask_restx import Namespace

def PrestamoRoutes(api):
    #namespace para notas
    ns_prestamo = Namespace('prestamo', description='EndPoints para Prestamo')

    #endpoint para listar prestamos - - GET
    #endpoint para crear prestamo - - POST
    ns_prestamo.add_resource(PrestamoController, '')
    
    #agregar namespace a la api
    api.add_namespace(ns_prestamo)
