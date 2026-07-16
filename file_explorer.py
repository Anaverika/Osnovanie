import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import messagebox as mb
import os

current_path = ""
def choose_dir():
    directory = fd.askdirectory()
    try:    
        if directory:
            entry.delete(0,tk.END)
            entry.insert(tk.END, directory)
            show_dir(directory)
    except Exception as e:
        mb.showerror("Ошибка", {e})

def show_dir(path):
    global current_path
    current_path = path
    
    entry.delete(0,tk.END)
    entry.insert(0,path)
    listbox.delete(0,tk.END)
    try:
        items = os.listdir(path)

        for i in items:
            full_path = os.path.join(path,i) 
            if os.path.isdir(full_path):
                listbox.insert(tk.END, "📁" + i)
            else:
                listbox.insert(tk.END, "📃" + i)
    except Exception as e:
        mb.showerror("Ошибка", {e})
def open_selected(event):
    selection = listbox.curselection()
    
    
    if not selection:
        return
    
    item = listbox.get(selection[0])
    name = item[1:]
    

    full_path = os.path.join(current_path,name)
    if os.path.isdir(full_path):
        show_dir(full_path)
    
    
win = tk.Tk()
win.title("Мини-проводник")
win.geometry("700x500")

entry = tk.Entry(win, width=80)
entry.pack(pady=10)

button = tk.Button(win,text="Выбрать папку",command=choose_dir)
button.pack()

listbox = tk.Listbox(win, width=90, height=25, font=("Arial", 20))
listbox.pack(pady = 10, fill=tk.BOTH, expand= True)
listbox.bind("<Double-Button-1>", open_selected)


win.mainloop()
