import os 
from flask import Flask

def register_blueprints(app):
    from app.auth import auth_blueprint
    from app.main import main_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/users')
    app.register_blueprint(main_blueprint)

def configure_logging(app):
    pass

def create_app():
    app = Flask(__name__)

    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    register_blueprints(app)

    configure_logging(app)

    return app

