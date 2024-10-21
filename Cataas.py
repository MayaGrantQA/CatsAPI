from tkinter import *
from PIL import Image, ImageTk
import requests  # Библиотека для отправки запросов
from io import BytesIO  # Библиотека ввода-вывода информации. Здесь в двоичном коде.


def load_image():
    try:
        # Отправляем GET-запрос с использованием requests.get()
        response = requests.get(url)
        # Проверяем успешность запроса (код ответа 200)
        response.raise_for_status()
        # Читаем байты из ответа в объект BytesIO
        image_data = BytesIO(response.content)
        # Открываем изображение с помощью PIL
        img = Image.open(image_data)
        #  Возвращает изображение, которое вставится в метку
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


window = Tk()
window.title('Cats')
window.geometry('600x480')

label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = load_image(url)  # загрузка картинки с url

if img:
    label.config(image=img)
    label.image = img  # Для того чтобы картинка случайно не удалилась.

window.mainloop()
