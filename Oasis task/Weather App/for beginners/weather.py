import requests

def get_weather_data(location):
    API_KEY = '48a90ac42caa09f90dcaeee4096b9e53'
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
    response = requests.get(BASE_URL, params={'q': location, 'appid': API_KEY, 'units': 'metric'})
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    if data:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather = data['weather'][0]['description']
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather}")
    else:
        print("Could not retrieve weather data.")

def main():
    location = input("Enter city or ZIP code: ")
    weather_data = get_weather_data(location)
    display_weather(weather_data)

if __name__ == '__main__':
    main()
