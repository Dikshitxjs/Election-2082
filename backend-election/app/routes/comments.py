from flask import Blueprint, jsonify, request

# Define the blueprint
comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/comments", methods=["GET"])
def get_comments():
    return jsonify([
        {"id": 1, "text": "This is great!"},
        {"id": 2, "text": "Needs improvement."}
    ])

@comments_bp.route("/comments", methods=["POST"])
def add_comment():
    data = request.json
    text = data.get("text")
    if not text:
        return jsonify({"success": False, "message": "Missing text"}), 400
    return jsonify({"success": True, "message": "Comment added!", "text": text})
