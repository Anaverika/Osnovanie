import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import messagebox as mb

def load_products():

    url = "https://dummyjson.com/products?limit=60"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    products = data['products']

    titles = [product['title'] for product in products]
    return products,titles
    
products, titles = load_products()

def load_img(url):
    response = requests.get(url)
    response.raise_for_status()

    img = Image.open(BytesIO(response.content))
    img.thumbnail((250,250))

    imgtk = ImageTk.PhotoImage(img)
    l_img.config(image=imgtk)
    l_img.image = imgtk



def show_product(event):
    index = combo.current()

    product = products[index]
    print(product)

    url_img = product['thumbnail']
    img = load_img(url_img)

    info = f"""
Название товара: {product['title']}
Цена товара: ${product['price']}
Категория товара: {product['category']}
Рейтинг: {product['rating']}
Остаток: {product['stock']}
"""
    l_info.config(text = info)



win = tk.Tk()
win.title("Каталог товаров")
win.geometry("700x600")

combo = ttk.Combobox(win, values=titles, width=60)
combo.pack(pady = 10)
combo.bind("<<ComboboxSelected>>", show_product)

l_info = tk.Label(win, font=("Calibri", 12, "bold"))
l_info.pack(pady = 10)

l_img = tk.Label(win)
l_img.pack(pady =10)

win.mainloop()
            
