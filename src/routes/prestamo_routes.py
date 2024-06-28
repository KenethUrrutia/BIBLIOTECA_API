from src.controllers.prestamo_controller import PrestamoController, PrestamoControllerPost

def PrestamoRoutes(api):
    api.add_resource(PrestamoController, '/prestamos')
    api.add_resource(PrestamoControllerPost, '/prestamo')