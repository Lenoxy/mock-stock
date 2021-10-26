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

            for i in range(skip, top + skip):
                try:
                    stocks.append(finance.get_stock(stock_ids[i]).to_json())
                except Exception as e:
                    print(stock_ids[i])
                

        else:
            for id in db.get_stock_ids():
                try:
                    stocks.append(finance.get_stock(id).to_json())
                except Exception as e:
                    print(id)


        return jsonify(stocks)
    except Exception as e:
        raise
        return str(e), 400


@stocks.route("/stocks/<string:id>", methods=['GET'])
def get_stock(id):
    try:
        stock = finance.get_stock_with_history(id)
        if current_user.is_authenticated:
            owned_stocks = db.get_owned_stocks(current_user.username)
            if id in owned_stocks:
                stock.amount = owned_stocks[id].amount

        return stock.to_json()

    except Exception as e:
        raise
        return str(e), 400


@stocks.route("/stocks/<string:id>", methods=['PUT'])
@login_required
def buy_stock(id):
    try:
        amount = request.json['amount']

        db.update_owned_stocks(OwnedStock({'username': current_user.username,'id': id, 'amount': amount }))

        return db.get_owned_stocks(current_user.username)[id].to_json()
    except Exception as e:
        return str(e), 400