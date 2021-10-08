class User():
    def __init__(self, user):
        if user['username'] and user['password_hash'] and user['money_liquid']:
            self.username = user['username']
            self.password_hash = user['password_hash']
            self.money_liquid = user['money_liquid']

    def to_json(self):
        return {"username": self.username,
                "money_liquid": self.money_liquid}

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)