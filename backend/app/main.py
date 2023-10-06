"""The main python file for the backend"""
from fastapi import FastAPI


app = FastAPI(
    title="Second Hand Cars", 
    description="The backend of a second hand cars app", 
    version="0.1.0"
)


@app.get("/")
async def root() -> dict[str]:
    """The root endpoint of the application

    Returns:
        dict[str]: A message to show that the application works
    """
    return {"message": "Hello World"}