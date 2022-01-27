from flask import Blueprint, jsonify
from datetime import datetime
import finance
import db


users = Blueprint('users', __name__)


@users.route("/users")
def get_users():
    users = db.get_users()
    new_users = []
    for user in users:
        if hasattr(user, 'username'):
            new_users.append(user)

    users = new_users
    stock_ids = []
    stock_values = {}
    for user in users:
        user.owned_stocks = db.get_owned_stocks(user.username)
        for stock in user.owned_stocks:
            if not stock.upper() in stock_ids and stock == 'INTEW':
                stock_ids.append(stock.upper())

    if stock_ids:
        stock_values = finance.get_stock_values(stock_ids)

    for user in users:
        for stock in user.owned_stocks:
            if stock != 'INTEW':
                if not finance.isNaN(stock_values[stock.upper()]):
                    user.money_in_stocks += user.owned_stocks[stock.upper()].amount * stock_values[stock.upper()]

    users = sorted(users, key=lambda user: user.money_in_stocks + user.money_liquid, reverse=True)

    return jsonify([u.to_dict() for u in users])


@users.route("/users/<string:username>")
def get_user(username):
    try:
        user = db.get_user(username)

        if not user:
            return f'Could not find user: {username}', 404

        user.money_in_stocks = 0.0

        owned_stocks = db.get_owned_stocks(username)
        if owned_stocks:
            stock_ids = [key for key in owned_stocks]
            stocks = finance.get_stocks(stock_ids)
            for stock in stocks:
                if finance.isNaN(stock.value):
                    stock.value = 0
                stock.amount = owned_stocks[stock.id].amount
                user.money_in_stocks += stock.amount * stock.value

            user.stocks = [stock.to_dict() for stock in stocks]

        # Calculation histories
        transactions = db.get_transactions(username)

        if transactions:
            transactions = sorted(transactions, key=lambda t: t.datetime, reverse=True)

            histories = {
                'keys': [],
                'liquid_money': [],
                'stock_money': [],
                'score': []
            }
            tmp_money_liquid = user.money_liquid
            tmp_stock_money = user.money_in_stocks

            # Appending current value to history
            histories['keys'].append(datetime.now().isoformat())
            histories['liquid_money'].append(tmp_money_liquid)
            histories['stock_money'].append(user.money_in_stocks)
            histories['score'].append(tmp_money_liquid + tmp_stock_money)

            for t in transactions:

                histories['keys'].append(t.datetime)
                histories['liquid_money'].append(tmp_money_liquid)
                histories['stock_money'].append(tmp_stock_money)
                histories['score'].append(tmp_money_liquid + tmp_stock_money)

                tmp_money_liquid += t.amount * t.stock_price
                tmp_stock_money -= t.amount * t.stock_price

            histories['keys'].append("2021-11-1")
            histories['liquid_money'].append(20000)
            histories['stock_money'].append(0)
            histories['score'].append(20000)

            histories['keys'].reverse()
            histories['liquid_money'].reverse()
            histories['stock_money'].reverse()
            histories['score'].reverse()

            user.histories = histories
        else:
            user.histories = None

        return user.to_dict()

    except Exception as e:
        raise
        return str(e), 400