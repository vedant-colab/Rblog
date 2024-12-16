from fastapi import APIRouter, Depends, Response, Header
from controller.auth_controller import Signup, signup, tokenBody, tokenCreation, logout
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

@auth_router.post("/logout", summary="Will logout a user")
async def logout_route(token : str = Header(alias="Authorization")):
    return await logout(token)