import requests
from bs4 import BeautifulSoup

def get_weather(api_key, city):
    # Use OpenWeatherMap API to get weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Extract relevant information from the API response
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Display the weather information
        print(f"Weather in {city}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print(f"Failed to retrieve weather data. Error code: {response.status_code}")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "81ef0556e40623d35aae1c9122ed4dff"
    city = input("Enter the city name: ")
    
    get_weather(api_key, city)
