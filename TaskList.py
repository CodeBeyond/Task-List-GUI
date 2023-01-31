import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("Task List")

def add():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="YOU SHALL NOT PASS.", message="You realize you left it blank, right? Enter a task!")

def delete():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="YOU SHALL NOT PASS.", message="I'm not a mind reader. Please select the task you wish to delete.")

def load():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="YOU SHALL NOT PASS", message="Cannot find tasks.dat.")

def save():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add", width=48, command=add)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete", width=48, command=delete)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load", width=48, command=load)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save", width=48, command=save)
button_save_tasks.pack()

root.mainloop()