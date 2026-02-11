#!/usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_instant_weather(location: str):
    """
    Get instant weather information for a city.
    """
    weather_api_key = os.getenv("WEATHER_API_KEY")

    if not weather_api_key:
        raise ValueError("Weather API key is missing. Check your .env file.")

    parameters = {
        "key": weather_api_key,
        "q": location
    }

    base_url = "http://api.weatherapi.com/v1/current.json"

    try:
        response = requests.get(base_url, params=parameters, timeout=30)
        response.raise_for_status()
    except requests.RequestException as error:
        return {"error": f"Request failed: {error}"}

    data = response.json()

    return {
        "location": data["location"]["name"],
        "country": data["location"]["country"],
        "localtime": data["location"]["localtime"],
        "temperature_c": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "feelslike_c": data["current"]["feelslike_c"],
        "humidity": data["current"]["humidity"],
        "wind_kph": data["current"]["wind_kph"],
        "pressure_mb": data["current"]["pressure_mb"],
        "cloud": data["current"]["cloud"]
    }


def display_weather(weather):
    """Display weather in a user-friendly format"""

    if "error" in weather:
        print("\nError:", weather["error"])
        return

    print("\n" + "=" * 40)
    print(f"Weather Report for {weather['location']}, {weather['country']}")
    print("=" * 40)
    print(f"Local Time      : {weather['localtime']}")
    print(f"Temperature     : {weather['temperature_c']}°C")
    print(f"Feels Like      : {weather['feelslike_c']}°C")
    print(f"Condition       : {weather['condition']}")
    print(f"Humidity        : {weather['humidity']}%")
    print(f"Wind Speed      : {weather['wind_kph']} kph")
    print(f"Pressure        : {weather['pressure_mb']} mb")
    print(f"Cloud Cover      : {weather['cloud']}%")
    print("=" * 40 + "\n")


def main():
    print("Simple Weather CLI App")
    print("-" * 30)

    while True:
        city = input("Enter city name (or type 'exit'): ").strip()

        if city.lower() == "exit":
            print("Goodbye!")
            break

        weather = get_instant_weather(city)
        display_weather(weather)


if __name__ == "__main__":
    main()
