import os 
from os.path import join, dirname
from dotenv import load_dotenv

class BaseConfig ():
    #path para variables de entorno
    dotenv_path = join(dirname(__file__), '.env')
    #cargar environment
    load_dotenv(dotenv_path, override=True)

    SQLALCHEMY_DATABASE_URI = ''

class DeveloperConfig (BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')

class ProductionConfig (BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')

