from typing import List

from fastapi import APIRouter, Depends

from services.user_service import UserService
from routers.dependencies import oauth2_schema
from helpers.api_key_helper import get_api_key
from schemas.user_schema import UserCreate, UserUpdate, UserResponse

user_router = APIRouter(
    prefix='/users',
    tags=['Users'],
    dependencies=[Depends(get_api_key), Depends(oauth2_schema)]
)

user_service = UserService()


@user_router.get('/', response_model=List[UserResponse])
def get_users():
    return user_service.get_all()


@user_router.post('/', response_model=UserResponse)
def create_user(user: UserCreate):
    return user_service.create(user)


@user_router.get('{user_id}', response_model=UserResponse)
def get_user(user_id: int):
    return user_service.get_by_id(user_id)


@user_router.patch('{user_id}', response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    return user_service.update(user_id, user)
