import matplotlib.pyplot as plt
import pandas as pd


# function to be called in the main file to put together the boxplot
def create_boxplot(bank_data):
    # set size of matplotlib canvas
    plt.figure(figsize=(18, 12))  # may or may not be needed

    # create a boxplot along columns, not rows; transpose DataFrame
    plt.boxplot(bank_data.transpose)

    # styling of title and axis
    plt.title('Boxplot of Bank Stock Prices (5Y Lookback)', fontsize=20)  # chart title
    plt.xlabel('Bank', fontsize=20)  # x axis
    plt.ylabel('Stock Prices', fontsize=20)  # y axis

    # add column-specific labels to x-axis for each bank
    ticks = range(1, len(bank_data.columns) + 1)  # establish spacing
    labels = list(bank_data.columns)  # fetch the bank names
    plt.xticks(ticks, labels, fontsize=20)  # set x labels


# creates scatterplot of given bank
def create_scatterplot(bank_data, bank):
    # create x-axis variable and format labels to datetime data type
    dates = bank_data.index.to_series()
    dates = [pd.to_datetime(d) for d in dates]

    # isolate stock prices of the specified bank
    bank_stock_prices = bank_data[bank]

    # generate the scatterplot
    plt.scatter(dates, bank_stock_prices)

    # add titles and axis
    plt.title(f"{bank} Stock Price (5Y Lookback)", fontsize=20)
    plt.ylabel("Stock Price", fontsize=20)
    plt.xlabel("Date", fontsize=20)


# creates histogram from bank_data
def create_histogram(bank_data):



