from peewee import AutoField, CharField, ForeignKeyField, Model

from config.database import get_db
from models.contact_model import ContactModel


class PhoneModel(Model):
    id = AutoField()
    number = CharField(max_length=15)
    contact = ForeignKeyField(
        ContactModel,
        column_name='contact_id',
        backref='phones',
        on_delete='CASCADE'
    )

    class Meta:
        database = get_db()
        table_name = 'phones'
