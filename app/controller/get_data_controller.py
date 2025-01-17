from pydantic import BaseModel
from Services.create_profile import fetch_all_users
from fastapi.encoders import jsonable_encoder
from fastapi import Response,status

async def getUsers(response: Response) -> dict:
    try:
        users = await fetch_all_users()
        result = jsonable_encoder(users)
        response.status_code = status.HTTP_200_OK
        if(len(users) == 0):
            return {"error_code" : "0", "message": "No users found" }
        return {"error_code" : "0", "Data": result }
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {e}