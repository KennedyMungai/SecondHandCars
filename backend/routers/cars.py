"""The cars router file"""
from typing import List, Optional

from beanie import PydanticObjectId
from beanie.operators import In
from fastapi import APIRouter, HTTPException, status
from models.models import Cars

cars_router = APIRouter(prefix="/cars", tags=["Cars"])


@cars_router.get("/")
async def get_all_cars(
    skip: Optional[int] = 0,
    limit: Optional[int] = 100,
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


@cars_router.get("/{car_id}")
async def get_one_car(car_id: PydanticObjectId) -> Cars:
    """The endpoint to retrieve one car

    Args:
        car_id (PydanticObjectId): The database id of the car

    Returns:
        Cars: The retrieved car
    """
    car = Cars.get(car_id)

    if not car:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")


@cars_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_one_car(car: Cars) -> Cars:
    """The endpoint to add a car

    Args:
        car (Cars): The car to add

    Returns:
        Cars: The added car
    """
    try:
        return await car.create()
    except:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Something Went Wrong")


@cars_router.put("/{car_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_one_car(car_id: PydanticObjectId, car: Cars) -> Cars:
    """The endpoint to update a car

    Args:
        car_id (PydanticObjectId): The database id of the car
        car (Cars): The car to update

    Returns:
        Cars: The updated car
    """
    car_to_update = Cars.get(car_id)

    if not car_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Car not found")

    car_to_update.brand = car.brand
    car_to_update.make = car.make
    car_to_update.year = car.year
    car_to_update.price = car.price
    car_to_update.km = car.km
    car_to_update.cm3 = car.cm3

    await car_to_update.save()

    return car_to_update
