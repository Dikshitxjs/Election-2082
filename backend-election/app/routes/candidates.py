from flask import Blueprint

candidates_bp = Blueprint("candidates", __name__)

@candidates_bp.route("/candidates")
def get_candidates():
    return "List of candidates"
