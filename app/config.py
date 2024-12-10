# from pydantic_settings import BaseSettings  
from pydantic import BaseSettings

class Settings(BaseSettings):
    title_name : str = "RBlog"
    admin_email : str =  "vedanttiwari641@gmail.com"
    
    class Config:
        env_file = ".env"
    
