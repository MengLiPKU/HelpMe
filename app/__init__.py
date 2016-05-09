from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.help import help as help_blueprint
from app.user import user as user_blueprint
from config import config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)

    app.register_blueprint(user_blueprint)
    app.register_blueprint(help_blueprint)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    return app
