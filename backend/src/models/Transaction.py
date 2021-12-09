class Transaction():
    def __init__(self, transaction={}):
        self.username = transaction['username'] if 'username' in transaction else None
        self.datetime = transaction['datetime'] if 'datetime' in transaction else None
        self.stock_id = transaction['stock_id'] if 'stock_id' in transaction else None
        self.amount = transaction['amount'] if 'amount' in transaction else None
        self.stock_price = transaction['stock_price'] if 'stock_price' in transaction else None
        

    def to_dict(self):
        return {'username': self.username,
                'datetime': self.datetime,
                'stock_id': self.stock_id,
                'amount': self.amount,
                'stock_price': self.stock_price}
