from data_collection import *
from visualizer import *
import requests

# from data_collection.py; set up data to be visualized

# serialize the ticker list into a string
tickers = serialize_ticker_list()

# format the http request
HTTP_request = select_endpoint(tickers)

# fetch bank data
response = requests.get(HTTP_request, verify=False).json()
bank_data = pd.DataFrame(response)

# pull closing prices
price_series = pull_price_time_series(TICKERS, bank_data)

# format bank_data and fetch stock data
stock_data = fetch_bank_stock_data(bank_data)


# from visualizer.py; visualize collected data

# generate boxplot
create_boxplot(bank_data)
# generate scatterplot
