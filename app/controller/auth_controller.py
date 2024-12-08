from pydantic import BaseModel
from Database.db import get_db
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from Models.users_db import User
from Services.create_profile import create_user

class Signup(BaseModel):
    userid : str
    username : str
    email : str 
    password : str

async def signup(request : Signup, db : AsyncSession = Depends(get_db)):
    try:
        new_user = await create_user(request.userid, request.username, request.email, request.password, db=db)
        return {"error_code": "0", "message": "user created successfully"}
    except Exception as e:
        return {"message": "something went wrong", "error": e}