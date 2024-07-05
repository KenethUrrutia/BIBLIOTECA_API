from .usuario_routes import UsuarioRoutes
from .genero_routes import GeneroRoutes
from .estado_routes import EstadoRoutes
from .libro_routes import LibroRoutes
from .prestamo_routes import PrestamoRoutes

def Routes(app): 
    #Rutas de Usuario
    UsuarioRoutes(app)

    #Rutas de Genero
    GeneroRoutes(app)

    #Rutas de Estado
    EstadoRoutes(app)
    
    #Rutas de Libro
    LibroRoutes(app)

    #Rutas de Prestamo
    PrestamoRoutes(app)
