from flask import Flask
import yfinance as yf



app = Flask(__name__)

@app.route("/")
def hello():

    aapl = yf.Ticker("AAPL")

    return str(aapl.history().tail(1)['Close'].iloc[0])