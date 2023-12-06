
import matplotlib.pyplot as plt

# Function to create a histogram
def create_histogram(x, y, title, xlabel, ylabel='Visitors', color='blue'):
    # Create a figure
    plt.figure(figsize=(10, 8))
    # Create a bar plot
    plt.bar(x, y, color=color, edgecolor='black')
    # Add a title and axis labels
    plt.title(title)
    # Print x label
    plt.xlabel(xlabel)
    # Print y label
    plt.ylabel(ylabel)
    # Rotate xticks
    plt.xticks(rotation=90)
    # Show the plot
    plt.show()



