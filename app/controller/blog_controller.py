from pydantic import BaseModel
from Services.blog import save_blog, fetch_blogs
from fastapi import status, HTTPException

class BlogBody(BaseModel):
    title : str
    body : str
    userid : str

class GetBlogBody(BaseModel):
    userid : str

async def create_blogs(request : BlogBody) -> dict:
    try:
        blog = await save_blog(request.title, request.body, request.userid)
        if blog:
            return {"Error_code": "0", "data" : "blog saved sucessfully"}
        else:
            HTTPException(status_code=200,detail= "Issue saving blog")
            return
    except Exception as e:
        return {"Error_coce": "1", "error": e}
    

async def get_blogs(request : GetBlogBody) -> dict:
    try:
        blogs = await fetch_blogs(request.userid)
        return blogs
    except Exception as e:
        return {}