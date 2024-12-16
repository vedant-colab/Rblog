from pydantic import BaseModel, StringConstraints
# from Database.db import get_db
from fastapi import FastAPI, Depends, Response, status, HTTPException, Header
from sqlalchemy.ext.asyncio import AsyncSession
from Models.users_db import User
from Services.create_profile import create_user, fetch_user
from core.hashing import Hasher
from core.create_access_token import create_access_token, delete_token
from typing_extensions import Annotated
class Signup(BaseModel):
    userid : Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)]
    username : Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)]
    email : Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)]
    password : str
    
class tokenBody(BaseModel):
    userid : Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)]
    password : Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)]
    email : Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)]


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
    
async def tokenCreation(request : tokenBody, response : Response):
    try:
        ifExist = await fetch_user(request.email)
        if ifExist:
            payload = {"userid": request.userid, "email" : request.email}
            token = await create_access_token(payload=payload)
            response.status_code = status.HTTP_200_OK
            return {"error_code": "0", "data" : token }
        else:
            return {"error_code": "1", "message": "user not found"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error_code": "1", "message": f"Some error occrured: {e}"}
    

async def logout(token : str = Header(alias="Authorization")):
    try:
        if token.startswith("Bearer"):
            token = token[len("Bearer "):]
        result = await delete_token(token) 
        if result:
            return result 
        raise HTTPException(status_code=404, detail = "user not found")
    except Exception as e:
        return {"Error_code": "1", "error": str(e)}
        