class User():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    def to_json(self):
        return {"username": self.username,
                "email": self.email}
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.username)