
import matplotlib.pyplot as plt
from collections import Counter
import pycountry_convert as pc
import pandas as pd
from datetime import datetime

# Function to plot countries for each document
def plot_countries(data):
    filtered_data = []
    # For every record in data
    for entry in data:
        # If visitor_country is present
        if 'visitor_country' in entry:
            # Convert country code to full name
            try:
                country_name = pc.country_alpha2_to_country_name(entry['visitor_country'])
            except:
                country_name = 'Unknown'
            # Append to filtered_data
            filtered_data.append(country_name)
            
    # Count occurrences of each country code
    country_count = Counter(filtered_data)
    # Return country_count
    return country_count

# Plot for hourly visitors
def plot_hourly_visitors(data):
    # ts is the data in epoch
    ts = [entry['ts'] for entry in data]
    # Convert to datetime
    ts = [datetime.fromtimestamp(t) for t in ts]
    # Convert to string
    ts = [t.strftime('%H') for t in ts]
    # Count occurrences of each date
    hourly_visitors = Counter(ts)
    return hourly_visitors

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

