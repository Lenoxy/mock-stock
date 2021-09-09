import yfinance as yf
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    aapl = yf.Ticker("AAPL")

    return str(aapl.history().tail(1)['Close'].iloc[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
