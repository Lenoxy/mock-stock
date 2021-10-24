from os import O_NDELAY

from yfinance import Ticker


class StockDetails():
    def __init__(self, owned_stock=None):
        if owned_stock['id'] and owned_stock['value'] and owned_stock['name'] and owned_stock['amount'] and owned_stock['valueHistory']:
            self.id = owned_stock['id']
            self.value = owned_stock['value']
            self.name = owned_stock['name']
            self.amount = owned_stock['amount']
            self.valueHistory = owned_stock['valueHistory']

    @classmethod
    def from_ticker(cls, ticker: Ticker, amount):
        stock = dict.fromkeys(
            ['id', 'value', 'name','amount', 'valueHistory'],
            [ticker.info.get('symbol'), ticker.info.get('currentPrice'), ticker.info.get('shortName'), amount, ticker.history("1mo", "1d")])

        return cls(stock)
