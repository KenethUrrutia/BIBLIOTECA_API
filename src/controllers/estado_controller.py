from src.schemas.estado_schema import EstadoSchema, EstadoSchemaValidar
from src.common.utils import db
from sqlalchemy.orm.exc import NoResultFound
from flask_restx import Resource
from flask import request
from src.models.estado_model import EstadoModel
from marshmallow import ValidationError


class EstadoController(Resource):
    def get(self):
        try: 
            estadosdb = db.session.execute(db.select(EstadoModel)).scalars()
            estados = EstadoSchema().dump(estadosdb, many=True)
            return estados, 200
        except NoResultFound:
            return {'message': 'estado no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class EstadoControllerGetById(Resource):
    def get(self, idestado):
        try: 
            estadodb = db.session.execute(db.select(EstadoModel).where(EstadoModel.IDESTADO == idestado)).scalar_one()
            estado = EstadoSchema().dump(estadodb)
            return estado, 200
        except NoResultFound:
            return {'message': 'estado no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class EstadoControllerPost(Resource):
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
            return {'message': str(e)}, 500

class EstadoControllerPut(Resource):
    def put(self):
        try:
            estadoValidar = EstadoSchemaValidar()
            estado = estadoValidar.load(request.json)
            
            estadodb = db.session.execute(db.select(EstadoModel).where(EstadoModel.IDESTADO == estado["IDESTADO"])).scalar_one()
            estadodb.NOMBRE = estado["NOMBRE"]

            db.session.commit()
            return EstadoSchema().dump(estadodb), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'estado no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class EstadoControllerDelete(Resource):
    def delete(self, idestado):
        try:
            estadodb = db.session.execute(db.select(EstadoModel).where(EstadoModel.IDESTADO == idestado)).scalar_one()
            db.session.delete(estadodb)
            db.session.commit()
            return {'message': 'estado eliminado'}, 200
        except NoResultFound:
            return {'message': 'estado no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500
