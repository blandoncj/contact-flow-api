from typing import List

from fastapi import APIRouter, Depends

from routers.dependencies import oauth2_schema
from helpers.api_key_helper import get_api_key
from services.contact_service import ContactService
from schemas.contact_schema import (
    ContactCreate, ContactUpdate, ContactResponse
)

contact_router = APIRouter(
    prefix='/contacts',
    tags=['Contacts'],
    dependencies=[Depends(get_api_key), Depends(oauth2_schema)]
)

contact_service = ContactService()


@contact_router.get('/', response_model=List[ContactResponse])
def get_contacts():
    return contact_service.get_all()


@contact_router.get('/{contact_id}', response_model=ContactResponse)
def get_contact(contact_id: int):
    return contact_service.get_by_id(contact_id)


@contact_router.get('/user/{user_id}', response_model=List[ContactResponse])
def get_contacts_by_user(user_id: int):
    return contact_service.get_by_user(user_id)


@contact_router.post('/', response_model=ContactResponse)
def create_contact(contact: ContactCreate):
    return contact_service.create(contact)


@contact_router.patch('/{contact_id}', response_model=ContactResponse)
def update_contact(contact_id: int, contact: ContactUpdate):
    return contact_service.update(contact_id, contact)


@contact_router.delete('/{contact_id}', status_code=204)
def delete_contact(contact_id: int):
    return contact_service.delete(contact_id)
