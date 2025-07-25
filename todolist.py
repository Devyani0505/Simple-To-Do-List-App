import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x400")
root.title("To-Do List")

lb1 = tk.Label(root, text="Enter task:", font=('Calibri', 15))
lb1.place(x=10, y=15)

ent = tk.Entry(root, width=70)
ent.place(x=120, y=20)

lbox = tk.Listbox(root, width=70, height=10)
lbox.place(x=120, y=70)


def add_command():
    task = ent.get()
    if task.strip() != "":
        lbox.insert(tk.END, task)
        ent.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def del_command():
    try:
        pos = lbox.curselection()[0]
        lbox.delete(pos)
    except IndexError:
        messagebox.showwarning("Delete Error", "Please select a task to delete.")

def edit_command():
    try:
        pos = lbox.curselection()[0]
        new_task = ent.get()
        if new_task.strip() != "":
            lbox.delete(pos)
            lbox.insert(pos, new_task)
            ent.delete(0, tk.END)
        else:
            messagebox.showwarning("Edit Error", "Please enter the new task.")
    except IndexError:
        messagebox.showwarning("Edit Error", "Please select a task to edit.")


btn1 = tk.Button(root, text="ADD", font=('Calibri', 15), width=12, command=add_command)
btn1.place(x=90, y=250)

btn2 = tk.Button(root, text="DELETE", font=('Calibri', 15), width=12, command=del_command)
btn2.place(x=250, y=250)

btn3 = tk.Button(root, text="EDIT", font=('Calibri', 15), width=12, command=edit_command)
btn3.place(x=420, y=250)


root.mainloop()
