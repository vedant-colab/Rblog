from sqlalchemy.ext.declarative import base_declarative
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

Base = base_declarative()

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


