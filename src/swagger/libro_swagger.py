from src.common.utils import api
from flask_restx import fields

#modelo para retornar información
LibroSwagger = api.model('LibroSwagger', {
    "IDLIBRO": fields.Integer,
    "TITULO": fields.String,
    "AUTOR": fields.String,
    "ANIO_PUBLICACION": fields.Date,
    "IDGENERO": fields.Integer,
})

#modelo para recibir información al crear Libro
LibroPostSwagger = api.model('LibroPostSwagger', {
    "TITULO": fields.String,
    "AUTOR": fields.String,
    "ANIO_PUBLICACION": fields.Date,
    "IDGENERO": fields.Integer,
})