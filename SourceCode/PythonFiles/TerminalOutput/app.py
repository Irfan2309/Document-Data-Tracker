import argparse
from plot_browser import get_browser, get_all_browsers
import matplotlib.pyplot as plt
import json
from plot_reader_time import user_reader_time
from helper_functions import create_histogram
from collections import Counter
from plot_countries import plot_countries, plot_continents
from also_likes import also_likes, generate_graph
from task7 import run_gui
import tkinter as tk


def handle_task_2a(data, doc_uuid):
    plot_countries(data, doc_uuid)

def handle_task_2b(data, doc_uuid):
    plot_continents(data, doc_uuid)


def handle_task_3a(data):
     # Get browser counts
    browser_counts = Counter(get_all_browsers(data))

    #plot 
    create_histogram(browser_counts, 'Browser Histogram', 'Browser', hide_xticks=True)

def handle_task_3b(data):
    # Get browser counts
    browser_counts = get_browser(data)

    # Print results and create histogram
    create_histogram(browser_counts, 'Browser Histogram', 'Browser')

# Modify the handle_task_4 function in app.py
def handle_task_4(data):
    top_readers = user_reader_time(data)

    # Create a new Tkinter window for displaying the results
    result_window = tk.Tk()
    result_window.title("Task 4 Results")

    # Create a Text widget to display the results
    result_text = tk.Text(result_window)
    result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Insert the results into the Text widget with the desired format
    result_text.insert(tk.END, "=======================================\n")
    result_text.insert(tk.END, "=            Top 10 Readers           =\n")
    result_text.insert(tk.END, "=======================================\n")
    result_text.insert(tk.END, "=       User ID       =   Read Time   =\n")
    result_text.insert(tk.END, "=======================================\n")
    
    for i in range(10):
        user_id = top_readers[i][0]
        read_time = top_readers[i][1]
        result_text.insert(tk.END, f"=  {user_id:16s}  ={read_time:9d} secs  =\n")

    result_text.insert(tk.END, "=======================================\n")

    # Disable editing of the Text widget
    result_text.config(state=tk.DISABLED)

    # Start the Tkinter main loop for the result window
    result_window.mainloop()



# Modify the handle_task_5d function in app.py
def handle_task_5d(data, doc_uuid, visitor_uuid):
    likes = also_likes(data, doc_uuid, visitor_uuid, sorting_function=None)

    # Calculate the required width and height based on the content
    text_width = max(len(f"{doc_id:16s}   ={readers['count']:9d}") for doc_id, readers in likes[:10])
    text_height = 15  # Assuming 15 lines of content, adjust as needed.

    # Create a new Tkinter window for displaying the results
    result_window = tk.Tk()
    result_window.title("Task 5d Results")

    # Calculate the window size based on the text size
    window_width = text_width * 10  # Adjust the multiplier as needed for desired width
    window_height = text_height * 20  # Adjust the multiplier as needed for desired height

    # Set the window's geometry to match the calculated size
    result_window.geometry(f"{window_width}x{window_height}")

    # Create a Text widget to display the results
    result_text = tk.Text(result_window)
    result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Insert the results into the Text widget with the desired format
    result_text.insert(tk.END, "==================================================\n")
    result_text.insert(tk.END, "=   Top 10 Documents also Read by The Visitors   =\n")
    result_text.insert(tk.END, "==================================================\n")
    result_text.insert(tk.END, "=                    Document ID                 =\n")
    result_text.insert(tk.END, "==================================================\n")
    
    for doc_id, readers in likes[:10]:
        result_text.insert(tk.END, f"=  {doc_id:16s} =\n")

    result_text.insert(tk.END, "==================================================\n")

    # Disable editing of the Text widget
    result_text.config(state=tk.DISABLED)

    # Start the Tkinter main loop for the result window
    result_window.mainloop()



def handle_task_6(data, doc_uuid, visitor_uuid, sorting_function=None):
    dotfile = generate_graph(data, doc_uuid, visitor_uuid, sorting_function)
    dotfile.view()

def handle_task_7(data):
    run_gui(handle_tasks, data)   

def handle_file(file_name):
    new_file_name = None
    if file_name is None:
        file_name == 'issuu_cw2_train'

    if file_name == 'issuu_cw2_train':
        new_file_name = '../../../Dataset/build_dataset.txt'
    
    if new_file_name is None:
        new_file_name = file_name
    
    try:
        with open(new_file_name) as f:
            data = f.readlines()
        data = [json.loads(x.strip()) for x in data]
        return data
    except Exception as e:
        print('Error: ', e)
        return None
    

def handle_tasks(task_id = None, data = None, visitor_uuid = None, doc_uuid = None):
    if task_id == '2a':
        handle_task_2a(data, doc_uuid)
    elif task_id == '2b':
        handle_task_2b(data, doc_uuid)
    elif task_id == '3a':
        handle_task_3a(data)
    elif task_id == '3b':
        handle_task_3b(data)
    elif task_id == '4':
        handle_task_4(data)
    elif task_id == '5d':
        handle_task_5d(data, doc_uuid, visitor_uuid)
    elif task_id == '6':
        handle_task_6(data, doc_uuid, visitor_uuid)
    elif task_id == '7':
        handle_task_7(data)
    else:
        print('Invalid Task ID')

def main():
    # Create a parser object
    parser = argparse.ArgumentParser(description='Process some UUIDs.')

    # Add arguments to the parser
    parser.add_argument('-u', '--user_uuid', required=False, help='User UUID')
    parser.add_argument('-d', '--doc_uuid', required=False, help='Document UUID')
    parser.add_argument('-t', '--task_id', required=True, help='Task ID')
    parser.add_argument('-f', '--file_name', required=True, help='JSON File with input data')

    # Parse the arguments
    args = parser.parse_args()
    # print('User UUID       :', args.user_uuid)
    # print('Document UUID   :', args.doc_uuid)
    # print('Task ID         :', args.task_id)
    # print('File Name       :', args.file_name)

    data = handle_file(args.file_name)
    if data is None:
        print('Error: Could not read file')
        return

    # Handle tasks
    handle_tasks(args.task_id, data, args.user_uuid, args.doc_uuid)



if __name__ == '__main__':
    main()