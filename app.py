from flask import Flask, jsonify, g
#import the global proxy from Flask
#initialize an instance of the Flask Class
#import flask_cors
from flask_cors import CORS

#this starts the website!
app = Flask(__name__)
#MODELS
#import the models
import models
#RESOURCES (CONTROLLERS)
#import products from products resources
from resources.products import products
#set up CORS middleware, first is Blueprint second is array
CORS(products, origins=['http://localhost:3000'], supports_credentials = True)



#set up connection and close logic for requests
@app.before_request
def before_request():
    """Connect to the DATABASE before earch request"""
    g.db = models.DATABASE
    g.db.connect()
 
#our switchboard that determines which resource to direct the request
app.register_blueprint(products, url_prefix= '/api/v1/products')
     
@app.after_request
def after_request(response):
    """Close the DATABASE connection after each request"""
    g.db.close()
    return response
    
#default URL ends in localhost:8000/
@app.route('/')
def index():
    return 'ON'
#INITIATE SERVER
#run the app when the program starts!
DEBUG = True
PORT = 8000
if __name__ == '__main__':
    #call initialize from models.py
    models.initialize()
    app.run(debug=DEBUG, port=PORT)