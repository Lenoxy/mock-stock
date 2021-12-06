from flask import Blueprint, jsonify
from datetime import datetime
import finance
import db

users = Blueprint('users', __name__)


@users.route("/users")
def get_users():
    users = db.get_users()
    stock_ids = []
    stock_values = {}
    for user in users:
        user.owned_stocks = db.get_owned_stocks(user.username)
        for stock in user.owned_stocks:
            if not stock.upper() in stock_ids:
                stock_ids.append(stock.upper())

    stock_values = finance.get_stock_values(stock_ids)

    for user in users:
        for stock in user.owned_stocks:
            print(stock_values)
            print(user.owned_stocks)
            user.money_in_stocks += user.owned_stocks[stock.upper()].amount * stock_values[stock.upper()]

    users = sorted(users, key=lambda user: user.money_in_stocks + user.money_liquid, reverse=True)

    return jsonify([u.to_dict() for u in users])


@users.route("/users/<string:username>")
def get_user(username):
    try:
        user = db.get_user(username)
        money_in_stocks = 0.0

        owned_stocks = db.get_owned_stocks(username)
        if owned_stocks:
            stock_ids = [key for key in owned_stocks]
            stocks = finance.get_stocks(stock_ids)
            for stock in stocks:
                stock.amount = owned_stocks[stock.id].amount
                money_in_stocks += stock.amount * stock.value

            user.stocks = [stock.to_dict() for stock in stocks]

        user.money_in_stocks = money_in_stocks
        return user.to_dict()

    except Exception as e:
        return str(e), 400


@users.route("/users/<string:username>/histories")
def get_user_stocks(username):
    try:
        user = db.get_user(username)

        transactions = db.get_transactions(username)
        print(transactions)
        transactions = sorted(transactions, key=lambda t: t.datetime, reverse=True)

        liquid_money_set = {}
        liquid_money_set[datetime.now().isoformat()] = user.money_liquid
        for t in transactions:
            liquid_money_set[t.datetime] = user.money_liquid + t.amount * t.stock_price
            user.money_liquid += t.amount * t.stock_price

        return jsonify(liquid_money_set)


    except Exception as e:
        return str(e), 400