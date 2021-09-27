from flask import Blueprint

users = Blueprint('users', __name__)

@users.route("/users")
def get_users():
    andsomedbcalls = "not implemented as well"

    return f'Should return them Users. Not yet implemented, do it bitch!'

@users.route("/users/<string:username>/stocks")
def get_users_stock(username):
    andsomedbcalls = "not implemented as well"

    return f'Should return stocks from {username}. Not yet implemented, do it bitch!'
