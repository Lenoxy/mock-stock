from flask import Blueprint
import db

from models import Transaction, OwnedStock

me = Blueprint('me', __name__)

@me.route("/me")
# @login_required
def get_me():
    # db.create_transaction(Transaction({'id': 1,
    #                                    'username': 'lenoxy',
    #                                    'date': 1,
    #                                    'stock_id': "5",
    #                                    'amount': 7}))

    #db.get_transactions("lenoxy")

    db.update_owned_stock(OwnedStock({'username': 'lenoxy',
                           'id': 'APPL',
                           'amount': -9}))


    return f'Should return me. Not yet implemented, do it bitch!'

@me.route("/me/stocks")
# @login_required
def get_my_stocks():
    return f'Should return my stocks. Not yet implemented, do it bitch!'
