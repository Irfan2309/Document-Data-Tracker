
import matplotlib.pyplot as plt
from collections import Counter
import pycountry_convert as pc

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

# Function to plot countries for each document
def plot_countries(data):
    filtered_data = [entry['visitor_country'] for entry in data if 'visitor_country' in entry]
    # Count occurrences of each country code
    country_count = Counter(filtered_data)
    return country_count
