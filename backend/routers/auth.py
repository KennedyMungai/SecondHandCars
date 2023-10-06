"""The application auth router"""
from fastapi import APIRouter


auth_router = APIRouter(prefix='/auth', tags=["Auth"])
