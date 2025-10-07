from typing import List

from repositories.phone_repository import PhoneRepository
from repositories.contact_repository import ContactRepository
from schemas.phone_schema import PhoneCreate, PhoneUpdate, PhoneResponse


class PhoneService:
    def __init__(self):
        self.phone_repository = PhoneRepository()
        self.contact_repository = ContactRepository()

    def validate_contact_exists(self, contact_id):
        return self.contact_repository.get_by_id(contact_id)

    def get_all(self) -> List[PhoneResponse]:
        return self.phone_repository.get_all()

    def get_by_id(self, phone_id: int) -> PhoneResponse:
        return self.phone_repository.get_by_id(phone_id)

    def get_by_contact(self, contact_id: int) -> List[PhoneResponse]:
        # validate if contact exists
        self.validate_contact_exists(contact_id)
        return self.phone_repository.get_by_contact(contact_id)

    def create(self, phone: PhoneCreate) -> PhoneResponse:
        # validate if contact exists
        self.validate_contact_exists(phone.contact_id)
        return self.phone_repository.create(phone)

    def update(self, phone_id: int, phone: PhoneUpdate) -> PhoneResponse:
        return self.phone_repository.update(phone_id, phone)

    def delete(self, phone_id: int) -> None:
        self.phone_repository.delete(phone_id)
