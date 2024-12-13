import jwt
import dotenv 
from main import app
from fastapi import Request
from fastapi.security import OAuth2AuthorizationCodeBearer

@app.middleware("http")
async def verify_token(request : Request, call_next):
    try:
        token = request.headers.get("Authorization")
        deocded = jwt.decode()
    except Exception as e:
        pass