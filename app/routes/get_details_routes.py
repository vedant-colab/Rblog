from fastapi import APIRouter, Depends, Response
from controller.get_data_controller import getUsers
details_router = APIRouter()

@details_router.get("/user-details", summary="details about all users")
async def get_users():
    response = Response()
    return await getUsers(response)