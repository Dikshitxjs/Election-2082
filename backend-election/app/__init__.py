from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.database.db import db, init_db
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Initialize DB safely
    init_db(app)

    # Initialize migrations (Flask-Migrate)
    # This attaches Alembic migration support to the app and SQLAlchemy `db`.
    try:
        Migrate(app, db)
    except Exception:
        # If Flask-Migrate isn't installed in the environment yet, continue gracefully.
        pass

    # Enable CORS using configured origins and restrict to API routes
    cors_origins = app.config.get("CORS_ORIGINS") or ["http://localhost:3000"]

    # If wildcard origin is explicitly provided, don't enable credentials
    if len(cors_origins) == 1 and cors_origins[0] == "*":
        CORS(
            app,
            supports_credentials=False,
            resources={r"/api/*": {"origins": "*"}},
            allow_headers=["Content-Type", "Authorization"],
            methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        )
    else:
        CORS(
            app,
            supports_credentials=True,
            resources={r"/api/*": {"origins": cors_origins}},
            allow_headers=["Content-Type", "Authorization"],
            methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        )

    # Register routes
    register_routes(app)

    # Debug: print configured CORS origins and registered routes
    try:
        print("Configured CORS origins:", app.config.get("CORS_ORIGINS"))
        rules = sorted([str(r) for r in app.url_map.iter_rules()])
        print("Registered routes:")
        for r in rules:
            print(" ", r)
    except Exception:
        pass

    # Log incoming requests (method, path, Origin) to help diagnose CORS issues
    @app.before_request
    def log_request_info():
        try:
            from flask import request
            origin = request.headers.get("Origin")
            print(f"Incoming request: {request.method} {request.path} Origin={origin}")
        except Exception:
            pass

    # Robustly handle OPTIONS preflight for any /api path before routing
    @app.before_request
    def handle_api_options():
        try:
            from flask import request, make_response
            if request.method == 'OPTIONS' and request.path.startswith('/api'):
                resp = make_response("")
                cors_origins = app.config.get("CORS_ORIGINS") or []
                origin = request.headers.get("Origin")
                allow_all = len(cors_origins) == 1 and cors_origins[0] == "*"

                if origin:
                    if allow_all:
                        resp.headers["Access-Control-Allow-Origin"] = "*"
                    else:
                        if origin in cors_origins:
                            resp.headers["Access-Control-Allow-Origin"] = origin
                            resp.headers["Access-Control-Allow-Credentials"] = "true"

                resp.headers["Access-Control-Allow-Headers"] = request.headers.get("Access-Control-Request-Headers", "Content-Type, Authorization")
                resp.headers["Access-Control-Allow-Methods"] = request.headers.get("Access-Control-Request-Method", "GET, POST, PUT, DELETE, OPTIONS")
                resp.headers["Vary"] = "Origin"
                return resp
        except Exception:
            pass

    # Manual CORS handling to ensure precise control in prod and dev.
    @app.after_request
    def apply_cors(response):
        try:
            from flask import request
            cors_origins = app.config.get("CORS_ORIGINS") or []
            origin = request.headers.get("Origin")

            # If wildcard allowed and no credential usage required, echo '*'
            allow_all = len(cors_origins) == 1 and cors_origins[0] == "*"

            if origin:
                if allow_all:
                    # When wildcard, we must not allow credentials
                    response.headers["Access-Control-Allow-Origin"] = "*"
                    response.headers.pop("Access-Control-Allow-Credentials", None)
                else:
                    # If origin exactly matches configured origins, echo it
                    if origin in cors_origins:
                        response.headers["Access-Control-Allow-Origin"] = origin
                        response.headers["Access-Control-Allow-Credentials"] = "true"
                    else:
                        # Not allowed origin; do not set CORS headers.
                        pass

                # Common CORS headers for browser requests
                response.headers.setdefault("Vary", "Origin")
                response.headers.setdefault("Access-Control-Allow-Headers", "Content-Type, Authorization")
                response.headers.setdefault("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        except Exception:
            pass
        return response

    # Handle preflight OPTIONS globally for /api/*
    @app.route('/api/<path:dummy>', methods=['OPTIONS'])
    @app.route('/api', methods=['OPTIONS'])
    def handle_options(dummy=None):
        from flask import make_response, request
        resp = make_response("")
        cors_origins = app.config.get("CORS_ORIGINS") or []
        origin = request.headers.get("Origin")
        allow_all = len(cors_origins) == 1 and cors_origins[0] == "*"

        if origin:
            if allow_all:
                resp.headers["Access-Control-Allow-Origin"] = "*"
            else:
                if origin in cors_origins:
                    resp.headers["Access-Control-Allow-Origin"] = origin
                    resp.headers["Access-Control-Allow-Credentials"] = "true"

        resp.headers["Access-Control-Allow-Headers"] = request.headers.get("Access-Control-Request-Headers", "Content-Type, Authorization")
        resp.headers["Access-Control-Allow-Methods"] = request.headers.get("Access-Control-Request-Method", "GET, POST, PUT, DELETE, OPTIONS")
        resp.headers["Vary"] = "Origin"
        return resp

    return app
