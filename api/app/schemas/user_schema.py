from pydantic import Field

from schemas.base_schema import BaseSchema


class UserCreate(BaseSchema):
    fullname: str = Field(..., min_length=3, max_length=50)
    username: str = Field(..., min_length=3, max_length=15)
    password: str = Field(..., min_length=6, max_length=15)


class UserUpdate(BaseSchema):
    fullname: str | None = Field(None, min_length=3, max_length=50)
    username: str | None = Field(None, min_length=3, max_length=15)
    password: str | None = Field(None, min_length=6, max_length=15)


class UserResponse(BaseSchema):
    id: int
    fullname: str
    username: str
    is_active: bool


class UserResponseWithPassword(UserResponse):
    password: str


class UserResponseWithToken(BaseSchema):
    user: UserResponse
    token: str


class UserAuth(BaseSchema):
    username: str
    password: str
