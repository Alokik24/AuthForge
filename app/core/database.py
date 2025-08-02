from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config

DATABASE_URL = config(
    'DATABASE_URL', 
    default='postgresql://authuser:auth123@localhost/authforge'
    )

# Connect to DB

engine = create_engine(DATABASE_URL)

# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependency for db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()