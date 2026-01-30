from app.database.db import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
