
import matplotlib.pyplot as plt
import mplcursors

def create_histogram(data, title, xlabel, ylabel='Visitors', color='darkblue'):
    # Create a figure and bar plot
    fig, ax = plt.subplots(figsize=(12, 10))
    bars = ax.bar(data.keys(), data.values(), color=color)

    # Add a title and axis labels
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Hide the x-ticks
    ax.set_xticks([])

    # Use mplcursors to add interactive hover tooltips to the bars
    cursor = mplcursors.cursor(bars, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f'Browser: {list(data.keys())[sel.target.index]}'))
    # Show the plot
    plt.show()


