"""The application auth router"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from models.models import Users
from utils.oauth2 import create_access_token
from utils.password_hashing import hash_password, verify_password

auth_router = APIRouter(prefix='/auth', tags=["Auth"])


@auth_router.post('/login')
async def user_login(user_data: OAuth2PasswordRequestForm = Depends()):
    db_user = await Users.find_one({"email": user_data.username})

    if not db_user or verify_password(user_data.password, db_user.password_hash) == False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(data={"sub": db_user.email})

    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.post(
    '/register',
    status_code=status.HTTP_201_CREATED
)
async def user_register(user_data: Users):
    user_data.password_hash = hash_password(user_data.password_hash)

    await user_data.create()

    return {"message": "User created successfully"}
