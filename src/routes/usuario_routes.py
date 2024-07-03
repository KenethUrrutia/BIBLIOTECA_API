from src.controllers.usuario_controller import UsuarioController, UsuarioControllerById, UsuarioControllerLogin
from flask_restx import Namespace
def UsuarioRoutes(api):

    #namespace para usuario
    ns_usuario = Namespace('usuario', description='EndPoints para Usuario')
    #endpoint para crear usuario - - POST
    #endpoint para actualizar usuario - - PUT
    ns_usuario.add_resource(UsuarioController, '')
    #endpoint para obtener usuario por id - - GET
    ns_usuario.add_resource(UsuarioControllerById, '/<int:idusuario>')

    #namespace para login
    ns_usuario_login = Namespace('login', description='EndPoints para Login de Usuario')
    #endpoint para login - - POST
    ns_usuario_login.add_resource(UsuarioControllerLogin, '')


    #agregar namespace a la api
    api.add_namespace(ns_usuario)
    api.add_namespace(ns_usuario_login)