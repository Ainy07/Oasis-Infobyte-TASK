## Weather App
This Weather App is a simple Python application that provides current weather information for a specified location using a graphical user interface (GUI) built with Tkinter.

## Features
- Fetches current weather data using the OpenWeatherMap API.
- Displays temperature, humidity, and weather conditions.
- User-friendly GUI for entering city or ZIP code and viewing weather details.

## Installation
### Prerequisites
- Python 3.x
- Required Python packages: requests, tkinter
You can install the required packages using pip:

```
pip install requests
```


## Usage
1. Navigate to the project directory.

2. Run the application:

```
python weatherapp.py
```
3. Enter a city name or ZIP code in the input field and click "Get Weather" to view the current weather information.

## Configuration
- API Key: The app uses the OpenWeatherMap API. Replace the placeholder API key in the code with your own API key.

Example in the code:

```
API_KEY = 'your_openweathermap_api_key'
```

## Contributing
Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Thanks to OpenWeatherMap for providing the weather API.
This project was inspired by the need for a simple, GUI-based weather application.