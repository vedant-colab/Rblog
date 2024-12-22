from fastapi import FastAPI
import dotenv
from contextlib import asynccontextmanager
from routes.auth_routes import auth_router
from routes.get_details_routes import details_router 
from routes.blog_routes import blog_router
from Database.init_db import init_db, close_db
from tortoise import Tortoise

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print(Tortoise.apps)
    yield
    print("Closing db")
    await close_db()
    


app = FastAPI(lifespan=lifespan)

dotenv.load_dotenv()

app.include_router(router=auth_router, prefix="/users", tags=["Users"])
app.include_router(router=details_router, prefix="/details", tags=["details"])
app.include_router(router=blog_router, prefix="/blog", tags=["blogs"])


@app.get("/")
def index():
    return {"message": f"Welcome to RBlog"}
