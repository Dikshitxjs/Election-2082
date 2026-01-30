from flask import Blueprint, jsonify

chhetra_bp = Blueprint("chhetra", __name__)

chhetras = [
    {"id": 1, "name": "Kathmandu-1"},
    {"id": 2, "name": "Kathmandu-2"}
]

@chhetra_bp.route("/", methods=["GET"])
def get_all_chhetras():
    return jsonify(chhetras)
