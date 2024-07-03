from src.schemas.genero_schema import GeneroSchema, GeneroSchemaValidar
from src.common.utils import db
from sqlalchemy.orm.exc import NoResultFound
from flask_restx import Resource
from flask import request
from src.models.genero_model import GeneroModel
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError


class GeneroController(Resource):
    def get(self):
        try: 
            generosdb = db.session.execute(db.select(GeneroModel)).scalars()
            generos = GeneroSchema().dump(generosdb, many=True)
            return generos, 200
        except NoResultFound:
            return {'message': 'Genero no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class GeneroControllerGetById(Resource):
    def get(self, idgenero):
        try: 
            generodb = db.session.execute(db.select(GeneroModel).where(GeneroModel.IDGENERO == idgenero)).scalar_one()
            genero = GeneroSchema().dump(generodb)
            return genero, 200
        except NoResultFound:
            return {'message': 'Genero no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class GeneroControllerPost(Resource):
    def post(self):
        try:
            generoValidar = GeneroSchemaValidar(exclude=['IDGENERO'])
            generoValidar.load(request.json)

            generoValidar = GeneroSchema()
            genero = generoValidar.load(request.json)

            db.session.add(genero)
            db.session.commit()
            return GeneroSchema().dump(genero), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 500

class GeneroControllerPut(Resource):
    def put(self):
        try:
            generoValidar = GeneroSchemaValidar()
            genero = generoValidar.load(request.json)
            
            generodb = db.session.execute(db.select(GeneroModel).where(GeneroModel.IDGENERO == genero["IDGENERO"])).scalar_one()
            generodb.NOMBRE = genero["NOMBRE"]

            db.session.commit()
            return GeneroSchema().dump(generodb), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'Genero no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500

class GeneroControllerDelete(Resource):
    def delete(self, idgenero):
        try:
            generodb = db.session.execute(db.select(GeneroModel).where(GeneroModel.IDGENERO == idgenero)).scalar_one()
            db.session.delete(generodb)
            db.session.commit()
            return {'message': 'Genero eliminado'}, 200
        except IntegrityError:
            return {'message': 'No se puede eliminar el genero porque esta siendo usado'}, 400
        except NoResultFound:
            return {'message': 'Genero no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 500
