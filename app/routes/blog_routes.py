from fastapi import APIRouter, Depends, Response
from controller.blog_controller import (
    create_blogs,
    get_blogs,
    update_blogs,
    delete_blogs_controller,
    GetBlogRequest,
    UpdateBlogRequest,
    CreateBlogRequest
)

blog_router = APIRouter()

@blog_router.post("/blogs", summary="Create a blog", status_code=201)
async def create_blog(request: CreateBlogRequest):
    return await create_blogs(request)

@blog_router.get("/blogs", summary="Get blogs", status_code=200)
async def get_blogs_route(request: GetBlogRequest):
    return await get_blogs(request)

@blog_router.put("/blogs/{slug}", summary="Update a blog")
async def update_blog_route(slug: str, request: UpdateBlogRequest):
    return await update_blogs(slug, request)

@blog_router.delete("/blogs/{slug}", summary="Delete a blog")
async def delete_blog_route(slug: str, request: GetBlogRequest):
    return await delete_blogs_controller(slug, request)
