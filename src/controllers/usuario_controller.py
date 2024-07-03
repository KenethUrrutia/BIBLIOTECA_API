from flask_restx import Resource
from flask import request
from src.common.utils import db
from src.models.usuario_model import UsuarioModel  
from src.schemas.usuario_schema import UsuarioSchema, UsuarioSchemaValidar, UsuarioSchemaLogin
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token
import datetime
from flask_jwt_extended import jwt_required

class UsuarioController(Resource):
    @jwt_required()
    def get(self, idusuario):
        try: 
            usuariodb = db.session.execute(db.select(UsuarioModel).where(UsuarioModel.IDUSUARIO == idusuario)).scalar_one()
            usuario = UsuarioSchema().dump(usuariodb)
            return usuario, 200
        except NoResultFound:
            return {'message': 'Usuario no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500
        
class UsuarioControllerPost(Resource):
    @jwt_required()
    def post(self):
        try:
            usuarioValidar = UsuarioSchemaValidar(exclude=['IDUSUARIO'])
            usuarioValidar.load(request.json)

            usuarioValidar = UsuarioSchema()
            usuario = usuarioValidar.load(request.json)

            db.session.add(usuario)
            db.session.commit()
            return UsuarioSchema().dump(usuario), 201
        
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 500
        
class UsuarioControllerPut(Resource):
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
            return UsuarioSchema().dump(usuariodb), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'Usuario no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500
        

class UsuarioControllerLogin(Resource) :
    def post(self):
        try:
            usuarioSchema = UsuarioSchemaLogin()
            usuario = usuarioSchema.load(request.json)
            print(usuario)

            #existencia de usuario
            usuariodb = db.session.execute(db.select(UsuarioModel).where(UsuarioModel.CORREO == usuario["CORREO"]).where(UsuarioModel.PASSWORD == usuario["PASSWORD"])).scalar_one()
            usuarioSchema = UsuarioSchema().dump(usuariodb)
            access_token = create_access_token(identity=usuarioSchema, expires_delta=datetime.timedelta(days=1))
            return access_token, 200
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'El correo o la contraseña no coinciden'}, 404
        except Exception as e:
            return {'message': str(e)}, 500