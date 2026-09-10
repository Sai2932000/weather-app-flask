import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("WEATHERSTACK_API_KEY")
API_URL = "https://api.weatherstack.com/current"


def get_weather(city: str) -> dict | None:
    """Get current weather information for a city."""

    if not API_KEY:
        print("❌ WEATHERSTACK_API_KEY was not found.")
        print("Make sure your .env file exists and contains your API key.")
        return None

    params = {
        "access_key": API_KEY.strip(),
        "query": city,
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

    except requests.exceptions.RequestException as error:
        print(f"❌ Network error: {error}")
        return None

    if "error" in data:
        print(f"❌ Weatherstack API error:")
        print(f"   {data['error'].get('info', 'Unknown API error')}")
        return None

    return data


def display_weather(data: dict) -> None:
    """Display weather information."""

    location = data["location"]
    current = data["current"]

    print("\n" + "=" * 45)
    print("          🌤️  WEATHER REPORT")
    print("=" * 45)

    print(f"📍 City         : {location['name']}")
    print(f"🌍 Country      : {location['country']}")
    print(f"🌡️ Temperature  : {current['temperature']}°C")
    print(f"🌡️ Feels Like   : {current['feelslike']}°C")
    print(f"☁️ Condition    : {current['weather_descriptions'][0]}")
    print(f"💧 Humidity     : {current['humidity']}%")
    print(f"💨 Wind Speed   : {current['wind_speed']} km/h")
    print(f"🧭 Wind Degree  : {current['wind_degree']}°")
    print(f"👁️ Visibility   : {current['visibility']} km")
    print(f"🔆 UV Index     : {current['uv_index']}")

    print("=" * 45)


def main() -> None:
    """Main application."""

    print("🌎 Weather App")

    city = input("Enter city: ").strip()

    if not city:
        print("❌ Please enter a city name.")
        return

    print(f"\n🔍 Fetching weather for {city}...")

    weather_data = get_weather(city)

    if weather_data:
        display_weather(weather_data)


if __name__ == "__main__":
    main()