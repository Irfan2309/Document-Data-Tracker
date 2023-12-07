
import matplotlib.pyplot as plt
from collections import Counter
import pycountry_convert as pc
import pandas as pd
from datetime import datetime


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

# Function to plot count of usrrs on daily basis
def plot_daily_visitors(data):
    # ts is the data in epoch
    ts = [entry['ts'] for entry in data]
    # Convert to datetime
    ts = [datetime.fromtimestamp(t) for t in ts]
    # Convert to string
    ts = [t.strftime('%Y-%m-%d') for t in ts]
    # Count occurrences of each date
    daily_visitors = Counter(ts)
    return daily_visitors

# Function to plot count of users on monthly basis
def plot_monthly_visitors(data):
    # ts is the data in epoch
    ts = [entry['ts'] for entry in data]
    # Convert to datetime
    ts = [datetime.fromtimestamp(t) for t in ts]
    # Convert to string
    ts = [t.strftime('%Y-%m') for t in ts]
    # Count occurrences of each date
    monthly_visitors = Counter(ts)
    return monthly_visitors

# Function to plot count of users on yearly basis
def plot_yearly_visitors(data):
    # ts is the data in epoch
    ts = [entry['ts'] for entry in data]
    # Convert to datetime
    ts = [datetime.fromtimestamp(t) for t in ts]
    # Convert to string
    ts = [t.strftime('%Y') for t in ts]
    # Count occurrences of each date
    yearly_visitors = Counter(ts)
    return yearly_visitors

