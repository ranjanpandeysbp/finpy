import os, pandas

subtotal = 0
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def is_consolidating(df, percentage=2):
    try:
        recent_candlesticks = df[-50:]

        max_close = recent_candlesticks['Close'].max()
        min_close = recent_candlesticks['Close'].min()

        threshold = 1 - (percentage / 100)
        if min_close > (max_close * threshold):
            return True
    except:
        pass
    return False


def is_breaking_out(df, percentage=2.5):
    try:
        last_close = df[-1:]['Close'].values[0]

        if is_consolidating(df[:-1], percentage=percentage):
            recent_closes = df[-51:-1]

            if last_close > recent_closes['Close'].max():
                return True
    except:
        pass
    return False


for filename in os.listdir('datasets/hourly_nifty500'):
    df = pandas.read_csv('datasets/hourly_nifty500/{}'.format(filename))

    if is_consolidating(df, percentage=2.5):
        print("{} is consolidating".format(filename))

    if is_breaking_out(df):
        print(bcolors.WARNING + "{} is breaking out".format(filename) + bcolors.ENDC)