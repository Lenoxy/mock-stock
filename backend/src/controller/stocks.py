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

        if current_user.is_authenticated:
            owned_stocks = db.get_owned_stocks(current_user.username)
            for stock in stocks:
                if stock.id in owned_stocks:
                    stock.amount = owned_stocks[stock.id].amount

        return jsonify([stock.to_dict() for stock in stocks])
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

        db.update_owned_stock(OwnedStock({'username': current_user.username, 'id': id, 'amount': amount}))
        current_user.money_liquid -= amount * current_value

        db.update_money_liquid(current_user)
        return f'{amount} {id} stocks'
    except Exception as e:
        return str(e), 400