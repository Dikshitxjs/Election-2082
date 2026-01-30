from app.database.db import db

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    party = db.Column(db.String(100))
    chhetra_id = db.Column(db.Integer, nullable=False)
