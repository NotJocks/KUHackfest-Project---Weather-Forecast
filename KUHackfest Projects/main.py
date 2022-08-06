import tkinter as tk
import requests
from PIL import Image, ImageTk


main = tk.Tk()
main.title("Weather Forecast by Jason K. C.")
main.resizable(False, False)


h = 500
w = 600


def format_response(weather_json):
    try:
        city = weather_json["name"]
        conditions = weather_json["weather"][0]["description"]
        temp = weather_json['main']['temp']
        pressure = weather_json["main"]['pressure']
        humidity = weather_json["main"]['humidity']
        final_str = "Location: %s \nConditions: %s \nTemperature (°C): %s \nPressure: %s \nHumidity: %s" % (city, conditions, temp, pressure, humidity)
    except:
        final_str = "There was an error fetching the requested data :("
    return final_str
 
def get_weather(city):
    weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city, 'units':'metric'}
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()

    label['text'] = format_response(response.json())

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)
    
    
def open_image(icon):
    size = int(lframe.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img
        

canvas = tk.Canvas(main, height=h, width=w)
canvas.pack()

bgi = tk.PhotoImage(file="background.png")
bglab = tk.Label(main, image=bgi)
bglab.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(main, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Courier", 12))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Go!", font=("Courier", 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lframe = tk.Frame(main, bg="#80c1ff", bd=10)
lframe.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lframe, font=15, anchor="nw", justify="left", bd = 4)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bd=0, highlightthickness=1)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)







main.mainloop()




