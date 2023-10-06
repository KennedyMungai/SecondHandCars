"""The application auth router"""
from fastapi import APIRouter, HTTPException, status
from models.models import Users
from utils.password_hashing import hash_password, verify_password
from utils.oauth2 import create_access_token


auth_router = APIRouter(prefix='/auth', tags=["Auth"])


@auth_router.post('/login')
async def user_login(user_data: Users):
    db_user = await Users.get(user_data._id)

    if not db_user or verify_password(user_data.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(data={"sub": db_user._id})

    return {"access_token": access_token, "token_type": "bearer"}
