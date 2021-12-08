from flask_login import login_required, current_user
from flask import Blueprint, request, jsonify
from models import OwnedStock, Transaction
from datetime import datetime
import finance
import math
import db


stocks = Blueprint('stocks', __name__)


def isNaN(num):
    return math.isnan(num)


@stocks.route("/stocks")
def get_stocks():
    try:
        # Paging start
        skip = request.args.get('skip')
        # Paging end
        top = request.args.get('top')
        local_stocks = []
        if top:
            top = int(top)
            if not skip:
                skip = 0
            else:
                skip = int(skip)

            stock_list = list(db.get_stock_ids())
            local_stocks = finance.get_stocks(stock_list[skip:top + skip])

        else:
            stock_list = list(db.get_stock_ids())
            local_stocks = finance.get_stocks(stock_list)

        if current_user.is_authenticated:
            owned_stocks = db.get_owned_stocks(current_user.username)
            for stock in local_stocks:
                if stock.id in owned_stocks:
                    stock.amount = owned_stocks[stock.id].amount

        serialized_stocks = []

        for stock in local_stocks:
            if isNaN(stock.change):
                stock.change = None

            if isNaN(stock.value):
                stock.value = None

            serialized_stocks.append(stock.to_dict())

        return jsonify(serialized_stocks)

    except Exception as e:
        return str(e), 400


@stocks.route("/stocks/<string:id>", methods=['GET'])
def get_stock(id):
    try:
        id = id.upper()
        stock = finance.get_stock_with_history(id)
        if current_user.is_authenticated:
            owned_stocks = db.get_owned_stocks(current_user.username)
            if id in owned_stocks:
                stock.amount = owned_stocks[id].amount

        return stock.to_dict()

    except Exception as e:
        return str(e), 400


@stocks.route("/stocks/<string:id>", methods=['PUT'])
@login_required
def buy_stock(id):
    try:
        id = id.upper()
        amount = request.json['amount']
        current_value = finance.get_stock_value(id)
        if current_user.money_liquid < amount * current_value:
            raise Exception("You can't afford that xD, you broke af dude...")

        transaction = Transaction()
        transaction.username = current_user.username
        transaction.amount = amount
        transaction.datetime = datetime.now().isoformat()
        transaction.stock_id = id
        transaction.stock_price = current_value

        db.update_owned_stock(OwnedStock({'username': current_user.username, 'id': id, 'amount': amount}))
        db.create_transaction(transaction)
        current_user.money_liquid -= amount * current_value

        db.update_money_liquid(current_user)
        return f'bought/sold {amount} {id} stocks'
    except Exception as e:
        return str(e), 400
