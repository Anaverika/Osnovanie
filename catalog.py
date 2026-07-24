import requests
import tkinter as tk

def load_products():

    url = "https://dummyjson.com/products?limit=60"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    products = data['products']


    for product in products:
        txt.insert(tk.END,
            f"Название товара: {product['title']}\n"
            f"Цена товара: {product['price']}\n"
            f"Категория товара: {product['category']}\n"
            f"Рейтинг: {product['rating']}\n"
            f"Остаток: {product['stock']}\n\n"
        )


win = tk.Tk()
win.title("Каталог товаров")
win.geometry("700x600")

frame = tk.Frame(win)
frame.pack(pady=10)


txt = tk.Text(frame, width=60, height=30, font=("Calibri", 11))
txt.pack(side=tk.LEFT)

b = tk.Button(win, text = "Загрузить товары", command=load_products)
b.pack(pady=10)

scr = tk.Scrollbar(frame, command=txt.yview)
scr.pack(side =tk.RIGHT ,fill=tk.Y)
txt.config(yscrollcommand=scr.set)

win.mainloop()
            
