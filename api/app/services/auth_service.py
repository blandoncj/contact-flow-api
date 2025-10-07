import os

from jose import jwt
from dotenv import load_dotenv
from fastapi.exceptions import HTTPException

from models.user_model import UserModel
from services.user_service import UserService
from helpers.password_helper import check_password
from schemas.user_schema import UserAuth, UserCreate, UserResponse

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = 'HS256'


class AuthService:
    def __init__(self):
        self.user_service = UserService()

    def encode_token(self, payload: dict) -> str:
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token

    def decode_token(self, token: str) -> UserResponse:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = UserModel.get_by_id(data['id'])
        return UserResponse.model_validate(user)

    def authenticate(self, user: UserAuth) -> dict:
        existing_user = self.user_service.get_by_username(user.username)

        if not existing_user or not check_password(
                user.password, existing_user.password):
            raise HTTPException(status_code=400, detail='Invalid credentials')

        if not existing_user.is_active:
            raise HTTPException(status_code=400, detail='Inactive user')

        token_data = {
            'id': existing_user.id,
            'fullname': existing_user.fullname,
            'username': existing_user.username,
            'is_active': existing_user.is_active
        }

        token = self.encode_token(token_data)

        return {'access_token': token}

    def create_user(self, user: UserCreate) -> UserResponse:
        return self.user_service.create(user)
