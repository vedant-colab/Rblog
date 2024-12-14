from fastapi import Depends
from Models.users_db import User
from tortoise.exceptions import IntegrityError 

# from Database.db import get_db
async def create_user(userid : str, username : str, email : str, password : str):
    try:
        user = await User.create(userid=userid, username=username, email=email, password=password)
        return {"Error_code": "0", "Message": "User created successfully"}
    except IntegrityError as ie:
        return {"Error_code": "1", "Message": "User already exist with same email or user id"}
    except Exception as e:
       print(f"Error from saving user to database", e)
       return None
       
async def fetch_user(email):
    try:
        user = await User.filter(email=email).first()
        return user
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None
    
async def fetch_all_users():
    try:
        users = await User.all()
        return users
    except Exception as e:
        print("Error fetching all users...", e)
        return None
    
async def fetch_user_on_userid(userid : str) -> User | None:
    try:
        user = await User.filter(userid = userid).first()
        if user :
            return user
    except Exception as e:
        print(f"Error fetching user on userid {e}")
        return None