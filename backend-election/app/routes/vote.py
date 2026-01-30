from flask import Blueprint, jsonify

vote_bp = Blueprint("votes", __name__)

# Dummy votes data
votes = [
    {"id": 1, "candidate_id": 1, "voter": "user1"},
    {"id": 2, "candidate_id": 2, "voter": "user2"}
]

# Get all votes
@vote_bp.route("/", methods=["GET"])
def get_all_votes():
    return jsonify(votes)

# Get votes by candidate
@vote_bp.route("/candidate/<int:candidate_id>", methods=["GET"])
def get_votes_by_candidate(candidate_id):
    candidate_votes = [v for v in votes if v["candidate_id"] == candidate_id]
    return jsonify(candidate_votes)
