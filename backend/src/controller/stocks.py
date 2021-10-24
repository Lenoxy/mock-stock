from flask import Blueprint, request, jsonify
import yfinance as yf

from backend.src.models.StockDetails import StockDetails

stocks = Blueprint('stocks', __name__)


@stocks.route("/stocks")
def hello():
    return 'AAPL GOOG etc...'


@stocks.route("/stocks/<string:id>")
def get_stock(id):
    stock = yf.Ticker(id)

    return str(stock.history().tail(1)['Close'].iloc[0])


@stocks.route("/stocks/<string:id>/buy", methods=['PUT'])
# @login_required
def buy_stock(id):
    amount = request.data
    stock = yf.Ticker(id)

    # db.update_owned_stocks()

    return jsonify(StockDetails.from_ticker(stock, amount))

    return f'Should buy {id}. Not yet implemented, do it bitch!'


@stocks.route("/stocks/<string:id>/sell", methods=['PUT'])
# @login_required
def sell_stock(id):
    stock = yf.Ticker(id)

    return f'Should sell {id}. Not yet implemented, do it bitch!'
