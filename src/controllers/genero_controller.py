from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.common.utils import db, api, RespuestaGenerica
from src.models.genero_model import GeneroModel
from src.schemas.genero_schema import GeneroSchema, GeneroSchemaValidar
from src.swagger.genero_swagger import GeneroSwagger, GeneroPostSwagger


class GeneroController(Resource):
    #interfaz que enlista todos los generos
    @api.doc(description='Obtiene todas los registros de GENERO')
    @api.response(200, "Se obtienen con éxito todos los registros de GENERO", GeneroSwagger)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(404, "No se encontraron registros de GENERO", RespuestaGenerica)
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def get(self):
        try: 
            generosdb = db.session.execute(db.select(GeneroModel)).scalars()
            generos = GeneroSchema().dump(generosdb, many=True)
            return generos, 200
        except NoResultFound:
            return {'message': 'Genero no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
    
    #interfaz para crear un GENERO
    @api.doc(description='Crea un nuevo registro de GENERO')
    @api.expect(GeneroPostSwagger)
    @api.response(201, "Se crea con éxito el nuevo registro de GENERO", GeneroSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
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
            return {'message': str(e)}, 503
    
    #interfaz para actualizar un GENERO
    @api.doc(description='Actualiza un registro de GENERO')
    @api.expect(GeneroSwagger)
    @api.response(200, "Se actualizó con éxito el registro de GENERO", GeneroSwagger)
    @api.response(400, "Error en la validación de datos", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def put(self):
        try:
            generoValidar = GeneroSchemaValidar()
            genero = generoValidar.load(request.json)
            
            generodb = db.session.execute(db.select(GeneroModel).where(GeneroModel.IDGENERO == genero["IDGENERO"])).scalar_one()
            generodb.NOMBRE = genero["NOMBRE"]

            db.session.commit()
            return GeneroSchema().dump(generodb), 200
        except ValidationError as e:
            return {'message': str(e)}, 400
        except NoResultFound:
            return {'message': 'Genero no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503



class GeneroControllerById(Resource):
    #interfaz para obtener un GENERO por id
    @api.doc(description='Obtiene un registro de GENERO por su ID')
    @api.param('idgenero', 'ID del GENERO')
    @api.response(200, "Se obtuvo con éxito el registro de GENERO", GeneroSwagger)
    @api.response(404, "No se encontró el registro de GENERO", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
    def get(self, idgenero):
        try: 
            generodb = db.session.execute(db.select(GeneroModel).where(GeneroModel.IDGENERO == idgenero)).scalar_one()
            genero = GeneroSchema().dump(generodb)
            return genero, 200
        except NoResultFound:
            return {'message': 'Genero no encontrado'}, 404
        except Exception as e:
            return {'message': str(e)}, 503
        
    #interfaz para eliminar un GENERO por id
    @api.doc(description='Elimina un registro de GENERO por su ID')
    @api.param('idgenero', 'ID del GENERO')
    @api.response(200, "Se eliminó con éxito el registro de GENERO", RespuestaGenerica)
    @api.response(400, "No se puede eliminar porque tiene registros asociados", RespuestaGenerica)
    @api.response(404, "No se encontró el registro de GENERO", RespuestaGenerica)
    @api.response(401, "Acceso por token no autorizado")
    @api.response(503, "Algo salió en la consulta o durante la ejecución", RespuestaGenerica)
    @jwt_required()
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
            return {'message': str(e)}, 503



    