from fastapi import APIRouter, Depends, Response
from controller.auth_controller import Signup, signup
auth_router = APIRouter()

@auth_router.post("/signup", summary="Register a new user")
async def user_signup(request: Signup):
    # print(f"in router")
    # print(request)
    response = Response()
    return await signup(request,response)