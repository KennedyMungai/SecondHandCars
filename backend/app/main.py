"""The main python file for the backend"""
from database.db import init_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import auth_router
from routers.cars import cars_router

app = FastAPI(
    title="Second Hand Cars",
    description="The backend of a second hand cars app",
    version="0.1.0"
)

origins = ["https://localhost:3000", "http://localhost:300"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
)


@app.on_event("startup")
async def initialize_database():
    """Initializing the application connection to the database"""
    await init_db()


@app.get("/", tags=["Root"])
async def root():
    """The root endpoint of the application

    Returns:
        dict[str]: A message to show that the application works
    """
    return {"message": "Hello World"}

app.include_router(cars_router)
app.include_router(auth_router)
