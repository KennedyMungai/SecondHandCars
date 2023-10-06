"""The cars router file"""
from fastapi import APIRouter, HTTPException, status
from models.models import Cars
from typing import Optional, List


cars_router = APIRouter(prefix="/cars", tags=["Cars"])


@cars_router.get("/")
async def get_all_cars(
    skip: Optional[int] = 0,
    limit: Optional[int] = 100,
    brand: Optional[str] = ''
) -> List[Cars]:
    """Get all cars"""
    return Cars.find_all(lazy_parse=True).skip(skip).limit(limit).filter(brand).to_list()
