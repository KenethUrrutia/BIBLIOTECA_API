from .usuario_routes import UsuarioRoutes
from .genero_routes import GeneroRoutes
from .estado_routes import EstadoRoutes
from .libro_routes import LibroRoutes
from .prestamo_routes import PrestamoRoutes

def Routes(app): 
    UsuarioRoutes(app)
    GeneroRoutes(app)
    EstadoRoutes(app)
    LibroRoutes(app)
    PrestamoRoutes(app)
