import tkinter as tk
from tkinter import messagebox

#Create the main window
window =tk.Tk()
window.title("To Do List")
window.geometry("400x400")

#list to store task
tasks=[]

#functions for performing task
def add_task():
    task=task_entry.get()
    if task != "":
        tasks.append({'task': task, 'completed': False})
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning(title="Attention!!",message="To add a task please write some task")

def delete_task():
    selected_task_index=task_listbox.curselection()
    if selected_task_index:
        task_index=selected_task_index[0]
        del tasks[task_index]
        update_task_listbox()
    else:
        messagebox.showwarning(Warning="Attention !!",message="You need to selete a task to delete")

def complete_task():
    selected_task_index=task_listbox.curselection()
    if selected_task_index:
        task_index=selected_task_index[0]
        tasks[task_index]["completed"]=True
        update_task_listbox()
    else:
        messagebox.showwarning(Warning="Attention!!",message="You need to select a task ")

def update_task_listbox():
    task_listbox.delete(0,tk.END)
    for task in tasks:
        status=("Done") if task["completed"] else "Not Done"
        task_listbox.insert(tk.END, f"{task['task']} [{status}]")

#create widget for adding tasks
task_entry=tk.Entry(window,width=30)
task_entry.pack(pady=10)

task_listbox=tk.Listbox(window,width=50,height=15)
task_listbox.pack(pady=10)

button_frame=tk.Frame(window)
button_frame.pack(pady=10)

add_button=tk.Button(button_frame,text="Add Task",command=add_task)
add_button.grid(row=0,column=0)

delete_button=tk.Button(button_frame,text="Delete Task",command=delete_task)
delete_button.grid(row=0,column=1)

complete_button=tk.Button(button_frame,text="Mark complete",command=complete_task)
complete_button.grid(row=0,column=2)

window.mainloop()