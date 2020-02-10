import datetime
#import everything from peewee
from peewee import *

#DATABASE
DATABASE = SqliteDatabase('products2.sqlite')


#MODELS
class Product(Model):
    name = CharField()
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
    DATABASE.create_tables([Product], safe=True)
    print('Products Table Created')
    DATABASE.close()
