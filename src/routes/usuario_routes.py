from src.controllers.usuario_controller import UsuarioController, UsuarioControllerPost, UsuarioControllerPut, UsuarioControllerLogin

def UsuarioRoutes(api):
    api.add_resource(UsuarioController, '/usuario/<int:idusuario>')
    api.add_resource(UsuarioControllerPost, '/usuario')
    api.add_resource(UsuarioControllerPut, '/usuario')
    api.add_resource(UsuarioControllerLogin, '/login')