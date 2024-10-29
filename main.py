from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests


def upload():
    filepath = fd.askopenfilename()
    if filepath:
        files = {'file': open(filepath, 'rb')}
        responce = requests.post('https://file.io', files=files)
        if responce.status_code == 200:
            link = responce.json()['link']
            entry.insert(0, link)



window = Tk()
window.title('Сохранение файлов в облаке')
window.geometry('400x200')

button = ttk.Button(text='Загрузить файл', command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.mainloop()
