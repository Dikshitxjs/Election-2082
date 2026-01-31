from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    # Only initialize if not already initialized
    if not hasattr(app, 'db_initialized'):
        db.init_app(app)
        app.db_initialized = True
