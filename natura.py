from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        image_data = BytesIO(response.content)

        img = Image.open(image_data)

        # Изменяем размер изображения
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)

        return ImageTk.PhotoImage(img)

    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


def set_image():

    url = "https://picsum.photos/600/480"

    img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


# Создание окна

window = Tk()

window.title("Nature Images")

window.geometry("620x550")


label = Label(window)

label.pack(pady=10)


button = Button(
    window,
    text="Новое изображение",
    command=set_image
)

button.pack(pady=10)


# Первое изображение при запуске

set_image()


window.mainloop()
