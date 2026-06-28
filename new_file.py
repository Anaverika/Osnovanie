import tkinter as tk

def show_info():
    name = entry_name.get()
    age = int(entry_age.get())

    if  age % 10 == 1 and  age % 100 !=11:
        word = "год"
    elif age % 10 in [2,3,4]:
        word = "года"
    else:
        word = "лет"
       #'год' if age == 1 else 'лет' if age > 4 else 'года'

#         def print_greeting():
# age = int(ef2.get().strip())
# lab2['text'] = (f'Привет {ef1.get().strip()}!\nТебе {age}'
# f' {'год' if age % 10 == 1 else 'лет' if age % 10 > 4 else 'года'}')
    
    label_result.config( text=f"Привет, {name}! Тебе {age} {word}.")



    

win = tk.Tk()
win.title("Анкета")
win.geometry("300x200")

# поле для имени
label_name = tk.Label(win, text="Имя:")
label_name.pack()

entry_name = tk.Entry(win)
entry_name.pack()

# поле для возраста
label_age = tk.Label(win, text="Возраст:")
label_age.pack()

entry_age = tk.Entry(win)
entry_age.pack()

# кнопка
button = tk.Button(win, text="Показать", command=show_info)
button.pack(pady=10)

# результат
label_result = tk.Label(win, text="")
label_result.pack()

win.mainloop()


