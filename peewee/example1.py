from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.


db.connect()

db.create_tables([Person])

test1 = Person(name='Dave', birthday=date(1978, 1, 1))
test1.save()
