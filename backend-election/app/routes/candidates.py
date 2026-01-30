@candidates_bp.route("/<int:id>", methods=["GET"])
def get_candidate(id):
    candidates = [
        {
            "id": 1,
            "name": "Ram Prasad Sharma",
            "party": "Party A",
            "chhetra": "Kathmandu-1",
            "votes": 120,
            "bio": "Experienced leader focused on development."
        },
        {
            "id": 2,
            "name": "Sita Karki",
            "party": "Party B",
            "chhetra": "Kathmandu-2",
            "votes": 95,
            "bio": "Advocate for education and youth."
        }
    ]

    candidate = next((c for c in candidates if c["id"] == id), None)

    if not candidate:
        return {"error": "Candidate not found"}, 404

    return candidate
