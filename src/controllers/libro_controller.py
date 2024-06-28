from src.common.utils import db
from src.models.libro_model import LibroModel
from flask import request
from flask_restx import Resource
from src.schemas.libro_schema import LibroSchema, LibroSchemaValidar
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError


class LibroController(Resource):
    def get(self):
        try:
            librodb = db.session.execute(db.select(LibroModel)).scalars()
            libro = LibroSchema().dump(librodb, many=True)
            return libro, 200
        except NoResultFound:
            return {'message': 'libro no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class LibroControllerGetById(Resource):
    def get(self, idlibro):
        try:
            librodb = db.session.execute(db.select(LibroModel).where(LibroModel.IDLIBRO == idlibro)).scalar_one()
            libro = LibroSchema().dump(librodb)
            return libro, 200
        except NoResultFound:
            return {'message': 'libro no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class LibroControllerPost(Resource):
    def post(self):
        try:
            libroValidar = LibroSchemaValidar(exclude=['IDLIBRO'])
            libroValidar.load(request.json)

            libroValidar = LibroSchema()
            libro = libroValidar.load(request.json)

            db.session.add(libro)
            db.session.commit()
            return LibroSchema().dump(libro), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 500

class LibroControllerPut(Resource):
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
            return LibroSchema().dump(libro), 200
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'libro no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class LibroControllerDelete(Resource):
    def delete(self, idlibro):
        try:
            librodb = db.session.execute(db.select(LibroModel).where(LibroModel.IDLIBRO == idlibro)).scalar_one()
            db.session.delete(librodb)
            db.session.commit()
            return {'message': 'libro eliminado'}, 200
        except NoResultFound:
            return {'message': 'libro no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500
