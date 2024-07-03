from src.common.utils import db
from src.schemas.prestamo_schema import PrestamoSchema, PrestamoSchemaValidar
from src.schemas.usuario_schema import UsuarioSchemaValidar, UsuarioSchema
from src.schemas.libro_schema import LibroSchemaValidar, LibroSchema
from src.schemas.estado_schema import EstadoSchemaValidar, EstadoSchema
from src.models.usuario_model import UsuarioModel
from src.models.libro_model import LibroModel
from src.models.estado_model import EstadoModel
from src.models.prestamo_model import PrestamoModel
from flask import request
from flask_restx import Resource
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required


class PrestamoController(Resource):
    @jwt_required()
    def get(self):
        try:
            prestamodb = db.session.execute(db.select(PrestamoModel)).scalars()
            prestamos = PrestamoSchema().dump(prestamodb, many=True)
            return prestamos, 200
        except NoResultFound:
            return {'message': 'No se encontraron prestamos'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class PrestamoControllerPost(Resource):
    @jwt_required()
    def post(self):
        try:
            prestamoValidar = PrestamoSchemaValidar(exclude=['IDPRESTAMO']).load(request.json["PRESTAMO"] )
            usuarioValidar = UsuarioSchemaValidar(exclude=["PASSWORD"]).load(request.json["USUARIO"])
            libroValidar = LibroSchemaValidar().load(request.json["LIBRO"])
            estadoValidar = EstadoSchemaValidar().load(request.json["ESTADO"])
            
            prestamoValidar = PrestamoSchema()
            prestamo = prestamoValidar.load(request.json["PRESTAMO"])

            usuarioValidar = UsuarioSchema(transient =True)
            usuario = usuarioValidar.load(request.json["USUARIO"])

            libroValidar = LibroSchema(transient =True)
            libro = libroValidar.load(request.json["LIBRO"])

            estadoValidar = EstadoSchema(transient =True)
            estado = estadoValidar.load(request.json["ESTADO"])

            

            prestamo.IDUSUARIO = usuario.IDUSUARIO
            prestamo.IDLIBRO = libro.IDLIBRO
            prestamo.IDESTADO = estado.IDESTADO

            usuariodb = db.session.execute(db.select(UsuarioModel).where(UsuarioModel.IDUSUARIO == usuario.IDUSUARIO)).scalar_one()
            if len(usuariodb.PRESTAMO) >= 3:
                return {'message': 'Usuario ya tiene 3 prestamos'}, 400         
            

            db.session.add(prestamo)
            db.session.commit()
            return PrestamoSchema().dump(prestamo), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 500
    
