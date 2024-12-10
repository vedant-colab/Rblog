from pydantic import BaseModel
# from Database.db import get_db
from fastapi import FastAPI, Depends, Response, status
from sqlalchemy.ext.asyncio import AsyncSession
from Models.users_db import User
from Services.create_profile import create_user, fetch_user
from core.hashing import Hasher
class Signup(BaseModel):
    userid : str
    username : str
    email : str 
    password : str

async def signup(request : Signup,response : Response):
    try:
        # print(db, request)
        ifExist = await fetch_user(request.email)
        print(ifExist)
        if(ifExist is not None):
            response.status_code = status.HTTP_200_OK
            return {"error_code": "1", "message": "user already exists"}
        hpass = Hasher.hash_password(request.password)
        print(hpass)
        new_user = await create_user(request.userid, request.username, request.email, hpass)
        response.status_code = status.HTTP_201_CREATED
        return new_user
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "something went wrong", "error": e}