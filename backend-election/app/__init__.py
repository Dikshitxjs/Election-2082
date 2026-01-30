from flask import Flask
from flask_cors import CORS
from app.database.db import init_db
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Initialize database
    init_db()

    # Enable CORS for frontend with credentials
    CORS(
        app,
        supports_credentials=True,
        origins=["http://localhost:3000"]  # frontend URL
    )

    # Register all routes without redirect issues
    register_routes(app)

    return app
