from typing import List

from fastapi import APIRouter, Depends

from routers.dependencies import oauth2_schema
from helpers.api_key_helper import get_api_key
from services.phone_service import PhoneService
from schemas.phone_schema import PhoneCreate, PhoneUpdate, PhoneResponse

phone_router = APIRouter(
    prefix='/phones',
    tags=['Phones'],
    dependencies=[Depends(get_api_key), Depends(oauth2_schema)]
)

phone_service = PhoneService()


@phone_router.get('/', response_model=List[PhoneResponse])
def get_phones():
    return phone_service.get_all()


@phone_router.get('/{phone_id}', response_model=PhoneResponse)
def get_phone(phone_id: int):
    return phone_service.get_by_id(phone_id)


@phone_router.get('/contact/{contact_id}', response_model=List[PhoneResponse])
def get_phones_by_contact(contact_id: int):
    return phone_service.get_by_contact(contact_id)


@phone_router.post('/', response_model=PhoneResponse)
def create_phone(phone: PhoneCreate):
    return phone_service.create(phone)


@phone_router.patch('/{phone_id}', response_model=PhoneResponse)
def update_phone(phone_id: int, phone: PhoneUpdate):
    return phone_service.update(phone_id, phone)


@phone_router.delete('/{phone_id}', status_code=204)
def delete_phone(phone_id: int):
    return phone_service.delete(phone_id)
