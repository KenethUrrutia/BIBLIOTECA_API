from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.common.utils import db, api, RespuestaGenerica
from src.models.estado_model import EstadoModel
from src.schemas.estado_schema import EstadoSchema, EstadoSchemaValidar
from src.swagger.estado_swagger import EstadoSwagger, EstadoPostSwagger


class EstadoController(Resource):
    #interfaz que enlista todos los estados
    @api.doc(description='Obtiene todas los registros de ESTADO')
    @api.response(200, "Se obtienen con éxito todos los registros de ESTADO", EstadoSwagger)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(404, "No se encontraron registros de ESTADO", RespuestaGenerica)
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def get(self):
        try: 
            estadosdb = db.session.execute(db.select(EstadoModel)).scalars()
            estados = EstadoSchema().dump(estadosdb, many=True)
            return estados, 200
        except NoResultFound:
            return {'message': 'estado no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
    
    #interfaz para crear un estado
    @api.doc(description='Crea un nuevo registro de ESTADO')
    @api.expect(EstadoPostSwagger)
    @api.response(201, "Se crea con éxito el nuevo registro de ESTADO", EstadoSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def post(self):
        try:
            estadoValidar = EstadoSchemaValidar(exclude=['IDESTADO']).load(request.json)

            estadoValidar = EstadoSchema()
            estado = estadoValidar.load(request.json)

            db.session.add(estado)
            db.session.commit()
            return EstadoSchema().dump(estado), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 503

    #interfaz para actualizar un estado
    @api.doc(description='Actualiza un registro de ESTADO')
    @api.expect(EstadoSwagger)
    @api.response(200, "Se actualizó con éxito el registro de ESTADO", EstadoSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(404, "No se encontró el registro de ESTADO", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def put(self):
        try:
            estadoValidar = EstadoSchemaValidar()
            estado = estadoValidar.load(request.json)
            
            estadodb = db.session.execute(db.select(EstadoModel).where(EstadoModel.IDESTADO == estado["IDESTADO"])).scalar_one()
            estadodb.NOMBRE = estado["NOMBRE"]

            db.session.commit()
            return EstadoSchema().dump(estadodb), 200
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'estado no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
        

class EstadoControllerById(Resource):
    #interfaz para obtener un estado por id
    @api.doc(description='Obtiene un registro de ESTADO por su ID')
    @api.param('idestado', 'ID del ESTADO')
    @api.response(200, "Se obtuvo con éxito el registro de ESTADO", EstadoSwagger)
    @api.response(404, "No se encontró el registro de ESTADO", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def get(self, idestado):
        try: 
            estadodb = db.session.execute(db.select(EstadoModel).where(EstadoModel.IDESTADO == idestado)).scalar_one()
            estado = EstadoSchema().dump(estadodb)
            return estado, 200
        except NoResultFound:
            return {'message': 'estado no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
    
    #interfaz para eliminar un estado por id
    @api.doc(description='Elimina un registro de ESTADO por su ID')
    @api.param('idestado', 'ID del ESTADO')
    @api.response(200, "Se eliminó con éxito el registro de ESTADO", RespuestaGenerica)
    @api.response(400, "No se puede eliminar porque tiene registros asociados", RespuestaGenerica)
    @api.response(404, "No se encontró el registro de ESTADO", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def delete(self, idestado):
        try:
            estadodb = db.session.execute(db.select(EstadoModel).where(EstadoModel.IDESTADO == idestado)).scalar_one()
            db.session.delete(estadodb)
            db.session.commit()
            return {'message': 'estado eliminado'}, 200
        except IntegrityError:
            return {'message': 'estado no se puede eliminar porque tiene registros asociados'}, 400
        except NoResultFound:
            return {'message': 'estado no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503

    


