import tkinter as tk
import datetime
from tkinter import filedialog as fd
from tkinter import messagebox as mb


def add_note():
    try:
        file = fd.askopenfilename(
            filetypes=[("Текстовые файлы","*.txt"), ("Все файлы","*.*")]
            )
        
        with open ( file,'r', encoding="utf-8") as file:
            file = file.read()
        # current_date = datetime.date.today()
        # note= f"{current_date} Запланировать подготовку к итоговой работе!\n"
        txt.insert(tk.END, file)
    except FileNotFoundError:
        mb.showerror("Ошибка","Выберите файл !")




def clear_note():
    
    last_line = txt.index("end-2l linestart")
    print(last_line)
    txt.delete(1.0, tk.END)


def save_note():
    try:
        file = fd.asksaveasfilename(
            defaultextension=(".txt"),
            filetypes=[("Текстовый фалы","*.txt"),("Все файлы","*.*")]

        )

        note = txt.get(1.0, tk.END)

        with open(file, "w", encoding="utf-8") as file:
            file.write(note)
    except FileNotFoundError:
        mb.showerror("Ошибка", "Вы не выбрали файл для сохранения")



win = tk.Tk()
win.title("Менеджер  проектов")
win.geometry("600x500+400+200")


txt = tk.Text(win,width=40, height=10, wrap="word")
txt.pack(side=tk.LEFT)

scr = tk.Scrollbar(win, command=txt.yview)
scr.pack(side=tk.LEFT, fill=tk.Y)
txt.config(yscrollcommand=scr.set)

mainmenu = tk.Menu(win)
win.config(menu=mainmenu)

fm = tk.Menu(mainmenu, tearoff= 0)
fm.add_command(label="Добавить",command=add_note)


mainmenu.add_cascade(label="File",menu=fm)



# b1 = tk.Button(win, text = "Добавить заметку", command= add_note)
# b1.pack(side=tk.LEFT)


# b2 = tk.Button(win, text= "Очистить поле", command= clear_note)
# b2.pack(side=tk.LEFT)

# b3 = tk.Button(win, text= "Сохранить файл", command=save_note)
# b3.pack(side=tk.LEFT)


win.mainloop()