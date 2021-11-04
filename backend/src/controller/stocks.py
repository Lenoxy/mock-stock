from flask_login import login_required, current_user
from flask import Blueprint, request, jsonify
from flask_login.mixins import AnonymousUserMixin
import finance
import db
from models import OwnedStock


stocks = Blueprint('stocks', __name__)


@stocks.route("/stocks")
def get_stocks():
    try:
        top = request.args.get('top')
        skip = request.args.get('skip')
        stocks = []
        if top:
            top = int(top)
            if not skip:
                skip = 0
            else:
                skip = int(skip)

            stock_ids = list(db.get_stock_ids())

            stocks = finance.get_stocks(stock_ids[skip:top+skip])
                

        else:
            stock_ids = list(db.get_stock_ids())
            stocks = finance.get_stocks(stock_ids)


        return jsonify([stock.to_dict() for stock in stocks])
    except Exception as e:
        return str(e), 400


@stocks.route("/stocks/<string:id>", methods=['GET'])
def get_stock(id):
    try:
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
        amount = request.json['amount']

        db.update_owned_stock(OwnedStock({'username': current_user.username, 'id': id, 'amount': amount}))

        return db.get_owned_stocks(current_user.username)[id].to_dict()
    except Exception as e:
        return str(e), 400