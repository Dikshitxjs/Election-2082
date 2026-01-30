from flask import Blueprint, request, jsonify
from app.models.vote import Vote
from app.database.db import db_session
from app.services.rate_limit import can_vote

vote_bp = Blueprint("vote", __name__)

@vote_bp.route("/vote", methods=["POST"])
def submit_vote():
    data = request.json
    user_id = data.get("user_id")
    candidate = data.get("candidate")

    if not user_id or not candidate:
        return jsonify({"success": False, "message": "Missing user_id or candidate"}), 400

    if not can_vote(user_id):
        return jsonify({"success": False, "message": "User has already voted"}), 403

    # Save vote
    new_vote = Vote(user_id=user_id, candidate=candidate)
    db_session.add(new_vote)
    db_session.commit()

    return jsonify({"success": True, "message": "Vote recorded!"})

@vote_bp.route("/votes", methods=["GET"])
def get_votes():
    votes = db_session.query(Vote).all()
    return jsonify([v.to_dict() for v in votes])
