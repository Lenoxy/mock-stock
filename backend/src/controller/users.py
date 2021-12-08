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

    if stock_values:
        stock_values = finance.get_stock_values(stock_ids)

    for user in users:
        for stock in user.owned_stocks:
            user.money_in_stocks += user.owned_stocks[stock.upper()].amount * stock_values[stock.upper()]

    users = sorted(users, key=lambda user: user.money_in_stocks + user.money_liquid, reverse=True)

    return jsonify([u.to_dict() for u in users])


@users.route("/users/<string:username>")
def get_user(username):
    try:
        user = db.get_user(username)

        if not user:
            return f'Could not find user: {username}', 404

        money_in_stocks = 0.0

        owned_stocks = db.get_owned_stocks(username)
        if owned_stocks:
            stock_ids = [key for key in owned_stocks]
            stocks = finance.get_stocks(stock_ids)
            for stock in stocks:
                stock.amount = owned_stocks[stock.id].amount
                money_in_stocks += stock.amount * stock.value

            user.stocks = [stock.to_dict() for stock in stocks]

        # Calculation histories
        transactions = db.get_transactions(username)
        transactions = sorted(transactions, key=lambda t: t.datetime, reverse=True)

        histories = {
            'keys': [],
            'liquid_money': [],
            'stock_money': [],
            'score': []
        }
        tmp_money_liquid = user.money_liquid
        tmp_stock_money = money_in_stocks

        # Appending first current value to history
        histories['keys'].append(datetime.now().isoformat())
        histories['liquid_money'].append(tmp_money_liquid)
        histories['stock_money'].append(money_in_stocks)
        histories['score'].append(tmp_money_liquid + tmp_stock_money)

        for t in transactions:
            histories['keys'].append(t.datetime)
            histories['liquid_money'].append(tmp_money_liquid + t.amount * t.stock_price)
            histories['stock_money'].append(tmp_stock_money - t.amount * t.stock_price)
            histories['score'].append((tmp_money_liquid + t.amount * t.stock_price) + (tmp_stock_money - t.amount * t.stock_price))

            tmp_money_liquid += t.amount * t.stock_price
            tmp_stock_money -= t.amount * t.stock_price

        user.histories = histories

        user.money_in_stocks = money_in_stocks
        return user.to_dict()

    except Exception as e:
        return str(e), 400