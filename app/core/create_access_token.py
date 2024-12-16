import jwt
import dotenv
from datetime import timedelta, datetime, timezone
import os
from Models.session import Session
from Services.create_profile import fetch_user
dotenv.load_dotenv()

JWT_KEY = os.getenv("JWT_SECRET_KEY")

async def create_access_token(payload : dict, expires_in : timedelta | None = None):
    try:
        data = payload.copy()
        if expires_in:
            expire = datetime.now(timezone.utc) + expires_in
        else:
            expire = datetime.now(timezone.utc) + timedelta(days=1)
        data.update({"exp" : expire})
        token = jwt.encode(data,JWT_KEY, algorithm="HS256")
        user = await fetch_user(payload["email"])
        await Session.create(userid_id = user.userid, token=token)
        return token
    except Exception as e:
        print(e)
        
async def delete_token(token : str):
    try:
        session = await Session.filter(token = token).order_by("createdAt").first()
        if session:
            session.isActive = False 
            await session.save()
            return {"error_code": "0", "data": "User logged out sucessfully"}
        return {"error_code": "1", "data": "No user found for this id or token"}
    except Exception as e:
        print(e)
        return {"error_code": "2", "error": f"{e}"}