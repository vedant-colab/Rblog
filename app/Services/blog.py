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
                return {"Error_code": "0", "data": "No blogs found for user"}
        return {"Error_code": "1", "data": "Invalid user"}
    except Exception as e:
        print(e)
        return None