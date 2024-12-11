from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "sessions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "token" TEXT NOT NULL,
    "createdAt" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "isActive" BOOL NOT NULL  DEFAULT True,
    "userid_id" VARCHAR(100) NOT NULL REFERENCES "users" ("userid") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "sessions";"""
