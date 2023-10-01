import pandas as pd
import yfinance as yf
import datetime as dt

#https://algotrading101.com/learn/yfinance-guide/#:~:text=interval%3A%20data%20interval%20(1m%20data,%E2%80%9C1mo%E2%80%9D%2C%20%E2%80%9C3mo%E2%80%9D
tables = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_500')
symbol_df = tables[2]

def fetch_symbol_data(symbol):
    data = yf.download(symbol, start="2023-09-01", end=dt.date.today(), interval = "1d")
    data.to_csv('datasets/onPtFive_hr_nifty500/{}.csv'.format(symbol))

for s in symbol_df[3]:
    try:
        fetch_symbol_data(s+'.NS')
    except:
        pass