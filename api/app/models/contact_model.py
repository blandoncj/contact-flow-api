from peewee import AutoField, BooleanField, CharField, ForeignKeyField, Model

from config.database import get_db
from models.user_model import UserModel


class ContactModel(Model):
    id = AutoField()
    firstname = CharField(max_length=50)
    lastname = CharField(max_length=50, null=True)
    email = CharField(max_length=50, null=True)
    is_favorite = BooleanField(default=False)
    user = ForeignKeyField(
        UserModel,
        column_name='user_id',
        backref='contacts',
        on_delete='CASCADE'
    )

    class Meta:
        database = get_db()
        table_name = 'contacts'
