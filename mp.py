import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def add_note():
        try:
            file = fd.askopenfilename(
            #defaultextension= ".txt",
                filetypes=[("Все файлы","*.*")]
            )
            with open (file, 'r',encoding="utf-8") as file:
                note = file.read()
            #note = f"\n Начать подготовку к итоговой работе."
                txt.insert(tk.END, note)
        except FileNotFoundError:
             mb.showerror("Ошибка","Файл не выбран")
             
def delete_note():
    txt.delete(1.0, tk.END)

def save_note():
        try:
            file = fd.asksaveasfilename()
            with open(file, "w",encoding="utf-8") as file:
                file.write(txt.get(1.0, tk.END))
        except Exception as e:
             mb.showinfo("Ошибка",f"Возникла ошибка {e}")


win = tk.Tk()
win.geometry("600x500+200+200")
win.title("Менеджер заметок")

txt = tk.Text(win, width=40, height=8, wrap="word")
txt.pack(side = tk.LEFT)
mainmenu = tk.Menu(win)
win.config(menu=mainmenu)
fm = tk.Menu(mainmenu, tearoff= 1)
fm.add_command(label = "Открыть", command= add_note)
fm.add_command(label = "Очистить", command= delete_note)
fm.add_command(label = "Сохранить", command= save_note)

fm.add_separator()
fm.add_command(label = "Закрыть", command= win.destroy)

mainmenu.add_cascade(label ="File", menu=fm)

scr = tk.Scrollbar(win, command=txt.yview)
scr.pack(side = tk.LEFT, fill = tk.Y)
txt.configure(yscrollcommand= scr.set)

# b1 = tk.Button(win, text = "Добавить заметку", command= add_note)
# b1.pack(side = tk.LEFT)

# b2 = tk.Button(win, text = "Очистить поле", command= delete_note)
# b2.pack(side = tk.LEFT)

# b3 = tk.Button(win, text = "Сохранить файл", command= save_note)
# b3.pack(side = tk.LEFT)

win.mainloop()
             