from src.controllers.genero_controller import GeneroController, GeneroControllerPost, GeneroControllerPut, GeneroControllerDelete, GeneroControllerGetById

def GeneroRoutes(api):
    api.add_resource(GeneroController, '/generos')
    api.add_resource(GeneroControllerPost, '/genero')
    api.add_resource(GeneroControllerPut, '/genero')
    api.add_resource(GeneroControllerDelete, '/genero/<int:idgenero>')
    api.add_resource(GeneroControllerGetById, '/genero/<int:idgenero>')