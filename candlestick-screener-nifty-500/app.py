import os, csv
import talib
import yfinance as yf
import pandas
from flask import Flask, request, render_template
from patterns import candlestick_patterns
import datetime as dt

app = Flask(__name__)

@app.route('/snapshot')
def snapshot():
    with open('datasets/symbols_NIFTY50.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start="2023-08-01", end=dt.date.today())
            data.to_csv('datasets/daily_nifty/{}.csv'.format(symbol))

    return {
        "code": "success"
    }

@app.route('/')
def index():
    pattern  = request.args.get('pattern', False)
    stocks = {}

    with open('datasets/symbols_NIFTY50.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}

    if pattern:
        for filename in os.listdir('datasets/daily_nifty'):
            df = pandas.read_csv('datasets/daily_nifty/{}'.format(filename))
            pattern_function = getattr(talib, pattern)
            symbol_arr = filename.split('.')
            symbol = symbol_arr[0]+'.'+symbol_arr[1]
            #print(symbol)

            try:
                results = pattern_function(df['Open'], df['High'], df['Low'], df['Close'])
                last = results.tail(1).values[0]
                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'
                else:
                    stocks[symbol][pattern] = None
            except Exception as e:
                print('failed on filename: ', filename)

    return render_template('index.html', candlestick_patterns=candlestick_patterns, stocks=stocks, pattern=pattern)

if __name__ == '__main__':
    app.run(port=9950)
