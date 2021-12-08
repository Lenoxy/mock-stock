import math
from threading import current_thread
from flask import Blueprint
from flask_login import login_required, current_user
import finance
import db
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
