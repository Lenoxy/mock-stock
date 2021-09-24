from flask import Blueprint

me = Blueprint('me', __name__)

@me.route("/me")
# @login_required
def get_me():
    somecookiestuff = "note here"
    andsomedbcalls = "not implemented as well"

    return f'Should return me. Not yet implemented, do it bitch!'

@me.route("/me/stocks")
# @login_required
def get_my_stocks():
    somecookiestuff = "note here"
    andsomedbcalls = "not implemented as well"

    return f'Should return my stocks. Not yet implemented, do it bitch!'
