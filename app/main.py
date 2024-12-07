from fastapi import FastAPI
from dotenv import load_dotenv
app = FastAPI()

load_dotenv()


@app.get("/")
def index():
    return {"message": f"Welcome to RBlog"}
