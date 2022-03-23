# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

import os
from flask import Flask
import secrets

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        #Estableciendo las cookies
        SECRET_KEY=secrets.token_hex(20),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')   
    )
    
    from . import db
    
    db.init_app(app)
    
    from . import auth
    from . import todo
    from . import index
    
    app.register_blueprint(index.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    return app
