import requests
import csv
import smtplib
import os


my_email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
weather_api_key = os.environ["WEATHER_API_KEY"]
latitude = os.environ.get("LATITUDE", "12.268583")
longitude = os.environ.get("LONGITUDE", "6.554311")

params = {
    "lat": latitude,
    "lon": longitude,
    "appid": weather_api_key,
    "cnt": 4
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast",
    params=params
)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"][:4]:
    weather_id = hour_data["weather"][0]["id"]

    if weather_id < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        with open("emails.csv", mode="r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                recipient = row.get("email")
                if not recipient:
                    continue

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=recipient,
                    msg="Subject:Rain Alert\n\nIt's going to rain today. Remember to bring an umbrella, forecast by bawunallah."
                )

                print(f"Email sent to {recipient}")
