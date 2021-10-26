from pandas._libs.tslibs.timestamps import Timestamp
from models import Transaction, Stock
import yfinance as yf

def get_stock(stock_id: str) -> Stock:
    try:
        ticker = yf.Ticker(stock_id)
        stock = Stock()

        stock.id = stock_id
        stock.value = ticker.history().tail(1)['Close'].iloc[0]
        stock.name = ticker.info['longName']

        before = ticker.history(period='2d', interval='1d').tail(2)['Close'].iloc[0]
        now = ticker.history(period='2d', interval='1d').tail(1)['Close'].iloc[0]
        stock.change = (now / before - 1) * 100

        return stock
    except:
        raise Exception(f"Sorry dude, couldn't get you the stock {stock_id}")


def get_stock_with_history(stock_id: str) -> Stock:
    stock = get_stock(stock_id)
    ticker = yf.Ticker(stock_id)
    history = ticker.history(period='5d', interval='5m').to_dict()['Close']
    timestamp_history = {}

    for _, key in enumerate(history):
        timestamp_history[int(key.timestamp())] = history[key]

    stock.history = timestamp_history

    return stock


def apply_transactions(history: dict, transactions: list[Transaction], current_value: float):
    pass


if __name__ == '__main__':
    print(get_stock_with_history('AAPL').to_json())
    time = Timestamp('2021-10-21 10:40:00-0400', tz='America/New_York')
    print(time.timestamp())