from typing import List

from models.phone_model import PhoneModel
from schemas.phone_schema import PhoneResponse
from repositories.base_repository import BaseRepository


class PhoneRepository(BaseRepository):
    def __init__(self):
        super().__init__(PhoneModel, PhoneResponse)

    def get_by_contact(self, contact_id: int) -> List[PhoneResponse]:
        phones = PhoneModel.select().where(PhoneModel.contact == contact_id)
        return [PhoneResponse.model_validate(phone) for phone in phones]
