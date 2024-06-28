from src.controllers.libro_controller import LibroController, LibroControllerGetById, LibroControllerPost, LibroControllerPut, LibroControllerDelete

def LibroRoutes(api):
    api.add_resource(LibroController, '/libros')
    api.add_resource(LibroControllerGetById, '/libro/<int:idlibro>')
    api.add_resource(LibroControllerPost, '/libro')
    api.add_resource(LibroControllerPut, '/libro')
    api.add_resource(LibroControllerDelete, '/libro/<int:idlibro>')