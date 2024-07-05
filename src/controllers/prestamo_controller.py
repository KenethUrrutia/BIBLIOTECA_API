from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource, fields
from marshmallow import ValidationError
from src.common.utils import db, api, RespuestaGenerica
from src.models.estado_model import EstadoModel
from src.models.libro_model import LibroModel
from src.models.prestamo_model import PrestamoModel
from src.models.usuario_model import UsuarioModel
from src.schemas.estado_schema import EstadoSchemaValidar, EstadoSchema
from src.schemas.libro_schema import LibroSchemaValidar, LibroSchema
from src.schemas.prestamo_schema import PrestamoSchema, PrestamoSchemaValidar
from src.schemas.usuario_schema import UsuarioSchemaValidar, UsuarioSchema
from sqlalchemy.orm.exc import NoResultFound
from src.swagger.prestamo_swagger import PrestamoSwagger, PrestamoPostSwagger


class PrestamoController(Resource):
    #interfaz que enlista todos los PRESTAMOS
    @api.doc(description='Obtiene todas los registros de PRESTAMO')
    @api.response(200, "Se obtienen con éxito todos los registros de PRESTAMO",PrestamoSwagger, as_list=True)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(404, "No se encontraron registros de PRESTAMO", RespuestaGenerica)
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def get(self):
        try:
            prestamodb = db.session.execute(db.select(PrestamoModel)).scalars()
            prestamos = PrestamoSchema(exclude=['USUARIO', 'ESTADO_LIBRO', 'LIBROS']).dump(prestamodb, many=True)
            return prestamos, 200
        except NoResultFound:
            return {'message': 'No se encontraron prestamos'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
        
    #interfaz para crear un PRESTAMO
    @api.doc(description='Crea un nuevo registro de PRESTAMO')
    @api.expect(PrestamoPostSwagger)
    @api.response(201, "Se crea con éxito el nuevo registro de PRESTAMO", PrestamoSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def post(self):
        try:
            prestamoValidar = PrestamoSchemaValidar(exclude=['IDPRESTAMO']).load(request.json["PRESTAMO"] )
            usuarioValidar = UsuarioSchemaValidar(exclude=["PASSWORD"]).load(request.json["USUARIO"])
            libroValidar = LibroSchemaValidar().load(request.json["LIBRO"])
            estadoValidar = EstadoSchemaValidar().load(request.json["ESTADO"])
            
            prestamoValidar = PrestamoSchema()
            prestamo = prestamoValidar.load(request.json["PRESTAMO"])

            usuarioValidar = UsuarioSchema(transient =True, exclude=["PASSWORD"])
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
            return PrestamoSchema(exclude=['USUARIO', 'ESTADO_LIBRO', 'LIBROS']).dump(prestamo), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 503
        
    
    
