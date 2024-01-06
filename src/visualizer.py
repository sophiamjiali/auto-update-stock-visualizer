import matplotlib.pyplot as plt


# function to be called in the main file to put together the boxplot
def create_boxplot(bank_data):
    # create a boxplot along columns, not rows; transpose DataFrame
    plt.boxplot(bank_data.transpose)
