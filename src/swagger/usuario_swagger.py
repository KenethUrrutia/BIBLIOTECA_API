from src.common.utils import api
from flask_restx import fields

#modelo para retornar información - - GET - PUT 
UsuarioSwagger = api.model('UsuarioSwagger', {
    "IDUSUARIO": fields.Integer,
    "NOMBRE": fields.String,
    "APELLIDO": fields.String,
    "EDAD": fields.Integer,
    "CORREO": fields.String,
})

#modelo para recibir información al crear Usuario - - POST
UsuarioPostSwagger = api.model('UsuarioPostSwagger', {
    "NOMBRE": fields.String,
    "APELLIDO": fields.String,
    "EDAD": fields.Integer,
    "CORREO": fields.String,
    "PASSWORD": fields.String
})

#modelo para recibir información login de Usuario - - POST
UsuarioLoginSwagger = api.model('UsuarioLoginSwagger', {
    "CORREO": fields.String,
    "PASSWORD": fields.String
})

#modelo para retornar información login de Usuario - - POST
UsuarioLoginResponseSwagger = api.model('UsuarioLoginResponseSwagger', {
    "token": fields.String
})