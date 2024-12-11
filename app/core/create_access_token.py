import jwt
import dotenv
from datetime import timedelta, datetime, timezone
import os
dotenv.load_dotenv()

JWT_KEY = os.getenv("JWT_SECRET_KEY")

def create_access_token(payload : dict, expires_in : timedelta | None = None):
    try:
        data = payload.copy()
        if expires_in:
            expire = datetime.now(timezone.utc) + expires_in
        else:
            expire = datetime.now(timezone.utc) + timedelta(days=1)
        data.update({"exp" : expire})
        token = jwt.encode(data,JWT_KEY, algorithm="HS256")
        return token
    except Exception as e:
        print(e)