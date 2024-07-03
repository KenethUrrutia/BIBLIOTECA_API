from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

#objeto de db
db = SQLAlchemy()
#objeto de esquemas
ma = Marshmallow()
#objeto de jwt
jwt = JWTManager()
