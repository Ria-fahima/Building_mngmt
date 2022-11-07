from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.cli_controller import db_commands
from init import db,bcrypt
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db.init_app(app)
    bcrypt.init_app(app)
    
    app.register_blueprint(db_commands)

    return app
