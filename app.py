import os 
from flask import Flask, jsonify, g
#import the global proxy from Flask

from flask_login import LoginManager
#initialize an instance of the Flask Class
#import flask_cors
from flask_cors import CORS

#this starts the website!
app = Flask(__name__)
app.secret_key = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)

#MODELS
#import the models
import models
#RESOURCES (CONTROLLERS)
#import products from products resources
from resources.products import products
from resources.users import users 

CORS(products, origins=['http://localhost:3000', "https://trackingfreight.herokuapp.com"], supports_credentials = True)
CORS(users, origins=['http://localhost:3000', "https://trackingfreight.herokuapp.com"], supports_credentials= True)
#login
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None
    
@login_manager.unauthorized_handler
def unauthorized():
    return jsonify(
        data = {
            'error': 'User not logged in'
        }, status = {
            'code': 401,
            'message': 'You must be logged in to access that resource'
        }
    )

#set up CORS middleware, first is Blueprint second is array

#our switchboard that determines which resource to direct the request
app.register_blueprint(products, url_prefix='/api/v1/products')
app.register_blueprint(users, url_prefix='/api/v1/users')

#set up connection and close logic for requests
@app.before_request
def before_request():
    """Connect to the DATABASE before earch request"""
    g.db = models.DATABASE
    g.db.connect()

     
@app.after_request
def after_request(response):
    """Close the DATABASE connection after each request"""
    g.db.close()
    return response
    
#default URL localhost:8000/
@app.route('/')
def index():
    return 'ON'

#INITIATE SERVER
#run the app when the program starts!
DEBUG = True
PORT = 8000
if 'ON HEROKU' in os.environ:
    print('hitting products_app')
    # models.initialize()
if __name__ == '__main__':
    #call initialize from models.py
    models.initialize()
    app.run(debug=DEBUG, port=PORT)