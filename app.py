from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("WEATHERSTACK_API_KEY")
API_URL = "https://api.weatherstack.com/current"


def get_weather(city):
    if not API_KEY:
        return None, "WEATHERSTACK_API_KEY was not found."

    params = {
        "access_key": API_KEY.strip(),
        "query": city
    }

    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")
        return None, "Unable to connect to weather service."

    # Weatherstack can return an API error
    if "error" in data:
        error_message = data["error"].get(
            "info",
            "Unknown API error"
        )

        print(f"Weatherstack API error: {error_message}")

        return None, error_message

    return data, None


@app.route("/", methods=["GET", "POST"])
def home():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form["city"].strip()

        if not city:
            error = "Please enter a city name."

        else:
            weather_data, error = get_weather(city)

            if weather_data:

                location = weather_data["location"]
                current = weather_data["current"]

                weather = {
                    "city": location["name"],
                    "country": location["country"],
                    "temperature": current["temperature"],
                    "feelslike": current["feelslike"],
                    "condition": current["weather_descriptions"][0],
                    "humidity": current["humidity"],
                    "wind_speed": current["wind_speed"],
                    "wind_degree": current["wind_degree"],
                    "visibility": current["visibility"],
                    "uv_index": current["uv_index"]
                }

    return render_template(
        "index.html",
        weather=weather,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)