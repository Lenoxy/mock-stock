import db
from flask import Blueprint, jsonify

users = Blueprint('users', __name__)


@users.route("/users")
def get_users():
    return jsonify([u.to_json() for u in db.get_users()])
    # return db.get_user('Leo1').to_json()


@users.route("/users/<string:username>/stocks")
def get_users_stock(username):
    andsomedbcalls = "not implemented as well"

    return f'Should return stocks from {username}. Not yet implemented, do it bitch!'
