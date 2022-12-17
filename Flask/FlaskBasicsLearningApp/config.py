import os 
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLASK_ENV = 'development'
    SECRET_KEY = os.getenv('SECRET_KEY', default='A very bad secret key')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    FLASK_ENV = 'production'

