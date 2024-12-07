from Database.db import Base
from sqlalchemy import Column,String, Boolean, DateTime, func

class User(Base):
    __tablename__ = "users"
    
    userid = Column(String(100), primary_key = True)
    username = Column(String(100), unique=True, nullable= False)
    password = Column(String(100), nullable=False)  #hashed passwords
    email = Column(String(200), unique=True, nullable=False)
    status = Column(Boolean, default=True)
    role = Column(String(50), default="user")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())