import dotenv
import os
dotenv.load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["Models.users_db", "aerich.models"],
            "default_connection": "default",
        },
    },
}

