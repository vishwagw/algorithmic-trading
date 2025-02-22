# import libs;
import pandas as pd
import time
# trad api:
import aplaca_trade_api as tradeapi

# Alpaca API credentials
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
BASE_URL = 'https://paper-api.alpaca.markets'

# intialize the apaca api:
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# define trading parameters:
symbol = 'AAPL'
short_window = 40
long_window = 100
quantity = 10

# function to getting moving average:
def get_moving_averages(symbol, short_window, long_window):
     # Retrieve historical market data
    barset = api.get_barset(symbol, 'day', limit=long_window)
    bars = barset[symbol]

    # Create a DataFrame
    data = pd.DataFrame({
        'close': [bar.c for bar in bars]
    })

    # Calculate moving averages
    data['short_mavg'] = data['close'].rolling(window=short_window).mean()
    data['long_mavg'] = data['close'].rolling(window=long_window).mean()

    return data

