
from tkinter import ttk
from tkinter import Tk
import tkinter.messagebox
import tkinter
import TKinterModernThemes as TKMT
import pickle


def buttonCMD():
    print("Button clicked!")

start = tkinter.Tk()
start.title("Task List")
style = ttk.Style(start)
start.option_add("*tearOff", False)
# start.tk.call("source", "forest-dark.tcl")
# style.theme_use("forest-dark")

def get_tasks_from_server():
    response = requests.get('http://localhost:3000/tasks')
    if response.status_code == 200:
        tasks = response.json().get('tasks')
        return tasks
    else:
        raise Exception('Request to Task Server failed with status code: {}'.format(response.status_code))

def add():
    enterTask = task.get()
    if enterTask != "":
        ui_box.insert(tkinter.END, enterTask)
        task.delete(0, tkinter.END)
    else:
        # pop up warning
        tkinter.messagebox.showwarning(title="YOU SHALL NOT PASS.", message="You realize you left it blank, right? Enter a task!")

def delete():
    try:
        curr_elem = ui_box.curselection()[0]
        ui_box.delete(curr_elem)
    except:
        # pop up warning
        tkinter.messagebox.showwarning(title="YOU SHALL NOT PASS.", message="I'm not a mind reader. Please select the task you wish to delete.")

def save():
    savedTasks = ui_box.get(0, ui_box.size())
    pickle.dump(savedTasks, open("tasks.dat", "wb"))

def load():
    try:
        loadTasks = pickle.load(open("tasks.dat", "rb"))
        ui_box.delete(0, tkinter.END)
        for task in loadTasks:
            ui_box.insert(tkinter.END, task)
    except:
    # pop up warning
        tkinter.messagebox.showwarning(title="YOU SHALL NOT PASS", message="Cannot find tasks.dat.")

# user interface using tkinter module
make_pretty = tkinter.Frame(start)
make_pretty.pack()

ui_box = tkinter.Listbox(make_pretty, height=20, width=80)
ui_box.pack(side=tkinter.LEFT)

scrolling = tkinter.Scrollbar(make_pretty)
scrolling.pack(side=tkinter.RIGHT, fill=tkinter.Y)

ui_box.config(yscrollcommand=scrolling.set)
scrolling.config(command=ui_box.yview)

task = tkinter.Entry(start, width=50)
task.pack()

click_add = tkinter.Button(start, text="Add", width=48, command=add)
click_add.pack()

click_delete = tkinter.Button(start, text="Delete", width=48, command=delete)
click_delete.pack()

click_load = tkinter.Button(start, text="Load", width=48, command=load)
click_load.pack()

click_save = tkinter.Button(start, text="Save", width=48, command=save)
click_save.pack()

start.mainloop()

