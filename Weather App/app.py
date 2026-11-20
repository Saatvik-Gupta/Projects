# run--> cd "Weather App"--> then python app.py
# Backend

from flask import Flask, render_template, request
import requests
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

API_KEY = "79da123e2b2e6f1a2706009075979e3e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def format_time(timestamp, offset):
    tz = timezone(timedelta(seconds=offset))
    return datetime.fromtimestamp(
        timestamp, tz
    ).strftime("%I:%M %p")


@app.route("/", methods=["GET", "POST"])
def home():

    weather = None
    error = None

    if request.method == "POST":

        city = request.form.get("city", "").strip()

        if not city:
            error = "Please enter a city name."

        else:
            params = {
                "q": city,
                "appid": API_KEY,
                "units": "metric"
            }

            try:
                response = requests.get(
                    BASE_URL,
                    params=params,
                    timeout=10
                )

                data = response.json()

                if response.status_code == 200:

                    offset = data["timezone"]

                    weather = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": round(data["main"]["temp"]),
                        "feels_like": round(data["main"]["feels_like"]),
                        "humidity": data["main"]["humidity"],
                        "pressure": data["main"]["pressure"],
                        "wind": data["wind"]["speed"],
                        "description": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"],
                        "sunrise": format_time(data["sys"]["sunrise"], offset),
                        "sunset": format_time(data["sys"]["sunset"], offset)
                    }

                else:
                    error = data.get("message", "Unable to fetch weather data.")

            except requests.exceptions.RequestException:
                error = "Network error. Please try again."

    return render_template(
        "index.html",
        weather=weather,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)

