from data_collection import *
from visualizer import *

# from data_collection.py; set up data to be visualized

# serialize the ticker list into a string
tickers = serialize_ticker_list()
# format the http request
HTTP_request = select_endpoint(tickers)
# fetch bank data
bank_data = pd.read_json(HTTP_request)
# pull closing prices
price_series = pull_price_time_series(tickers, bank_data)
# format bank_data and fetch stock data
stock_data = fetch_bank_stock_data(bank_data)

# from visualizer.py; visualize collected data
