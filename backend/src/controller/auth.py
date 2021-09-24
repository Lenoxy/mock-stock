from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/auth/register", methods=['POST'])
def register_user():
    andsomedbcalls = "not implemented as well"

    return f'Should create User. Not yet implemented, do it bitch!'

@auth.route("/auth/login", methods=['POST'])
def login_user(loginRequest):
    andsomedbcalls = "not implemented as well"

    return f'Should return a cookie. You dont get any cookies because noone implemented this!'

@auth.route("/auth/logout")
# @login_required
def logout_user():
    andsomedbcalls = "not implemented as well"

    return f'Why tho, coulnt we just delete the cookie in the frontend?'