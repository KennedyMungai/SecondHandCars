"""The cars router file"""
from typing import List, Optional

from beanie.operators import In
from fastapi import APIRouter, HTTPException, status
from models.models import Cars

cars_router = APIRouter(prefix="/cars", tags=["Cars"])


@cars_router.get("/")
async def get_all_cars(
    skip: Optional[int] = 0,
    limit: Optional[int] = 100,
    search: Optional[str] = ''
) -> List[Cars]:
    """The endpoint to retrieve a bunch of cars

    Args:
        skip (Optional[int], optional): The pagination query parameter. Defaults to 0.
        limit (Optional[int], optional): The number of results per page. Defaults to 100.
        search (Optional[str], optional): The search parameter. Defaults to ''.

    Returns:
        List[Cars]: Returns a list of cars
    """
    return await Cars.find_all().skip(skip).limit(limit).to_list()


@cars_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_one_car(car: Cars) -> Cars:
    """The endpoint to add a car

    Args:
        car (Cars): The car to add

    Returns:
        Cars: The added car
    """
    return await car.create()
