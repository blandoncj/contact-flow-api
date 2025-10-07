from typing import List

from peewee import DoesNotExist, Model
from pydantic import BaseModel

from helpers.password_helper import hash_password
from exceptions.entity_exceptions import EntityNotFoundException


class BaseRepository:
    def __init__(self, model: Model, schema: BaseModel):
        self.model = model
        self.schema = schema

    def get_all(self) -> List[BaseModel]:
        return [
            self.schema.model_validate(item) for item in self.model.select()
        ]

    def get_by_id(self, id: int) -> BaseModel:
        try:
            return self.schema.model_validate(self.model.get_by_id(id))
        except DoesNotExist:
            raise EntityNotFoundException(self.model.__name__, id)

    def create(self, data: BaseModel) -> BaseModel:
        obj = self.model.create(**data.model_dump())
        return self.schema.model_validate(obj)

    def update(self, id: int, data: BaseModel) -> BaseModel:
        try:
            existing_item = self.model.get_by_id(id)

            for key, value in data.model_dump(exclude_unset=True).items():
                if key == 'password' and value:
                    value = hash_password(value)
                setattr(existing_item, key, value)

            existing_item.save()
            return self.schema.model_validate(existing_item)
        except DoesNotExist:
            raise EntityNotFoundException(self.model.__name__, id)

    def delete(self, id: int) -> None:
        try:
            self.model.get_by_id(id).delete_instance()
        except DoesNotExist:
            raise EntityNotFoundException(self.model.__name__, id)
