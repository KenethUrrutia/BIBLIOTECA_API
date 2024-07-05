from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_restx import Api, fields

api = Api(prefix="/api/v1/")
#objeto de db
db = SQLAlchemy()
#objeto de esquemas
ma = Marshmallow()
#objeto de jwt
jwt = JWTManager()

#objeto comun de respuesta de Swagger
RespuestaGenerica = api.model('RespuestaModel', {'message': fields.String})



