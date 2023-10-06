"""The oauth2 logic for creating JWT tokens"""
import os
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import find_dotenv, load_dotenv
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

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

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str) -> dict:
    """The function to verify a JWT token

    Args:
        token (str): The JWT token

    Returns:
        dict: The decoded JWT token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    except Exception as e:
        print(e)
        return None


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """The function to get the current user

    Args:
        token (str): The JWT token

    Returns:
        dict: The current user
    """
    return verify_access_token(token=token)
