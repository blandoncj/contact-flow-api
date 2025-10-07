from typing import List

from models.contact_model import ContactModel
from schemas.contact_schema import ContactResponse
from repositories.base_repository import BaseRepository


class ContactRepository(BaseRepository):
    def __init__(self):
        super().__init__(ContactModel, ContactResponse)

    def get_by_user(self, user_id: int) -> List[ContactResponse]:
        contacts = ContactModel.select().where(ContactModel.user == user_id)
        return [
            ContactResponse.model_validate(contact) for contact in contacts
        ]
