from flask_restx import fields
from .estado_swagger import EstadoSwagger
from .libro_swagger import LibroSwagger
from .usuario_swagger import UsuarioSwagger
from src.common.utils import api


#modelo para retornar información
PrestamoSwagger = api.model('PrestamoSwagger', {
    "IDUSUARIO": fields.Integer,
    "IDLIBRO": fields.Integer,
	"IDPRESTAMO": fields.Integer,
    "FECHA_PRESTAMO": fields.Date,
    "FECHA_DEVOLUCION": fields.Date,
    "ESTADO": fields.String,
	"IDESTADO": fields.Integer
})

#modelo para recibir información al crear Prestamo
PrestamoCreateSwagger = api.model('PrestamoCreateSwagger', {
    "IDUSUARIO": fields.Integer,
    "IDLIBRO": fields.Integer,
    "FECHA_PRESTAMO": fields.Date,
    "FECHA_DEVOLUCION": fields.Date,
    "ESTADO": fields.String,
    "IDESTADO": fields.Integer
})

PrestamoPostSwagger = api.model('PrestamoPostSwagger', {
    "PRESTAMO": fields.Nested(PrestamoCreateSwagger),
    "USUARIO": fields.Nested(UsuarioSwagger),
    "LIBRO": fields.Nested(LibroSwagger),
    "ESTADO": fields.Nested(EstadoSwagger)
})

