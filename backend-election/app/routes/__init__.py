from .candidates import candidates_bp
from .vote import vote_bp
from .comments import comments_bp


def register_routes(app):
    app.register_blueprint(candidates_bp, url_prefix="/api/candidates")
    app.register_blueprint(votes_bp, url_prefix="/api/votes")
    app.register_blueprint(comments_bp, url_prefix="/api/comments")
   
