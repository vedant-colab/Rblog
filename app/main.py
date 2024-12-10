from fastapi import FastAPI
import dotenv
from contextlib import asynccontextmanager
from routes.auth_routes import auth_router
from routes.get_details_routes import details_router 
from Database.init_db import init_db, close_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    
    await close_db()
    


app = FastAPI(lifespan=lifespan)

dotenv.load_dotenv(r"C:\Users\VEDANT\fastAPI_Projects\blog\.env")

app.include_router(router=auth_router, prefix="/users", tags=["Users"])
app.include_router(router=details_router, prefix="/details", tags=["details"])


@app.get("/")
def index():
    return {"message": f"Welcome to RBlog"}
