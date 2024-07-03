from src.common.utils import api
from flask_restx import fields

#modelo para retornar información - - GET - PUT
GeneroSwagger = api.model('GeneroSwagger', {
    "IDGENERO": fields.Integer,
    "NOMBRE": fields.String
})

#modelo para recibir información al crear Genero - - POST
GeneroPostSwagger = api.model('GeneroPostSwagger', {
    "NOMBRE": fields.String
})