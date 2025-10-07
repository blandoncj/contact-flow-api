from peewee import DoesNotExist

from models.user_model import UserModel
from repositories.base_repository import BaseRepository
from schemas.user_schema import UserResponse, UserResponseWithPassword


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserModel, UserResponse)

    def get_by_username(self, username: str) -> UserResponseWithPassword | None:
        try:
            existing_user = UserModel.get(UserModel.username == username)
            return UserResponseWithPassword.model_validate(existing_user)
        except DoesNotExist:
            return None
