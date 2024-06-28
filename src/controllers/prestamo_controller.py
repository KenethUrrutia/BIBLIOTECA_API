from src.common.utils import db
from src.schemas.prestamo_schema import PrestamoSchema, PrestamoSchemaValidar
from src.models.prestamo_model import PrestamoModel
from flask import request
from flask_restx import Resource
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError


class PrestamoController(Resource):
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
    def post(self):
        try:
            prestamoValidar = PrestamoSchemaValidar(exclude=['IDPRESTAMO']).load(request.json)
            prestamoValidar = PrestamoSchema()
            prestamo = prestamoValidar.load(request.json)

            db.session.add(prestamo)
            db.session.commit()
            return PrestamoSchema().dump(prestamo), 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except Exception as e:
            return {'message': str(e)}, 500
    
