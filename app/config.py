# from pydantic_settings import BaseSettings  
from pydantic import BaseSettings
import dotenv
import os
dotenv.load_dotenv()

class Settings(BaseSettings):
    title_name : str = "RBlog"
    admin_email : str =  os.getenv("ADMIN_EMAIL")
    
    class Config:
        env_file = ".env"
    
