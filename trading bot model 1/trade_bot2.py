# tradng bot sample version 2:
import pandas as pd

# function:
# moving the average strategy:
def move_avrg_crossover_strategy(data, short_window, long_window):
    # compute short-term moving average:
    data['short_ma'] = data['close'].rolling(window=short_window).mean()

    # compute long_term moving average:
    data['long_ma'] = data['close'].rolling(window=long_window).mean()

    # generate buy or sell signals:
    data ['signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1
    data.loc[data['short_ma'] < data['long_ma'], 'signal'] = -1

    return data

# example usage:
price_data = pd.read_csv('./')
strategy_data = move_avrg_crossover_strategy(price_data, 50, 200)
print(strategy_data)
