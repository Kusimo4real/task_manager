from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import os

class Database:
    client: Optional[AsyncIOMotorClient] = None
    database = None

db = Database()

async def get_database():
    return db.database

async def connect_to_mongo():
    """Create database connection"""
    db.client = AsyncIOMotorClient(os.getenv("DATABASE_URL"))
    db.database = db.client.task_manager

async def close_mongo_connection():
    """Close database connection"""
    if db.client:
        db.client.close()