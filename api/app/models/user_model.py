from peewee import AutoField, BooleanField, CharField, Model

from config.database import get_db


class UserModel(Model):
    id = AutoField()
    fullname = CharField(max_length=50)
    username = CharField(max_length=15, unique=True)
    password = CharField(max_length=15)
    is_active = BooleanField(default=True)

    class Meta:
        database = get_db()
        table_name = 'users'
