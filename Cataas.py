from tkinter import *
from PIL import Image, ImageTk
import requests  # Библиотека для отправки запросов
from io import BytesIO  # Библиотека ввода-вывода информации. Здесь в двоичном коде.


def load_image(url):
    try:
        # Отправляем GET-запрос с использованием requests.get()
        response = requests.get(url)
        # Проверяем успешность запроса (код ответа 200)
        response.raise_for_status()
        # Читаем байты из ответа в объект BytesIO
        image_data = BytesIO(response.content)
        # Открываем изображение с помощью PIL
        img = Image.open(image_data)
        # Изменяем размер изображения, подгоняя под размер окна
        img.thumbnail((600, 520), Image.Resampling.LANCZOS)  # Способ конвертации

        #  Возвращает изображение, которое вставится в метку
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None

def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)  # загрузка картинки с url

    if img:
        # Создаем новое вторичное окно
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x520")

        # Добавляем изображение в новое окно
        label = Label(new_window, image=img)
        label.pack()
        label.image = img  # Сохраняем ссылку на изображение


def exit():
    window.destroy()


window = Tk()
window.title('Cats')
window.geometry('600x520')

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text='Загрузить по тегу', command=open_new_window)
load_button.pack()



# Создаем меню
menu_bar = Menu(window)
window.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = 'https://cataas.com/cat'

window.mainloop()
