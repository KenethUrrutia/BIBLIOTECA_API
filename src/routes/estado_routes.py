from src.controllers.estado_controller import EstadoController, EstadoControllerPost, EstadoControllerPut, EstadoControllerDelete, EstadoControllerGetById

def EstadoRoutes(api):
    api.add_resource(EstadoController, '/estados')
    api.add_resource(EstadoControllerPost, '/estado')
    api.add_resource(EstadoControllerPut, '/estado')
    api.add_resource(EstadoControllerDelete, '/estado/<int:idestado>')
    api.add_resource(EstadoControllerGetById, '/estado/<int:idestado>')