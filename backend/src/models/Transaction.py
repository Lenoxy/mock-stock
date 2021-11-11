class Transaction():
    def __init__(self, transaction=None):
        if transaction and transaction['username'] and transaction['datetime'] and transaction['stock_id'] and transaction['amount']:
            self.username = transaction['username']
            self.datetime = transaction['datetime']
            self.stock_id = transaction['stock_id']
            self.amount = transaction['amount']

    def to_dict(self):
        return {'username': self.username,
                'datetime': self.datetime,
                'stock_id': self.stock_id,
                'amount': self.amount}
