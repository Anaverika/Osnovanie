import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkinter import messagebox as mb

def open_file():
    try:
        file = fd.askopenfilename()
        
    
        img = Image.open(file)
        win_width = 500
        win_height = 500
        img.thumbnail((win_width,win_height))

        imgtk = ImageTk.PhotoImage(img)
        l.configure(image=imgtk)
        l.image = imgtk
        
    
    except FileNotFoundError:
        mb.showerror ("Ошибка", "Файл не найден")
    except OSError:
        mb.showerror("Ошибка"," Не удалось открыть файл")
    except Exception as e:
        mb.showerror("Ошибка",f"произошла ошибка {e}")
        

    
win = tk.Tk()
win.geometry("700x600")

mainmenu = tk.Menu(win)
win.config(menu=mainmenu)
filemenu = tk.Menu(mainmenu, tearoff= 0)
filemenu.add_command(label="Открыть", command=open_file)
filemenu.add_separator()
filemenu.add_command(label="Закрыть", command=win.destroy)

l = tk.Label(win)
l.pack()

mainmenu.add_cascade(label="File",menu=filemenu)
win.mainloop()