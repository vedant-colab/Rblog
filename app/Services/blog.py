from .create_profile import fetch_user_on_userid
from datetime import datetime
from Models.blogs import Blogs
from slugify import slugify

async def save_blog(title, body, userid):
    try:
        user = await fetch_user_on_userid(userid)
        if user:
            slug = slugify(title + ' ' +  datetime.now().strftime("%Y%m%d%H%M%S"))
            blog = await Blogs.create(user_id_id = user.userid, title = title, body = body, slug = slug)
            return blog
        return None
    except Exception as e:
        print(f"Error creating blog {e}")
        return None
    
    
async def fetch_blogs(userid : str) -> dict | None:
    try:
        user = await fetch_user_on_userid(userid)
        if user:
            blogs = await Blogs.filter(user_id = userid).all().values("title", "body", "slug" ,"updated_at")
            if blogs:
                return {"Error_code": "0", "data": blogs}
            else:
                return {"Error_code": "1", "data": "No blogs found for user"}
        return {"Error_code": "1", "data": "Invalid user"}
    except Exception as e:
        print(e)
        return None
    
async def update_blog(title: str, body: str, userid: str, slug: str) -> dict | None:
    try:
        user = await fetch_user_on_userid(userid)
        if not user:
            return {"error_code": "1", "data": "No user found for this ID"}

        blog = await Blogs.filter(slug=slug, user_id=userid).first()
        if blog:
            new_slug = slugify(f"{title} {datetime.now().strftime('%Y%m%d%H%M%S')}")
            blog.title = title
            blog.body = body
            blog.slug = new_slug
            await blog.save()  # Save updates
            return {"success": True, "data": f"Blog updated with new slug {new_slug}"}
        
    except Exception as e:
        print(f"Error updating blog: {e}")
        return {"error_code": "2", "data": "An unexpected error occurred"}
    
async def delete_blog(userid : str, slug : str):
    try:
        user = await fetch_user_on_userid(userid)
        if not user:
            return {"error_code": "1", "data": "No user found for this ID"}

        blog = await Blogs.filter(slug=slug, user_id=userid).first()
        if not blog:
            return {"error_code": "1", "data": "No blog found for the given slug and user"}
        await blog.delete()
        return {"error_code": "0", "data": "Blog deleted successfully"}
    except Exception as e:
        print(f"Error updating blog: {e}")
        return {"error_code": "2", "data": "An unexpected error occurred"}