import tkinter as tk
import tkinterweb

def read_site():
    site  = e.get()
    frame.load_website(site)


win = tk.Tk()
win.geometry("900x700+200+200")
win.title("Мини-браузер")

l = tk.Label(win, text = "Введите сайт")
l.pack(pady = 10)

e = tk.Entry(win, width=60)
e.pack(pady = 10)

b = tk.Button(win, text = "Перейти на сайт", command = read_site)
b.pack()


frame = tkinterweb.HtmlFrame(win)
#frame.load_website("https://ya.ru")
frame.pack(fill="both", expand=True)

win.mainloop()