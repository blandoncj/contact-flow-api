from pydantic import Field

from schemas.base_schema import BaseSchema


class PhoneBase(BaseSchema):
    number: str = Field(
        ..., min_length=7, max_length=15, example='+571234567890'
    )


class PhoneCreate(PhoneBase):
    contact_id: int


class PhoneUpdate(PhoneBase):
    pass


class PhoneResponse(PhoneBase):
    id: int
    contact_id: int
