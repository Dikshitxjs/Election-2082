from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.db import Base  # must match exactly

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    candidate = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "candidate": self.candidate,
            "timestamp": self.timestamp.isoformat()
        }
