import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(location):
    API_KEY = '48a90ac42caa09f90dcaeee4096b9e53'
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
    response = requests.get(BASE_URL, params={'q': location, 'appid': API_KEY, 'units': 'metric'})
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather():
    location = location_entry.get()
    weather_data = get_weather_data(location)
    if weather_data:
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather = weather_data['weather'][0]['description']
        result_label.config(text=f"Temperature: {temp}°C\nHumidity: {humidity}%\nWeather: {weather}")
    else:
        messagebox.showerror("Error", "Could not retrieve weather data.")

app = tk.Tk()
app.title("Weather App")

tk.Label(app, text="Enter city or ZIP code:").pack()
location_entry = tk.Entry(app)
location_entry.pack()
tk.Button(app, text="Get Weather", command=display_weather).pack()
result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
