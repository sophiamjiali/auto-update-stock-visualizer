import matplotlib.pyplot as plt
import pandas as pd

# final variables
BOXPLOT_X = 18
BOXPLOT_Y = 12
BIN_COUNT = 50  # for histogram
FONT_SIZE = 20


# called by each function to set up the matplotlib canvas
def set_canvas_size():
    # set size of matplotlib canvas
    plt.figure(figsize=(BOXPLOT_X, BOXPLOT_Y))


# function to be called in the main file to put together the boxplot
def create_boxplot(bank_data):
    # call the set_canvas_size helper function
    # set_canvas_size() -> called by subplot function, necessary?

    # create a boxplot along columns, not rows; transpose DataFrame
    plt.boxplot(bank_data.transpose())

    # styling of title and axis
    plt.title('Boxplot of Bank Stock Prices (5Y Lookback)', fontsize=FONT_SIZE)  # chart title
    plt.xlabel('Bank', fontsize=FONT_SIZE)  # x axis
    plt.ylabel('Stock Prices', fontsize=FONT_SIZE)  # y axis

    # add column-specific labels to x-axis for each bank
    ticks = range(1, len(bank_data.columns) + 1)  # establish spacing
    labels = list(bank_data.columns)  # fetch the bank names
    plt.xticks(ticks, labels, fontsize=FONT_SIZE)  # set x labels


# creates scatterplot of given bank
def create_scatterplot(bank_data, bank):
    # call the set_canvas_size helper function
    # set_canvas_size() -> called by subplot function, necessary?

    # create x-axis variable and format labels to datetime data type
    dates = bank_data.index.to_series()
    dates = [pd.to_datetime(d) for d in dates]

    # isolate stock prices of the specified bank
    bank_stock_prices = bank_data[bank]

    # generate the scatterplot
    plt.scatter(dates, bank_stock_prices)

    # add titles and axis
    plt.title(f"{bank} Stock Price (5Y Lookback)", fontsize=FONT_SIZE)
    plt.ylabel("Stock Price", fontsize=FONT_SIZE)
    plt.xlabel("Date", fontsize=FONT_SIZE)


# creates histogram from bank_data
def create_histogram(bank_data):
    # call the set_canvas_size helper function
    # set_canvas_size() -> called by subplot function, necessary?

    # create the histogram, change bin count
    plt.hist(bank_data.transpose(), bins=BIN_COUNT)

    # add legend for colours of histogram
    plt.legend(bank_data.columns, fontsize=FONT_SIZE)

    # format labels and axis
    plt.title("A Histogram of Daily Closing Stock Prices for the 5 Largest Banks in the US *5Y Lookback)", fontsize=FONT_SIZE)
    plt.ylabel("Observations", fontsize=FONT_SIZE)
    plt.xlabel("Stock Prices", fontsize=FONT_SIZE)


# creates a subplot using the three previous plot types
def create_subplots(bank_data, bank1, bank2):
    # create subplot grid
    plt.subplot(2, 2, 1)
    create_boxplot(bank_data)

    plt.subplot(2, 2, 2)  # scatterplot for first bank
    create_scatterplot(bank_data, bank1)

    plt.subplot(2, 2, 3)  # scatterplot for second bank
    create_scatterplot(bank_data, bank2)

    plt.subplot(2, 2, 4)
    create_histogram(bank_data)

    # save data visualizations as a png file
    plt.savefig('bank_data.png')
