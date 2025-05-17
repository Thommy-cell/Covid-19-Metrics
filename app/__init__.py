from flask import Flask
from app.extensions import db, migrate
from app import routes 

def create_app(config_class=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprint (only once, and correctly)
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    # Import models after db is initialized so migrations work correctly
    with app.app_context():
        from app import models

    return app
