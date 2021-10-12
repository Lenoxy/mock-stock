from os import O_NDELAY


class OwnedStock():
    def __init__(self, owned_stock=None):
        if owned_stock['username'] and owned_stock['id'] and owned_stock['amount']:
            self.username = owned_stock['username']
            self.id = owned_stock['id']
            self.amount = owned_stock['amount']

    def to_json(self):
        return {'username': self.username,
                'id': self.id,
                'amount': self.amount}