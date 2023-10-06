"""The oauth2 logic for creating JWT tokens"""
import os
from datetime import datetime, timedelta

from dotenv import find_dotenv, load_dotenv
from jose import JWTError, jwt

load_dotenv(find_dotenv())

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")


def create_access_token(data: dict) -> str:
    """The function to create a JWT token

    Args:
        data (dict): The data used to create a JWt token

    Returns:
        str: The jwt token
    """
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
