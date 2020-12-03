from flask import Flask, Blueprint
from flask_admin import Admin


from config import Config
import os

def create_app(config_class = Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)


    from app.base import bp as base_bp
    from app.errors import bp as errors_bp
    from app.admin import bp as admin_bp
    app.register_blueprint(base_bp)
    app.register_blueprint(errors_bp)
    app.register_blueprint(admin_bp)

    admin = Admin(app, name='textureasy', template_mode='bootstrap3')

    return app
