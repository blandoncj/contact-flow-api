import os

from dotenv import load_dotenv
from peewee import MySQLDatabase

load_dotenv()

db = MySQLDatabase(
    os.getenv('MYSQL_DATABASE'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    host=os.getenv('MYSQL_HOST'),
    port=int(os.getenv('MYSQL_PORT'))
)


def get_db():
    if db.is_closed():
        db.connect()
    return db
