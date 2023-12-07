import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from card_num import get_unique_visitors_count, get_unique_documents_count, average_reading_time_per_document, total_visits_count
from graph_data import plot_countries
from graph_data import plot_daily_visitors
import json
import mplcursors
from table_data import process_reading_data, process_document_data

def on_frame_configure(event, canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

# Function to create a card-like frame
def create_card(parent, title, value, bg_color):
    frame = tk.Frame(parent, bg=bg_color, bd=1, relief="solid", padx=10, pady=10)
    tk.Label(frame, text=title, bg=bg_color, fg='black', font=("Arial", 16, 'bold')).pack()
    tk.Label(frame, text=value, bg=bg_color, fg='black', font=("Arial", 20, 'bold')).pack()
    return frame

# Function to create a chart frame and plot a Matplotlib chart
def create_matplotlib_chart(parent, title, x, y):
    # Create a container frame for each chart and title
    container = tk.Frame(parent)
    container.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    # Create a label for the chart's title
    label = tk.Label(container, text=title, fg='white', font=("Arial", 16, "bold"), padx=5, pady=5)
    label.pack(fill="x")

    # Create a figure for the plot
    fig = Figure(figsize=(4, 4), dpi=100)
    plot = fig.add_subplot(111)

    # Plot the data
    plot.bar(x, y)

    #hide the x-ticks
    plot.set_xticks([])

     # Use mplcursors to add interactive hover tooltips to the bars
    cursor = mplcursors.cursor(plot, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(list(x)[sel.target.index]))

    # Create the canvas and add it to the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# Function to create the top cards
def all_cards(parent,data):
    top_frame = tk.Frame(parent)
    top_frame.pack(fill="x", pady=10)

    # Get the data for the cards
    unique_visitors = get_unique_visitors_count(data)
    unique_documents = get_unique_documents_count(data)
    average_time = average_reading_time_per_document(data)
    total_visits = total_visits_count(data)

    # Create the cards
    card1 = create_card(top_frame, "Unique Visitors", "{:,}".format(unique_visitors), "lightblue")
    card1.pack(side="left", fill="both", expand=True, padx=5)

    card2 = create_card(top_frame, "Unique Documents", "{:,}".format(unique_documents), "lightgreen")
    card2.pack(side="left", fill="both", expand=True, padx=5)

    card3 = create_card(top_frame, "Average Reading Time", str(average_time)+" Secs", "lightcoral")
    card3.pack(side="left", fill="both", expand=True, padx=5)

    card4 = create_card(top_frame, "Total Visits", "{:,}".format(total_visits), "lightgrey")
    card4.pack(side="left", fill="both", expand=True, padx=5)


def all_charts(parent, data):
    # Heading for the charts
    heading_label = tk.Label(scrollable_frame, text="Graph Analysis", font=("Arial", 20, "bold", "italic"), fg="white")
    heading_label.pack(fill="x", pady=5)

    # Generate some random data for the charts
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    middle_frame = tk.Frame(parent)
    middle_frame.pack(fill="x", pady=10)

    # Create the charts
    counter = plot_countries(data)
    create_matplotlib_chart(middle_frame, "Chart 1", counter.keys(), counter.values())

    daily_visitors = plot_daily_visitors(data)
    create_matplotlib_chart(middle_frame, "Chart 2", daily_visitors.keys(), daily_visitors.values())

    # create_matplotlib_chart(middle_frame, "Chart 2", x, y)

# Function to create a table with three columns
def create_table(parent, title, column_names, content):
    table_frame = tk.Frame(parent)
    tk.Label(table_frame, text=title, font=("Arial", 14)).pack()
    
    tree = ttk.Treeview(table_frame, columns=column_names, show='headings')
    for col in column_names:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")
    
    # Print content
    for item in content[:20]:
        tree.insert('', 'end', values=item)
    tree.pack(expand=True, fill='both')
    return table_frame

# Function to place two tables side by side
def place_tables(parent,data):
    # Left table
    result = process_reading_data(data)
    table1 = create_table(parent, "Top Readers", ('User ID', 'Documents Read', 'Average Time Spent (secs)'), result)
    table1.pack(side="left", expand=True, fill="both", padx=(0, 5), pady=5)
    
    result2 = process_document_data(data)
    # Right table
    table2 = create_table(parent, "Top Readers", ('Document ID', 'Users Read', 'Average Time Spent'), result2)
    table2.pack(side="left", expand=True, fill="both", padx=(0, 5), pady=5)



def full_gui():
    # Initialize main window for the dashboard
    root = tk.Tk()
    root.title("Admin Panel Dashboard")
    root.geometry("1230x800")
    root.configure(bg="black")

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(root, bg="black")
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

    # Configure the canvas
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the scrollbar to the right side, fill Y axis. Pack the canvas to fill the rest
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Add a frame inside the canvas
    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    scrollable_frame.bind("<Configure>", on_frame_configure(canvas=canvas))
    data = []
    try:
        with open('../../../Dataset/sample_600k_lines.json') as f:
            data = f.readlines()
        data = [json.loads(x.strip()) for x in data]
    except Exception as e:
        print('Error: ', e)

    # Heading for the charts
    heading_label = tk.Label(scrollable_frame, text="Admin Dashboard", font=("Arial", 22, "bold", "italic"), fg="white")
    heading_label.pack(fill="x", pady=10)

    # Add all the components to the scrollable_frame
    all_cards(scrollable_frame, data)

    all_charts(scrollable_frame, data)

    # Create a frame for the tables and add it to the scrollable_frame
    tables_frame = tk.Frame(scrollable_frame)
    tables_frame.pack(fill="x")

    # Call the function to place two tables
    place_tables(tables_frame,data)

    # Run the application
    root.mainloop()



full_gui()

