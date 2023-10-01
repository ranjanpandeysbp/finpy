import pandas as pd
import yfinance as yf
import datetime as dt

def fetch():
    # https://algotrading101.com/learn/yfinance-guide/#:~:text=interval%3A%20data%20interval%20(1m%20data,%E2%80%9C1mo%E2%80%9D%2C%20%E2%80%9C3mo%E2%80%9D
    tables = pd.read_html('https://finance.yahoo.com/crypto/?count=0&offset=100')
    # tables = pd.read_html('https://finance.yahoo.com/crypto/?count=300&offset=100')
    symbol_df = tables[0]

    # print(symbol_df[0]['Symbol'])
    def fetch_symbol_data(symbol):
        data = yf.download(symbol, start="2023-09-01", end=dt.datetime.now(), interval="15m")
        data.to_csv('datasets/five_minute/{}.csv'.format(symbol))

    for s in symbol_df['Symbol']:
        try:
            fetch_symbol_data(s)
        except:
            pass