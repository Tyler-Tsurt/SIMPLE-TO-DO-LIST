import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

# Function to refresh the task list
def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Function to add a task
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        refresh_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

# Create the main window
app = tk.Tk()
app.title("Simple To-Do List")

# Create and place widgets
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(app, width=40, height=10)
task_listbox.pack(pady=10)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Run the application
app.mainloop()
