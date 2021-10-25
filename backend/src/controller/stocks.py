from flask_login import login_required, current_user
from flask import Blueprint, request, jsonify
from flask_login.mixins import AnonymousUserMixin
import yfinance as yf
import finance
import db
from models import OwnedStock

stocks = Blueprint('stocks', __name__)


@stocks.route("/stocks")
def get_stocks():
    return 'AAPL GOOG etc...'


@stocks.route("/stocks/<string:id>")
def get_stock(id):
    try:
        stock = finance.get_stock_with_history(id)
        if not current_user is AnonymousUserMixin:
            owned_stocks = db.get_owned_stocks(current_user.username)
            if id in owned_stocks:
                stock.amount = owned_stocks[id].amount

        return stock.to_json()

    except Exception as e:
        # return str(e), 400
        raise


@stocks.route("/stocks/<string:id>/buy", methods=['PUT'])
@login_required
def buy_stock(id):
    try:
        amount = request.json['amount']

        db.update_owned_stocks(OwnedStock({'username': current_user.username,'id': id, 'amount': amount }))

        return db.get_owned_stocks(current_user.username)[id].to_json()
    except Exception as e:
        return str(e), 400


@stocks.route("/stocks/<string:id>/sell", methods=['PUT'])
@login_required
def sell_stock(id):
    try:
        amount = -(request.json['amount'])

        db.update_owned_stocks(OwnedStock({'username': current_user.username,'id': id, 'amount': amount }))

        return db.get_owned_stocks(current_user.username)[id].to_json()
    except Exception as e:
        return str(e), 400