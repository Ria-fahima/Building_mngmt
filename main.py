from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.cli_controller import db_commands
from controllers.annoucements_controller import annoucement_bp
from controllers.complains_controller import complain_bp
from controllers.auth_controller import auth_bp
from controllers.user_controller import user_bp
from marshmallow.exceptions import ValidationError
from init import db,bcrypt,ma,jwt
import os

def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)},404

    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)},400

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)},401

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages},400
    
    @app.errorhandler(ValueError)
    def value_error(err):
        return {'error': f'The field has {err}.'}, 400

    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400

    app.config ['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')


    db.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    
    app.register_blueprint(db_commands)
    app.register_blueprint(annoucement_bp)
    app.register_blueprint(complain_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    return app

