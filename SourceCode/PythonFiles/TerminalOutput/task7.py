import tkinter as tk
from dashboard import full_gui

# This function is called hen task 7 is selected by the user
def run_gui(handle_tasks_callback, data):
    # Create the GUI
    root = tk.Tk()
    # Title of the GUI
    root.title("Data Analysis")

    # Function to be called when the "Run Task" button is pressed
    def on_run_task():
        # Get the values from the entry fields
        task_id = task_id_entry.get()
        visitor_uuid = visitor_uuid_entry.get()
        doc_uuid = doc_uuid_entry.get()
        handle_tasks_callback(task_id, data, visitor_uuid, doc_uuid)
    
    # Function to be called when the "Full Document Analysis" button is pressed
    def on_full_analysis():
        full_gui(data)

    # Define padding
    label_padx = 10
    label_pady = 2
    entry_padx = 10
    entry_pady = 4
    button_padx = 10
    button_pady = 10

    # Create and place the input fields and labels for task ID
    tk.Label(root, text="Task ID").pack(padx=label_padx, pady=label_pady)
    task_id_entry = tk.Entry(root)
    task_id_entry.pack(padx=entry_padx, pady=entry_pady)

    # Create and place the input fields and labels for visitor UUID
    tk.Label(root, text="Visitor UUID").pack(padx=label_padx, pady=label_pady)
    visitor_uuid_entry = tk.Entry(root)
    visitor_uuid_entry.pack(padx=entry_padx, pady=entry_pady)

    # Create and place the input fields and labels for document UUID
    tk.Label(root, text="Document UUID").pack(padx=label_padx, pady=label_pady)
    doc_uuid_entry = tk.Entry(root)
    doc_uuid_entry.pack(padx=entry_padx, pady=entry_pady)

    # # Create and place the input fields and labels for file name
    tk.Label(root, text="File Name").pack(padx=label_padx, pady=label_pady)
    file_name_entry = tk.Entry(root)
    file_name_entry.pack(padx=entry_padx, pady=entry_pady)

    # Create and place the "Run Task" button
    run_button = tk.Button(root, text="Run Task", command=on_run_task)
    run_button.pack(padx=button_padx, pady=button_pady)

    # Create and place the "Full Document Analysis" button
    full_analysis_button = tk.Button(root, text="Full Document Analysis", command=on_full_analysis)
    full_analysis_button.pack(padx=button_padx, pady=button_pady)


    # Start the GUI event loop
    root.mainloop()
