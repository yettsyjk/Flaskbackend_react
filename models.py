import os
import datetime
from playhouse.db_url import connect
#import everything from peewee
from peewee import *
from flask_login import UserMixin

#DATABASE
# DATABASE = SqliteDatabase('products.sqlite')
#replace your database definition withi this block
if 'ON HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))
else:
    DATABASE = PostgresqlDatabase('products_app')

#MODELS
class User (UserMixin, Model):
    email = CharField(unique = True)
    password = CharField(max_length=10)
    
    class Meta:
        database = DATABASE
        
class Product(Model):
    load_name = CharField(unique = True)
    cost_of_load = CharField(null= False)
    trucking_company = CharField()
    bol_number = CharField()
    travel_days_required = CharField()
    estimated_date_arrival = CharField()
    point_of_contact = CharField()
    num_of_pallets = CharField()
    originating_port = CharField()
    recent_terminal = CharField()
    date_last_terminal = CharField()
    owner_id = ForeignKeyField(User, backref="products")
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Product, User], safe=True)
    print('Products and Users Tables Created')
    DATABASE.close()
