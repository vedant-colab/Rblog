from fastapi import FastAPI
import dotenv
from routes.auth_routes import auth_router 
app = FastAPI()

dotenv.load_dotenv(r"C:\Users\VEDANT\fastAPI_Projects\blog\.env")

app.include_router(router=auth_router, prefix="/users", tags=["Users"])

@app.get("/")
def index():
    return {"message": f"Welcome to RBlog"}
