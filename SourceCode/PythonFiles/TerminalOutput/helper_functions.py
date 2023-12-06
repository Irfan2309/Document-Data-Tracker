
import matplotlib.pyplot as plt

# Function to create a histogram
def create_histogram(data, title, xlabel, ylabel='Number of Views', color='darkblue'):
    # Create a figure
    plt.figure(figsize=(10, 6))
    # Create a bar plot
    plt.bar(data.keys(), data.values(), color=color)
    # Add a title and axis labels
    plt.title(title)
    # Print x label
    plt.xlabel(xlabel)
    # Print y label
    plt.ylabel(ylabel)
    # Show the plot
    plt.show()

