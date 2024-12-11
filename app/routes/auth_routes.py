from fastapi import APIRouter, Depends, Response
from controller.auth_controller import Signup, signup, tokenBody, tokenCreation
auth_router = APIRouter()

@auth_router.post("/signup", summary="Register a new user")
async def user_signup(request: Signup):
    # print(f"in router")
    # print(request)
    response = Response()
    return await signup(request,response)

@auth_router.post("/tokenCreation", summary="Will send a jwt token")
async def create_token(request : tokenBody):
    return await tokenCreation(request, Response)