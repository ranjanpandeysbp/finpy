import pandas as pd
import yfinance as yf
import datetime as dt

#https://www.linkedin.com/pulse/using-python-yahoo-finance-api-analyze-stock-market-neven-dujmovic
#https://algotrading101.com/learn/yfinance-guide/#:~:text=interval%3A%20data%20interval%20(1m%20data,%E2%80%9C1mo%E2%80%9D%2C%20%E2%80%9C3mo%E2%80%9D

with open('datasets/symbols_crypto.csv') as f:
    for line in f:
        if "," not in line:
            continue
        symbol = line.split(",")[0]
        data = yf.download(symbol, start="2023-09-02", end=dt.datetime.now(), interval="5m")
        data.to_csv('datasets/three_minute/{}.csv'.format(symbol))
