from flask import Flask
from src.common.utils import db, ma, jwt, api
from src.routes.routes import Routes
import os


app = Flask(__name__)

if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object("settings.DeveloperConfig")    
elif os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object("settings.ProductionConfig")


api.init_app(app)
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

Routes(api)
