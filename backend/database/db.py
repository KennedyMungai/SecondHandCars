"""The config python file for the databases"""
from beanie import init_beanie
from models.models import Cars
from motor.motor_asyncio import AsyncIOMotorClient


async def init_db():
    """The function needed to initialize the database connection"""
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.Cars, document_models=[Cars])
