# gui.py
import tkinter as tk

def run_gui(handle_tasks_callback, data):
    root = tk.Tk()
    root.title("Data Analysis Tool")

    # Function to be called when the "Run Task" button is pressed
    def on_run_task():
        task_id = task_id_entry.get()
        doc_uuid = doc_uuid_entry.get()
        visitor_uuid = visitor_uuid_entry.get()
        file_name = file_name_entry.get()

        # Here we are assuming handle_tasks_callback is expecting four arguments
        # You may need to adjust this depending on how handle_tasks is implemented
        handle_tasks_callback(task_id, data, visitor_uuid, doc_uuid)


    # Create and place the entry fields and labels
    tk.Label(root, text="Task ID").pack()
    task_id_entry = tk.Entry(root)
    task_id_entry.pack()

    tk.Label(root, text="Document UUID").pack()
    doc_uuid_entry = tk.Entry(root)
    doc_uuid_entry.pack()

    tk.Label(root, text="Visitor UUID").pack()
    visitor_uuid_entry = tk.Entry(root)
    visitor_uuid_entry.pack()

    tk.Label(root, text="File Name").pack()
    file_name_entry = tk.Entry(root)
    file_name_entry.pack()

    # Create and place the "Run Task" button
    run_button = tk.Button(root, text="Run Task", command=on_run_task)
    run_button.pack()

    # Start the GUI event loop
    root.mainloop()
