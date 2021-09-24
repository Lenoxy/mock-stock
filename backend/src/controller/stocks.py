from flask import Blueprint
import yfinance as yf

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
    stock = yf.Ticker(id)

    return f'Should buy {id}. Not yet implemented, do it bitch!'

@stocks.route("/stocks/<string:id>/sell", methods=['PUT'])
# @login_required
def sell_stock(id):
    stock = yf.Ticker(id)

    return f'Should sell {id}. Not yet implemented, do it bitch!'