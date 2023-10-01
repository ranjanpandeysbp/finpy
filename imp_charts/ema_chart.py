import yfinance as yf
import matplotlib.pyplot as plt

#https://www.youtube.com/watch?v=yIQCMbiTLQI&t=302s
data = yf.download('RELIANCE.NS', period='5y')
#print(data.tail())

data['100SMA'] = data['Adj Close'].rolling(100).mean()
data['100EMA'] = data['Adj Close'].ewm(span=100,min_periods=100).mean()
#print(data.tail())

data[['Adj Close', '100SMA', '100EMA']].plot(figsize=(15,5))
#plt.show()
plt.savefig('100EMA_100SMA.png')

