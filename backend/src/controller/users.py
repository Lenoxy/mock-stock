from flask import Blueprint, jsonify
import finance
import db

users = Blueprint('users', __name__)


@users.route("/users")
def get_users():
    users = db.get_users()
    stock_ids = []
    for user in users:
        user.owned_stocks = db.get_owned_stocks(user.username)
        for stock in user.owned_stocks:
            if not stock in stock_ids:
                stock_ids.append(stock)

    stock_values = finance.get_stock_values(stock_ids)

    for user in users:
        for stock in user.owned_stocks:
            user.money_in_stocks += user.owned_stocks[stock].amount * stock_values[stock]

    return jsonify([u.to_dict() for u in users])


@users.route("/users/<string:username>")
def get_user(username):
    try:
        user = db.get_user(username)
        money_in_stocks = 0.0

        owned_stocks = db.get_owned_stocks(username)
        if owned_stocks:
            stock_ids = [key for _, key in enumerate(owned_stocks)]
            stocks = finance.get_stocks(stock_ids)
            for stock in stocks:
                stock.amount = owned_stocks[stock.id].amount
                money_in_stocks += stock.amount * stock.value

            user.stocks = [stock.to_dict() for stock in stocks]

        user.money_in_stocks = money_in_stocks
        return user.to_dict()

    except Exception as e:
        return str(e), 400