"""The main python file for the backend"""
from fastapi import FastAPI
from database.db import init_db


app = FastAPI(
    title="Second Hand Cars",
    description="The backend of a second hand cars app",
    version="0.1.0"
)


@app.on_event("startup")
async def initialize_database():
    """Initializing the application connection to the database"""
    await init_db()


@app.get("/")
async def root() -> dict[str]:
    """The root endpoint of the application

    Returns:
        dict[str]: A message to show that the application works
    """
    return {"message": "Hello World"}
