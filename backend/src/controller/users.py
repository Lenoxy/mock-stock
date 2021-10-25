from flask import Blueprint
import db

users = Blueprint('users', __name__)

@users.route("/users")
def get_users():
    return db.get_users()

@users.route("/users/<string:username>/stocks")
def get_users_stock(username):
    andsomedbcalls = "not implemented as well"

    return f'Should return stocks from {username}. Not yet implemented, do it bitch!'
