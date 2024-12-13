from fastapi import APIRouter, Depends, Response
from controller.blog_controller import  BlogBody, create_blogs, GetBlogBody, get_blogs


blog_router = APIRouter()

@blog_router.post("/create-blog", summary="save blog", status_code=201)
async def create_blog(request : BlogBody):
    return await create_blogs(request)

@blog_router.post("/get-blogs", summary="get blog", status_code=200)
async def create_blog(request : GetBlogBody):
    return await get_blogs(request)