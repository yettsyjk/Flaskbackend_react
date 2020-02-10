# Flaskbackend_react
# App created by Software Developer Yettsy Knapp located in Denver, CO
1. Let's connect [www.linkedin.com/in/yettsy-jo-knapp] [www.github.com/yettsyjk]
1. Capstone Project February 2020
1. Flask back-end repo found on my github: [https://github.com/yettsyjk/Flaskbackend_react.git]
1. React front-end repo found on my guthub: [https://github.com/yettsyjk/ReactFrontEnd_Flask.git]
1. Capstone project Trello link: [https://trello.com/b/wDbzPVBC]

## Reason for Freight Tracking App
1. My goal is to create a better form of tracking LTL Freight for businesses with 1 Logistic Manager to accurately track incoming freight and better report to business owner.
## LTL Freight Tracking App created with Flask Python3 back-end and React Javascript for front-end.
## 
## User Story:
1. User will be able to create card with pertinent information regarding less than truckload pallet location and estimated travel time.
1. User will be able to read card attributes to that client identifies as important to track.
1. User will be able to update 
1. User will be able to delete cards pertaining freight that has been delivered and no longer tracking
## Flask back-end Models for product tracking:
` class Product(Model):
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
    date_last_terminal = CharField() `

## Stretch Goals:
1. Attach Map API within the dashboard user card, allowing the user to view a map for better user experience

## Setup Flask Python3 back-end
1. Let's also build a virtual environment. 
1. Virtual environments allow us to have multiple versions of Python on the same system so we can have different versions of both Python and the packages we are using on our computers.

## Setting up environment for production development
# Run the following commands:
` virtualenv .env -p python3 `
` source .env/bin/activate `
` (If virtualenv isn't recognized, you may need to run pip3 install virtualenv.) `

## Notice that (.env) is now prepended to your command line. 1. Make sure that you see that when you're working on your Flask app.

## Now let's set up our dependencies by running the following commands (if you get an error regarding psycopg2, try running pip3 install psycopg2-binary instead):
` pip3 install flask-bcrypt peewee flask psycopg2 flask_login flask_cors `
` pip3 freeze > requirements.txt `
1. We'll run the Flask app like any other app.

1. This process is similar to what we did with our Express apps, but we just do the process backwards. Instead of first creating the file that keeps track of our dependences (like package.json did in Express), we install our app and dependences(the pip3 install command). Then, we save all our dependencies to a text file that will keep track of them (the pip3 freeze command) within our virtualenv.

1. This means that, in the same way that we could clone a project and just run npm i or npm install because all the dependencies were listed in package.json, in Flask, we can clone a project and run 
`` pip3 install -r requirements.txt which will read and install the dependencies in requirements.txt.

1. Create a .gitignore file and enter the following lines inside it:
.env
*.sqlite
*.pyc
This prevents our environment directory, any sqlite database files, and any pycache files from being tracked by git.

Setting up a basic server
Create a file called app.py.
In app.py:

from flask import Flask
# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / (e.g., "my-website.com/").
` @app.route('/')
def index():
    return 'hi' `

# Run the app when the program starts!
`   DEBUG = True
    PORT = 8000
    if __name__ == '__main__':
        app.run(debug=DEBUG, port=PORT) `
To run our server, we will run this command:

1. python3 app.py

## Now go to:

` http://localhost:8000/ `

1. You made a Flask web app!
