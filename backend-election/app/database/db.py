from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
DATABASE_URL = "sqlite:///votes.db"  # or your preferred DB

# Engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = SessionLocal()

# Base class for models
Base = declarative_base()

# Optional: function to create tables
def init_db():
    from app.models.vote import Vote  # import your models here
    Base.metadata.create_all(bind=engine)
