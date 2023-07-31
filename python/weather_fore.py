import requests

def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change the units to "imperial" for Fahrenheit.
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None

def display_weather_data(data):
    if data:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("No weather data available.")

def main():
    api_key = "80616dfed1169a50aa13053420bfc7c8"
    city = input("Enter the city name: ")

    weather_data = get_weather_data(api_key, city)
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()