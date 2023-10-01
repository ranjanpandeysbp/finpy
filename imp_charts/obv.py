#https://www.youtube.com/watch?v=lkng10n9q9Q

import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import numpy as np

data_sbi = yf.download('SBIN.NS', period='5y')
data_sbi['Daily Returns'] = data_sbi['Adj Close'].pct_change()

data_sbi['Volume Status'] = 0
#below returns the rows where daily returns is greater than 0, we also want the Volume Status to be set to 1 at those rows
data_sbi.loc[data_sbi['Daily Returns'] > 0, 'Volume Status'] = 1
data_sbi.loc[data_sbi['Daily Returns'] < 0, 'Volume Status'] = -1

data_sbi.dropna(inplace=True)

data_sbi['Effective Volume'] = data_sbi['Volume Status'] * data_sbi['Volume']
#on_balance_volume = OBV
data_sbi['OBV'] = data_sbi['Effective Volume'].cumsum()

data_sbi[['OBV']].plot(figsize=(15,3))
data_sbi[['Adj Close']].plot(figsize=(15,3))
plt.show()
