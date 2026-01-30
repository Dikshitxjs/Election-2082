from .candidates import candidates_bp
from .vote import vote_bp
from .comments import comments_bp
from .chhetra import chhetra_bp

def register_routes(app):
    # strict_slashes=False avoids automatic redirects
    app.register_blueprint(candidates_bp, url_prefix="/api/candidates", strict_slashes=False)
    app.register_blueprint(vote_bp, url_prefix="/api/votes", strict_slashes=False)
    app.register_blueprint(comments_bp, url_prefix="/api/comments", strict_slashes=False)
    app.register_blueprint(chhetra_bp, url_prefix="/api/chhetras", strict_slashes=False)
