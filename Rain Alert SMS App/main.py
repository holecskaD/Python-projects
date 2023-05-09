import requests
from twilio.rest import Client

api_key = "8145d40391a02338017bda81d57d85a8"
lat_value = 48.85
lon_value = 2.35

# lat_value = 47.49
# lon_value = 19.04

account_sid = "ACfbae50bf5fce51e28777afe7815d76fb"
auth_token = "6c896eb0d3a187b59fdf38f8f4c7ab65"

parameters = {
    "lat": lat_value,
    "lon": lon_value,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for i in range(12):
    if weather_data["hourly"][i]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today, don't forget to bring an umbrella! ",
        from_="+12706123144",
        to="+36709406818"
    )
    print(message.status)
