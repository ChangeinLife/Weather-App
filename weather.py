from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json['name']
        weather = json['weather'][0]['main']
        weather1 = json['weather'][0]['description']
        temp = json['main']['temp']
        final = (city, weather, weather1, temp)
        return final
    else: 
        return None




def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}'.format(weather[0])
        weather_lbl['text'] = '{}'.format(weather[1], weather[2])
        temp_lbl['text']= '{:.0f}°F'.format(weather[3])
        
    else:
        messagebox.showerror('Error', 'Can not find city {}'.format(city))




app =Tk()
app.title("Weather App")
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app, textvariable = city_text, font=('bold', 30))
city_entry.pack(padx=5, pady=20)

search_btn = Button(app, text= 'Search Weather', width = 30, font=('bold', 30), command=search)
search_btn.pack(padx=5, pady=20)

location_lbl = Label(app, text='Location', font=('bold', 30))
location_lbl.pack(padx=5, pady=20)


weather_lbl = Label(app, text='Weather', font=('bold', 30))
weather_lbl.pack(padx=5, pady=20)


temp_lbl = Label(app, text='Temperature',font=('bold', 30))
temp_lbl.pack(padx=5, pady=20)

app.mainloop()








