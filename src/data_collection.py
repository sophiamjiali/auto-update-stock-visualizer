import pandas as pd

# Final variables
IEX_API_KEY = "pk_54a6961a936642eda3fc48fa3e50761c"  # IEX Cloud API Token - Publishable
TICKERS = ['JPM', 'BAC', 'C', 'WFC', 'GS']
YEARS = 10
ENDPOINT = 'chart'


# serialize ticker list into a separated string of tickers
def serialize_ticker_list():
    ticker_string = ''
    for ticker in TICKERS:  # loop through each element and add
        ticker_string += (ticker + ',')
    return ticker_string[:-1]  # drop last added comma


# selects an endpoint from the IEX Cloud API to ping
def select_endpoint(tickers):
    return f'https://cloud.iexapis.com/stable/stock/market/batch?symbols={tickers}&types={ENDPOINT}&range={YEARS}y&token={IEX_API_KEY}'


# pull closing price time series for each stock
def pull_price_time_series(tickers, bank_data):
    bank_price_series = {}  # initialize the dictionary
    for ticker in tickers:
        bank_price_series.update({ticker: pd.DataFrame(bank_data[ticker][ENDPOINT])['close']})
    return bank_price_series


# formats DataFrame with date as index and closing price as column
def fetch_bank_stock_data(bank_data):
    stock_data = []  # initialize the list
    for ticker in TICKERS:
        stock_data.append(pd.DataFrame(bank_data[ticker][ENDPOINT])['close'])
    # add the first bank of TICKERS
    stock_data.append(pd.DataFrame(bank_data[TICKERS[0]][ENDPOINT])['date'])
    # format columns, names, and data
    column_names = TICKERS.copy()
    column_names.append('Date')
    # mutate bank_data
    bank_data = pd.concat(stock_data, axis=1)
    bank_data.columns = column_names
    bank_data.set_index('Date', inplace=True)
    # return the formatted DataFrame; bank_data is mutated in-place
    return stock_data
