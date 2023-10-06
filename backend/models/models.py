"""The model of the car data"""
from beanie import Document


class Cars(Document):
    """The model for the second hand cars

    Args:
        Document (_type_): The base for the models
    """
    brand: str
    make: str
    year: int
    price: int
    km: int
    gearbox: str
    doors: str
    imported: int
    kW: int
    cm3: int
    fuel: str
    registered: int
    color: str
    aircon: int
    damage: int
    car_type: str
    standard: int
    drive: str

    class Settings:
        """The name of the collection"""
        name = "second_hand_cars"

    class Config:
        """The configuration class for the model"""
        json_schema_extra = {
            "example": {
                "brand": "Mercedes",
                "make": "Some Pretentious Series of Letters and Spaces",
                "year": 1990,
                "price": 1000000,
                "km": 1200,
                "gearbox": "Something",
                "doors": "4/4",
                "imported": 0,
                "kW": 60,
                "cm3": 2000,
                "fuel": "petrol",
                "registered": 1,
                "color": "Black",
                "aircon": 3,
                "damage": 0,
                "car_type": "SUV",
                "standard": 4,
                "drive": "F"
            }
        }
