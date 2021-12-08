import json

from flask.json import JSONEncoder
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user=None):
        if user and user['username'] and user['password_hash'] and user['money_liquid']:
            self.username = user['username']
            self.password_hash = user['password_hash']
            self.money_liquid = user['money_liquid']

        self.money_in_stocks: float = 0
        self.stocks = []
        self.is_authenticated = True
        self.histories = None

    def to_dict(self):
        return {"username": self.username,
                "money_liquid": self.money_liquid,
                "money_in_stocks": self.money_in_stocks,
                "score": self.money_liquid + self.money_in_stocks,
                "stocks": self.stocks,
                "histories": self.histories}

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)
