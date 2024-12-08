from Models.users_db import User
from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(userid : str, username : str, email : str, password : str ,db: AsyncSession):
    try:
        new_user = User(userid = userid, username = username, email = email, password = password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
    except Exception as e:
       print(f"Error from saving user to database", e) 