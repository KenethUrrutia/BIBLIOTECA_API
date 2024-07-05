from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restx import Resource
from marshmallow import ValidationError
from src.common.utils import db, api, RespuestaGenerica
from src.models.usuario_model import UsuarioModel  
from src.schemas.usuario_schema import UsuarioSchema, UsuarioSchemaValidar, UsuarioSchemaLogin
from src.swagger.usuario_swagger import UsuarioSwagger, UsuarioPostSwagger, UsuarioLoginSwagger, UsuarioLoginResponseSwagger
from sqlalchemy.orm.exc import NoResultFound
import datetime

class UsuarioControllerById(Resource):
     #interfaz para obtener un USUARIO por id
    @api.doc(description='Obtiene un registro de USUARIO por su ID')
    @api.param('idusuario', 'ID del USUARIO')
    @api.response(200, "Se obtuvo con éxito el registro de USUARIO", UsuarioSwagger, as_list=True)
    @api.response(404, "No se encontró el registro de USUARIO", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def get(self, idusuario):
        try: 
            usuariodb = db.session.execute(db.select(UsuarioModel).where(UsuarioModel.IDUSUARIO == idusuario)).scalar_one()
            usuario = UsuarioSchema(exclude=['PASSWORD']).dump(usuariodb)
            return usuario, 200
        except NoResultFound:
            return {'message': 'Usuario no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503

class UsuarioController(Resource):
    #interfaz para crear un USUARIO
    @api.doc(description='Crea un nuevo registro de USUARIO')
    @api.expect(UsuarioPostSwagger)
    @api.response(201, "Se crea con éxito el nuevo registro de USUARIO", UsuarioSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def post(self):
        try:
            usuarioValidar = UsuarioSchemaValidar(exclude=['IDUSUARIO'])
            usuarioValidar.load(request.json)

            usuarioValidar = UsuarioSchema()
            usuario = usuarioValidar.load(request.json)

            db.session.add(usuario)
            db.session.commit()
            return UsuarioSchema(exclude=['PASSWORD']).dump(usuario), 201
        
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 503
        
    #interfaz para actualizar un USUARIO
    @api.doc(description='Actualiza un registro de USUARIO')
    @api.expect(UsuarioSwagger)
    @api.response(200, "Se actualizó con éxito el registro de USUARIO", UsuarioSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def put(self):
        try:
            usuarioValidar = UsuarioSchemaValidar()
            usuario = usuarioValidar.load(request.json)
            
            usuariodb = db.session.execute(db.select(UsuarioModel).where(UsuarioModel.IDUSUARIO == usuario["IDUSUARIO"])).scalar_one()
            usuariodb.NOMBRE = usuario["NOMBRE"]
            usuariodb.APELLIDO = usuario["APELLIDO"]
            usuariodb.EDAD = usuario["EDAD"]
            usuariodb.CORREO = usuario["CORREO"]
            usuariodb.PASSWORD = usuario["PASSWORD"]

            db.session.commit()
            return UsuarioSchema(exclude=['PASSWORD']).dump(usuariodb), 200
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'Usuario no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
        
    

class UsuarioControllerLogin(Resource) :
    @api.doc(description='Login de usuario')
    @api.expect(UsuarioLoginSwagger)
    @api.response(200, "Se obtiene con éxito el token de acceso", UsuarioLoginResponseSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(404, "Usuario no encontrado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    def post(self):
        try:
            usuarioSchema = UsuarioSchemaLogin()
            usuario = usuarioSchema.load(request.json)
            print(usuario)

            #existencia de usuario
            usuariodb = db.session.execute(db.select(UsuarioModel).where(UsuarioModel.CORREO == usuario["CORREO"]).where(UsuarioModel.PASSWORD == usuario["PASSWORD"])).scalar_one()
            usuarioSchema = UsuarioSchema().dump(usuariodb)
            access_token = create_access_token(identity=usuarioSchema, expires_delta=datetime.timedelta(days=1))
            return {'token' : access_token}, 200
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'El correo o la contraseña no coinciden'}, 404
        except Exception as e:
            return {'message': str(e)}, 503