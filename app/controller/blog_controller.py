from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated
from typing import Optional
from Services.blog import save_blog, fetch_blogs, update_blog, delete_blog
from fastapi import status, HTTPException

# Request Models
class BaseRequest(BaseModel):
    userid: Annotated[str, StringConstraints(strip_whitespace=True, min_length=4)]

class CreateBlogRequest(BaseRequest):
    title: Annotated[str, StringConstraints(strip_whitespace=True, max_length=100)]
    body: str

class UpdateBlogRequest(CreateBlogRequest):
    # slug: Annotated[str, StringConstraints(strip_whitespace=True, min_length=10)]
    pass

class GetBlogRequest(BaseRequest):
    pass

class DeleteBlogRequest(BaseRequest):
    slug: Annotated[str, StringConstraints(strip_whitespace=True, min_length=10)]

# Controllers
async def create_blogs(request: CreateBlogRequest) -> dict:
    try:
        blog = await save_blog(request.title, request.body, request.userid)
        if blog:
            return {"Error_code": "0", "data": "Blog saved successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Issue saving blog")
    except Exception as e:
        return {"Error_code": "1", "error": str(e)}

async def get_blogs(request: GetBlogRequest) -> Optional[dict]:
    try:
        blogs = await fetch_blogs(request.userid)
        if blogs:
            return {"Error_code": "0", "data": blogs}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No blogs found")
    except Exception as e:
        return {"Error_code": "1", "error": str(e)}

async def update_blogs(slug : str, request: UpdateBlogRequest) -> dict:
    try:
        updated_blog = await update_blog(request.title, request.body, request.userid, slug)
        if updated_blog:
            return {"Error_code": "0", "data": "Blog updated successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    except Exception as e:
        return {"Error_code": "1", "error": str(e)}

async def delete_blogs_controller(request: DeleteBlogRequest) -> dict:
    try:
        deleted_blog = await delete_blog(request.userid, request.slug)
        if deleted_blog:
            return {"Error_code": "0", "data": "Blog deleted successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    except Exception as e:
        return {"Error_code": "1", "error": str(e)}
