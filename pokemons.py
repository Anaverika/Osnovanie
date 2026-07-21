import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

def get_pokemon_data(number):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}" # получить адрес https://pokeapi.co/api/v2/pokemon/10
        
    responce = requests.get(url) 
    responce.raise_for_status() # Проверить статус 200

    return responce.json()  # получить json

def load_image(url):#  скачивает и подготавливает изображение; # return ImageTk.PhotoImage(img)

    responce = requests.get(url)
    responce.raise_for_status()
    img = Image.open(BytesIO(responce.content))
    img.thumbnail((250,250))
    return ImageTk.PhotoImage(img)

def show_pokemon():
    try:
        number = sb.get() # получить номер

        data = get_pokemon_data(number)  # получить json
       
        img_url = data['sprites']['other']['official-artwork']['front_default'] # ссылка на изображение

        photo = load_image(img_url)

        top = tk.Toplevel(win)
        top.title(data['name'].capitalize())
        top.geometry("320x450")

        l_img= tk.Label(top, image=photo)
        l_img.image = photo
        l_img.pack(pady=10)

        info = f"""  
            Имя: {data['name']}

            Рост: {data['height']}

            Вес: {data['weight']}

            Опыт: {data['base_experience']}
"""

        l_info = tk.Label(top, text =info, font=("Arial, 13"))
        l_info.pack(pady=10)
    except Exception as e:
        print(f"{e}")
    finally:
        pb.stop()
        b.config(state=tk.NORMAL)


def start_loading():
    b.config(state=tk.DISABLED)
    pb.start(10)
    win.after(1000, show_pokemon)

def show_info():
    pass


win = tk.Tk()
win.title("Pokemon viewer")
win.geometry("400x300")

mainmenu = tk.Menu(win)
win.config(menu=mainmenu)
filemenu = tk.Menu(mainmenu, tearoff= 0)
filemenu.add_command(label="Load", command= start_loading)
filemenu.add_separator()
filemenu.add_command(label="Close", command=win.destroy)

help_menu = tk.Menu(mainmenu, tearoff=0)
help_menu.add_command(label="О программе", command = show_info)

mainmenu.add_cascade(label="File", menu=filemenu)
mainmenu.add_cascade(label ="Справка", menu = help_menu)

l = tk.Label(win,text = "Номер покемона")
l.pack(pady=10)

sb = ttk.Spinbox(win, from_=1, to=1000)
sb.pack(pady=10)

b = ttk.Button(win, text = "Получить покемона", command= start_loading)
b.pack(pady = 10)

pb = ttk.Progressbar(win, mode="indeterminate", length=250)
pb.pack(pady = 10)


win.mainloop()