from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import sessionmaker
import dotenv
import os
dotenv.load_dotenv()

db_url : str = os.getenv("DATABASE_URL")
print(db_url)
engine = create_async_engine(db_url, echo = True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


