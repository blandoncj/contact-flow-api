from pydantic import EmailStr, Field

from schemas.base_schema import BaseSchema


class ContactBase(BaseSchema):
    lastname: str | None = Field(None, max_length=50)
    email: EmailStr | None = Field(None, max_length=50)
    is_favorite: bool = False


class ContactCreate(ContactBase):
    firstname: str = Field(..., max_length=50)
    user_id: int


class ContactUpdate(ContactBase):
    firstname: str = Field(None, max_length=50)


class ContactResponse(ContactBase):
    id: int
    firstname: str
    user_id: int
