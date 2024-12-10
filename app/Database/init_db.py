from tortoise import Tortoise, run_async
import dotenv
import os

dotenv.load_dotenv()

# Load the database URL from the environment variable
db_url: str = os.getenv("DATABASE_URL")

# Initialize Tortoise ORM
async def init_db():
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["Models.users_db"]}  # Point to the module where models are defined
    )
    # Generate schema (if needed)
    await Tortoise.generate_schemas()
    print("Tortoise-ORM is initialized and schema is created.")

# Close Tortoise connections
async def close_db():
    await Tortoise.close_connections()

if __name__ == "__main__":
    run_async(init_db())
