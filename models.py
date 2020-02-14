import datetime
#import everything from peewee
from peewee import *
import flask_login import UserMixin

#DATABASE
DATABASE = SqliteDatabase('products3.sqlite')


#MODELS
class User (UserMixin, Model):
    email = Charfield(unique = True)
    password = CharField()
    
    class Meta:
        database = DATABASE
        
class Product(Model):
    name = CharField(unique = True)
    cost_of_load = CharField()
    trucking_company = CharField()
    bol_number = CharField()
    travel_days_required = CharField()
    estimated_date_arrival = CharField()
    point_of_contact = CharField()
    num_of_pallets = CharField()
    originating_port = CharField()
    recent_terminal = CharField()
    date_last_terminal = CharField()
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Product, User], safe=True)
    print('Products and Users Tables Created')
    DATABASE.close()
