from flask_login import login_required, current_user
from flask import Blueprint
from controller import users


me = Blueprint('me', __name__)


@me.route("/me")
@login_required
def get_me():
    try:
        username = current_user.username
        return users.get_user(username)

    except Exception as e:
        return str(e), 400
