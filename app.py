from flask import Flask
from flask_restx import Resource, Api
from src.common.utils import db, ma, jwt
from src.routes.routes import Routes
import os


app = Flask(__name__)

if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object("settings.DeveloperConfig")    
elif os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object("settings.ProductionConfig")


api = Api(app, prefix='/api/v1')

db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

Routes(api)
