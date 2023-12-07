import matplotlib.pyplot as plt
import mplcursors
import random

# Function to create a histogram
def create_histogram(data, title, xlabel, ylabel='Visitors', hide_xticks=False, color='blue'):
    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(12, 10))
    # Create bars
    colors = [(random.random(), random.random(), random.random()) for _ in range(len(data))]
    bars = ax.bar(data.keys(), data.values(), color=colors, width = 1, edgecolor='black')
    # Add title and labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # Remove xticks
    if hide_xticks:
        ax.set_xticks([])
        # Add annotations
        cursor = mplcursors.cursor(bars, hover=True)
        # Add annotation to each bar
        cursor.connect("add", lambda sel: sel.annotation.set_text(f'Browser: {list(data.keys())[sel.target.index]}'))
    plt.show()




