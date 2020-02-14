from flask import request, jsonify, Blueprint
from flask-bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user


import models 

users = Blueprint('users', 'users')

@users.route('/register', methods = ["POST"])
def register():
    payload = rquest.get_json()
    payload['email'].lower()
    
    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(data={}, status={'code:': 400, 'message:' 'A user with taht email alreadt exists'}) 
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        return