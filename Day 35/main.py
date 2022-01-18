import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

# for running in python anywhere free account
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {"https": os.environ['https_proxy']}

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
# client = Client(account_sid, auth_token)
client = Client(account_sid, auth_token, http_client=proxy_client)  # for python anywhere


# get the api key from https://openweathermap.org/
# to view the json file in a nice format use this: http://jsonviewer.stack.hu/

# Get lattitude and logitude from https://www.latlong.net/
# LAT = os.getenv("LAT")
# LON = os.getenv("LON")

# get a place that is definitely raining from https://www.ventusky.com/
LAT = -2.529450
LON = -44.296951


parameters = {
    "lat": LAT,
    "lon": LON,
    "exclude": "current,minutely,daily",
    "appid": os.getenv("API_KEY")
}


def take_raincoat(report):
    hourly = report["hourly"][:12]
    for hourly_data in hourly:
        weather_id = hourly_data["weather"][0]["id"]
        if weather_id < 700:
            return True
            return "Bring an Umbrella"
    return False
    return "No Umbrella Needed"


URL = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()

if take_raincoat(data):
    message = client.messages.create(
        body="It's Going To Rain Today. So, Don't Forget To Take The Raincoat",
        from_=str(os.getenv("SENDING_NUMBER")),
        to=str(os.getenv("RECEIVING_NUMBER"))
    )

    print(message.status)
else:
    print("NO NEED FOR RAINCOAT")
