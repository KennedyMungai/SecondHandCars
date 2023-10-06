"""The model of the car data"""
from beanie import Document, PydanticObjectId


class Cars(Document):
    """The model for the second hand cars

    Args:
        Document (_type_): The base for the models
    """
    _id: PydanticObjectId
    brand: str
    make: str
    year: int
    price: int
    km: int
    cm3: int

    class Settings:
        """The name of the collection"""
        name = "second_hand_cars"

    class Config:
        """The configuration class for the model"""
        json_schema_extra = {
            "example": {
                "_id": "e1c5d5sd1c5dc5sd5",
                "brand": "Mercedes",
                "make": "Something Fancy",
                "year": 2005,
                "price": 1000000,
                "km": 2000,
                "cm3": 2000
            }
        }


class Users(Document):
    _id: PydanticObjectId
    email: str
    password_hash: str

    class Settings:
        name = "users_collection"

    class Config:
        json_schema_extras = {
            "example": {
                "_id": "e1c5d5sd1c5dc5sd5",
                "email": "XXXXXXXXXXXX",
                "password_hash": "XXXXXXXXXXXX"
            }
        }
