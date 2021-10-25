import flask_login
from flask import Blueprint, request, jsonify
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
        return finance.get_stock_with_history(id).to_json()
    except Exception as e:
        return str(e), 400



@stocks.route("/stocks/<string:id>/buy", methods=['PUT'])
# @login_required
def buy_stock(id):
    amount = request.json['amount']

    db.update_owned_stocks(OwnedStock({'username': flask_login.current_user.username,'id': id, 'amount': amount }))

    return db.get_owned_stocks(flask_login.current_user.username)[id].to_json()


@stocks.route("/stocks/<string:id>/sell", methods=['PUT'])
# @login_required
def sell_stock(id):
    amount = -(request.json['amount'])

    db.update_owned_stocks(OwnedStock({'username': flask_login.current_user.username,'id': id, 'amount': amount }))

    return db.get_owned_stocks(flask_login.current_user.username)[id].to_json()
