Here’s a professional **README.md** for your weather CLI app. I’ve included instructions for creating an account and generating the API key on WeatherAPI.

---

````markdown
# Simple Weather CLI App

A command-line Python application that fetches and displays instant weather information for any city using the [WeatherAPI](https://www.weatherapi.com/) service.

---

## Features

- Get current temperature, feels-like temperature, and weather conditions.
- View humidity, wind speed, pressure, and cloud cover.
- User-friendly terminal display.
- Continuous CLI interaction until the user chooses to exit.

---

## Prerequisites

- Python 3.7+
- `requests` library
- `python-dotenv` library

Install required packages using:

```bash
pip install requests python-dotenv
````

---

## Setup Instructions

1. **Create a WeatherAPI account**
   Go to [WeatherAPI](https://www.weatherapi.com/) and sign up for a free account.

2. **Generate your API Key**
   After signing up, navigate to your dashboard and copy your **API key**.

3. **Create a `.env` file** in the project root directory:

```
WEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with the key you obtained from WeatherAPI.

---

## Usage

Run the app from the terminal:

```bash
python weather_cli.py
```

Example session:

```
Simple Weather CLI App
------------------------------
Enter city name (or type 'exit'): Kigali

========================================
Weather Report for Kigali, Rwanda
========================================
Local Time      : 2026-02-11 17:43
Temperature     : 24°C
Feels Like      : 25°C
Condition       : Partly cloudy
Humidity        : 60%
Wind Speed      : 10 kph
Pressure        : 1012 mb
Cloud Cover     : 50%
========================================
```

Type `exit` to quit the app.

---

## Project Structure

```
weather_api/
├── main.py              # Main Python script
├── .env                 # Environment file containing your API key
└── INSTRUCTIONS.md            # This file
```

---

## Notes

* Make sure to **keep your API key private** and do not share it publicly.
* If you receive an error about the API key, verify that your `.env` file exists and contains the correct key.
* The free WeatherAPI plan has limitations on requests per month. Check their [pricing & limits](https://www.weatherapi.com/pricing.aspx).

---

## License

This project is open-source and available under the MIT License.

```

---
