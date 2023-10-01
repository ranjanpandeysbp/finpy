import pandas as pd
import yfinance as yf
import datetime as dt

#https://algotrading101.com/learn/yfinance-guide/#:~:text=interval%3A%20data%20interval%20(1m%20data,%E2%80%9C1mo%E2%80%9D%2C%20%E2%80%9C3mo%E2%80%9D
tables = pd.read_html('https://en.wikipedia.org/wiki/NIFTY_500')
symbol_df = tables[2]

symbols_data = symbol_df[3]
symbols_data.to_csv('datasets/symbols_nifty500.csv')