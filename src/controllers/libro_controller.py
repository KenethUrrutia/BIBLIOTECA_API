from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.common.utils import db, api, RespuestaGenerica
from src.models.libro_model import LibroModel
# from src.models.prestamo_model import PrestamoModel
from src.schemas.libro_schema import LibroSchema, LibroSchemaValidar
from src.swagger.libro_swagger import LibroSwagger, LibroPostSwagger

class LibroController(Resource):
    #interfaz que enlista todos los LIBRO
    @api.doc(description='Obtiene todas los registros de LIBRO')
    @api.response(200, "Se obtienen con éxito todos los registros de LIBRO", LibroSwagger)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(404, "No se encontraron registros de LIBRO", RespuestaGenerica)
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def get(self):
        try:
            librodb = db.session.execute(db.select(LibroModel)).scalars()
            libro = LibroSchema(exclude=['PRESTAMO', 'GENERO']).dump(librodb, many=True)
            return libro, 200
        except NoResultFound:
            return {'message': 'libro no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
    
    #interfaz para crear un LIBRO
    @api.doc(description='Crea un nuevo registro de LIBRO')
    @api.expect(LibroPostSwagger)
    @api.response(201, "Se crea con éxito el nuevo registro de LIBRO", LibroSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def post(self):
        try:
            libroValidar = LibroSchemaValidar(exclude=['IDLIBRO'])
            libroValidar.load(request.json)

            libroValidar = LibroSchema()
            libro = libroValidar.load(request.json)

            db.session.add(libro)
            db.session.commit()
            return LibroSchema(exclude=['PRESTAMO', 'GENERO']).dump(libro), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 503
    
    #interfaz para actualizar un LIBRO
    @api.doc(description='Actualiza un registro de LIBRO')
    @api.expect(LibroSwagger)
    @api.response(200, "Se actualizó con éxito el registro de LIBRO", LibroSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(404, "No se encontró el libro", RespuestaGenerica)
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def put(self):
        try:
            libroValidar = LibroSchemaValidar()
            libro = libroValidar.load(request.json)
            
            librodb = db.session.execute(db.select(LibroModel).where(LibroModel.IDLIBRO == libro["IDLIBRO"])).scalar_one()
            librodb.TITULO = libro["TITULO"]
            librodb.AUTOR = libro["AUTOR"]
            librodb.ANIO_PUBLICACION = libro["ANIO_PUBLICACION"]
            librodb.IDGENERO = libro["IDGENERO"]

            db.session.commit()
            return LibroSchema(exclude=['PRESTAMO', 'GENERO']).dump(libro), 200
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'libro no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503

class LibroControllerById(Resource):
    #interfaz para obtener un LIBRO por id
    @api.doc(description='Obtiene un registro de LIBRO por su ID')
    @api.param('idlibro', 'ID del LIBRO')
    @api.response(200, "Se obtuvo con éxito el registro de LIBRO", LibroSwagger)
    @api.response(404, "No se encontró el registro de LIBRO", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def get(self, idlibro):
        try:
            librodb = db.session.execute(db.select(LibroModel).where(LibroModel.IDLIBRO == idlibro)).scalar_one()
            libro = LibroSchema(exclude=['PRESTAMO', 'GENERO']).dump(librodb)
            return libro, 200
        except NoResultFound:
            return {'message': 'libro no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
    
    #interfaz para eliminar un LIBRO por id
    @api.doc(description='Elimina un registro de LIBRO por su ID')
    @api.param('idlibro', 'ID del LIBRO')
    @api.response(200, "Se eliminó con éxito el registro de LIBRO", RespuestaGenerica)
    @api.response(400, "No se puede eliminar porque tiene registros asociados", RespuestaGenerica)
    @api.response(404, "No se encontró el registro de LIBRO", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def delete(self, idlibro):
        try:
            librodb = db.session.execute(db.select(LibroModel).where(LibroModel.IDLIBRO == idlibro)).scalar_one()
            
            if librodb.PRESTAMO != []:
                return {'message': 'libro tiene prestamos asociados'}, 400
            
            db.session.delete(librodb)
            db.session.commit()
            return {'message': 'libro eliminado'}, 200
        except IntegrityError:
            return {'message': 'libro no se puede eliminar porque tiene registros asociados'}, 400
        except NoResultFound:
            return {'message': 'libro no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503

