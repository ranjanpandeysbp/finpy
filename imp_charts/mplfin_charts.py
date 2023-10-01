#https://www.youtube.com/watch?v=v88IDnpHd-o

import yfinance as yf
import pandas as pd
import mplfinance as mpf

stock = 'SBIN'
filename = stock.lower()+'_mpl_chart'+'.png'
data_sbi = yf.download(stock+'.NS',period='12mo')
#mpf.plot(data_sbi)
mpf.plot(data_sbi, style='yahoo', type='candle', figsize=(15,5), volume=True, mav=(21,50,200),savefig=filename)
#mpf.plot(data_sbi, style='yahoo', type='renko', figsize=(15,5), volume=True, mav=(21,50,200),savefig=filename)
#https://pypi.org/project/mplfinance/