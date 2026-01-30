from flask import Blueprint, jsonify

chhetra_bp = Blueprint("chhetra", __name__)

# TEMP: map chhetra id → candidates
CANDIDATES = [
    {
        "id": 1,
        "name": "Ram Prasad Sharma",
        "party": "Party A",
        "chhetra_id": 1,
        "votes": 120,
        "bio": "Experienced leader focused on development."
    },
    {
        "id": 2,
        "name": "Sita Karki",
        "party": "Party B",
        "chhetra_id": 2,
        "votes": 95,
        "bio": "Advocate for education and youth."
    },
    {
        "id": 3,
        "name": "Hari Bhandari",
        "party": "Party C",
        "chhetra_id": 1,
        "votes": 80,
        "bio": "Focused on infrastructure and roads."
    }
]

@chhetra_bp.route("/<int:id>/candidates", methods=["GET"])
def get_candidates_by_chhetra(id):
    candidates = [c for c in CANDIDATES if c["chhetra_id"] == id]
    return jsonify(candidates)
