from typing import List

from repositories.user_repository import UserRepository
from repositories.contact_repository import ContactRepository
from schemas.contact_schema import (
    ContactResponse, ContactCreate, ContactUpdate
)


class ContactService:
    def __init__(self):
        self.contact_repository = ContactRepository()
        self.user_repository = UserRepository()

    def validate_user_exists(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def get_all(self) -> List[ContactResponse]:
        return self.contact_repository.get_all()

    def get_by_id(self, contact_id: int) -> ContactResponse:
        return self.contact_repository.get_by_id(contact_id)

    def get_by_user(self, user_id: int) -> List[ContactResponse]:
        # validate if user exists
        self.validate_user_exists(user_id)
        return self.contact_repository.get_by_user(user_id)

    def create(self, contact: ContactCreate) -> ContactResponse:
        # validate if user exists
        self.validate_user_exists(contact.user_id)
        return self.contact_repository.create(contact)

    def update(self, contact_id: int, contact: ContactUpdate) -> ContactResponse:
        return self.contact_repository.update(contact_id, contact)

    def delete(self, contact_id) -> None:
        return self.contact_repository.delete(contact_id)
