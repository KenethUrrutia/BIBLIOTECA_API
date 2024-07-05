from src.common.utils import api
from flask_restx import fields

#modelo para retornar información 
EstadoSwagger = api.model('EstadoSwagger', {
    "IDESTADO": fields.Integer,
    "NOMBRE": fields.String
})

#modelo para recibir información al crear Usuario - - POST
EstadoPostSwagger = api.model('EstadoPostSwagger', {
    "NOMBRE": fields.String
})

