from flask import Flask
from app.routes.vote import vote_bp
from app.routes.candidates import candidates_bp
from app.routes.comments import comments_bp  # <--- IMPORT COMMENTS
from app.database.db import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    init_db()

    # Register blueprints
    app.register_blueprint(vote_bp, url_prefix="/api")
    app.register_blueprint(candidates_bp, url_prefix="/api")
    app.register_blueprint(comments_bp, url_prefix="/api")  # now Python knows this

    return app
