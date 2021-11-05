from flask import Blueprint, request
from flask_login import login_user, logout_user, login_required, current_user
import db
from hashlib import sha512
from models import User

auth = Blueprint('auth', __name__)

@auth.route("/auth/register", methods=['POST'])
def register_user():
    auth_request = request.json

    username = auth_request.get('username')
    password = auth_request.get('password') 

    try:
        user = User()
        user.username = username
        user.password_hash = sha512(password.encode('utf-8')).hexdigest()
        user.money_liquid = 20000.0
        user = db.create_user(user)
        login_user(user)

        return 'User registered and logged in'

    except Exception as e:
        print(e)
        return str(e), 400


@auth.route("/auth/login", methods=['POST'])
def post_login():
    auth_request = request.json

    username = auth_request.get('username')
    password_hash = sha512(auth_request.get('password').encode('utf-8')).hexdigest()

    try:
        user = db.get_user(username)
        if user.password_hash == password_hash:
            login_user(user)
            return 'User successfuly logged in'
        return f'Wrong password dude', 401
    except Exception as e:
        return str(e), 400


@auth.route("/auth/logout")
@login_required
def get_logout():
    logout_user()
    return 'Succesfully logged out', 200