from fastapi import APIRouter, Depends

from Database.db import get_db
from controller.auth_controller import Signup, signup
from sqlalchemy.ext.asyncio import AsyncSession
auth_router = APIRouter()

@auth_router.post("/signup", summary="Register a new user", status_code=201)
async def user_signup(request: Signup, db: AsyncSession = Depends(get_db)):
    return await signup(request, db)