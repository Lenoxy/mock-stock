import yfinance as yf
from models import Transaction, Stock
import math
import db


stock_dict = db.get_stock_ids()
tickers = {}


def get_stock(stock_id: str) -> Stock:
    try:
        ticker = {}
        if stock_id in tickers:
            ticker = tickers[stock_id]
        else:
            tickers[stock_id] = yf.Ticker(stock_id)
            ticker = tickers[stock_id]
        stock = Stock()

        stock.id = stock_id
        history_for_value = ticker.history(period='2d', interval='1d')
        stock.value = history_for_value.tail(1)['Close'].iloc[0]
        stock.name = ticker.info['longName']

        change_values = ticker.history(period='2d', interval='1d')
        before = change_values.tail(2)['Close'].iloc[0]
        now = change_values.tail(1)['Close'].iloc[0]
        stock.change = (now / before - 1) * 100

        return stock
    except:
        raise Exception(f"Sorry dude, couldn't get you the stock {stock_id}")


def get_stocks(stock_ids: list[str]) -> list[Stock]:
    try:
        if len(stock_ids) == 1:
            return [get_stock(stock_ids[0])]

        data = yf.download( tickers=stock_ids, period="2d", interval="1d")['Close']

        stocks = []

        for stock_data in data.items():
            stock = Stock()
            stock.id = stock_data[0]
            stock.value = stock_data[1].iloc[1]

            if stock_data[0] in stock_dict:
                stock.name = stock_dict[stock_data[0]]
            else:
                # Fallback
                stock_dict[stock_data[0]] = yf.Ticker(stock_data[0]).info['longName']
                stock.name = stock_dict[stock_data[0]]

            before = stock_data[1].iloc[0]
            now = stock_data[1].iloc[1]
            stock.change = (now / before - 1) * 100
            stocks.append(stock)

        return stocks
    except:
        raise Exception(f"Sorry dude, couldn't get you the stocks")


def get_stock_with_history(stock_id: str) -> Stock:
    stock = get_stock(stock_id)
    ticker = yf.Ticker(stock_id)
    history = ticker.history(period='5d', interval='5m').to_dict()['Close']
    timestamp_history = {}

    for _, key in enumerate(history):
        timestamp_history[str(key.isoformat())] = history[key]

    stock.history = timestamp_history

    return stock


def get_stock_value(stock_id: str):
    data = yf.download( tickers=stock_id, period="1d", interval="1d")['Close']
    return data[0]


def get_stock_values(stock_ids: list) -> dict[float]:

    if len(stock_ids) == 1:
        return {stock_ids[0]: get_stock_value(stock_ids[0])}

    data = yf.download( tickers=stock_ids, period="1d", interval="1d")['Close']
    return {stock_data[0].upper(): stock_data[1].iloc[0] for stock_data in data.items()}


def apply_transactions(history: dict[float], transactions: list[Transaction], amount_now: float = 0) -> dict[float]:

    transactions.sort(key=lambda t: t.datetime, reverse=True)
    history = sorted(history, key=lambda h: h, reverse=True)

    res_dict: dict[float] = {}

    i = 0
    for time_stamp in history:
        if time_stamp > transactions[i]:
            res_dict[time_stamp] = history[time_stamp] * amount_now
        else:
            amount_now = amount_now - transactions[i].amount
            res_dict[time_stamp] = history[time_stamp] * amount_now
            i += 1

    return res_dict


def isNaN(num):
    return math.isnan(num)


if __name__ == '__main__':
    print(apply_transactions({}))

