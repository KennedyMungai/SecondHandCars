"""The python script for password hashing"""
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """The function to hash a password

    Args:
        password (str): The password

    Returns:
        str: The password hash
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """The function to verify a password hash

    Args:
        plain_password (str): The plain password
        hashed_password (str): The hashed password

    Returns:
        bool: Shows if the plain_password matches the has password
    """
    return pwd_context.verify(plain_password, hashed_password)
