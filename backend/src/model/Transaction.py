class Transaction():
    def __init__(self, transaction):
        if transaction['id'] and transaction['username'] and transaction['date'] and transaction['stock_id'] and transaction['amount']:
            self.id = transaction['id']
            self.username = transaction['username']
            self.date = transaction['date']
            self.stock_id = transaction['stock_id']
            self.amount = transaction['amount']

    def to_json(self):
        return {'id': self.id,
                'username': self.username,
                'date': self.date,
                'stock_id': self.stock_id,
                'amount': self.amount}
