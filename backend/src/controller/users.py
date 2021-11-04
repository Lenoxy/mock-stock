import db
from flask import Blueprint, jsonify
import finance

users = Blueprint('users', __name__)


@users.route("/users")
def get_users():
    return jsonify([u.to_dict() for u in db.get_users()])


@users.route("/users/<string:username>")
def get_user(username):
    try:
        user = db.get_user(username)
        money_in_stocks = 0.0

        owned_stocks = db.get_owned_stocks(username)
        stock_ids = [key for _, key in enumerate(owned_stocks)]
        stocks = finance.get_stocks(stock_ids)
        for stock in stocks:
            stock.amount = owned_stocks[stock.id].amount
            money_in_stocks += stock.amount * finance.get_stock_value(stock.id)

        user.money_in_stocks = money_in_stocks
        user.stocks = [stock.to_dict() for stock in stocks]
        return user.to_dict()

    except Exception as e:
        return str(e), 400