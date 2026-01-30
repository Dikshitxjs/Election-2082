from flask import Blueprint, jsonify

comments_bp = Blueprint("comments", __name__)

comments = [
    {"id": 1, "candidate_id": 1, "comment": "Great leader!"},
    {"id": 2, "candidate_id": 2, "comment": "Very promising candidate."}
]

@comments_bp.route("/", methods=["GET"])
def get_all_comments():
    return jsonify(comments)

@comments_bp.route("/candidate/<int:candidate_id>", methods=["GET"])
def get_comments_by_candidate(candidate_id):
    candidate_comments = [c for c in comments if c["candidate_id"] == candidate_id]
    return jsonify(candidate_comments)
