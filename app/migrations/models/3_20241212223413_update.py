from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "blogs" (
    "blog_id" BIGSERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(300) NOT NULL,
    "body" TEXT NOT NULL,
    "slug" VARCHAR(100) NOT NULL UNIQUE,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id_id" VARCHAR(100) NOT NULL REFERENCES "users" ("userid") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "blogs";"""
