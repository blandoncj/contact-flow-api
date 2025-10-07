from typing import List

from helpers.password_helper import hash_password
from repositories.user_repository import UserRepository
from exceptions.entity_exceptions import EntityAlreadyRegisteredException
from schemas.user_schema import (
    UserCreate, UserUpdate, UserResponse, UserResponseWithPassword
)


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def get_all(self) -> List[UserResponse]:
        return self.user_repository.get_all()

    def get_by_id(self, user_id: int) -> UserResponse:
        return self.user_repository.get_by_id(user_id)

    def get_by_username(self, username: str) -> UserResponseWithPassword | None:
        return self.user_repository.get_by_username(username)

    def validate_username(self, username: str) -> None:
        if self.get_by_username(username):
            raise EntityAlreadyRegisteredException('Username')

    def create(self, user: UserCreate) -> UserResponse:
        # validate if username already exists
        self.validate_username(user.username)

        # hash user password
        user.password = hash_password(user.password)
        return self.user_repository.create(user)

    def update(self, user_id: int, user: UserUpdate) -> UserResponse:
        existing_user = self.get_by_id(user_id)

        # validate username only if it was not the same as before
        if existing_user.username != user.username:
            self.validate_username(user.username)

        return self.user_repository.update(user_id, user)

    def delete(self, user_id: int) -> None:
        self.user_repository.delete(user_id)
