from tkinter import *
import requests

root = Tk()


def get_weather():
    user_city = cityField.get()

    key = '9d6dd84b881a328b5039c00c43ea0ef3'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': user_city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'


root['bg'] = '#fafafa'
root.title('Приложение погоды')
root.geometry('500x350')
root.resizable(width=True, height=True)
frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relwidth=1, relheight=1)

frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.20, rely=0.9, relwidth=1, relheight=1)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Показать погоду', command=get_weather)
btn.pack()

info = Label(frame_top, text='Информация о погоде', bg='#ffb700', font=40)
info.pack()

root.mainloop()
