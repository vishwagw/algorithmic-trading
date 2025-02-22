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
# function to check the signals for buying:
def check_buy_sell_signals(data):
    if data['short_mavg'].iloc[-1] > data['long_mavg'].iloc[-1] and \
       data['short_mavg'].iloc[-2] <= data['long_mavg'].iloc[-2]:
        return 'buy'
    elif data['short_mavg'].iloc[-1] < data['long_mavg'].iloc[-1] and \
         data['short_mavg'].iloc[-2] >= data['long_mavg'].iloc[-2]:
        return 'sell'
    else:
        return 'hold'
    
# function to self execute a trade
def exeute_trade(action, symbol, quantity):
    if action == 'buy':
        api.submit_order(
            symbol=symbol,
            qty=quantity,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        print(f"Bought {quantity} shares of {symbol}")
    elif action == 'sell':
        api.submit_order(
            symbol=symbol,
            qty=quantity,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        print(f"Sold {quantity} shares of {symbol}")

# main execution function:
def main():
    while True:
        e True:
        data = get_moving_averages(symbol, short_window, long_window)
        action = check_buy_sell_signals(data)
        execute_trade(action, symbol, quantity)
        time.sleep(86400)  # Run once per day

# proegram execution:
if __name__ == "__main__":
     main()



