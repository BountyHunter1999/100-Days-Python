import smtplib
import time

import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

MY_LAT = float(os.getenv("LATITUDE"))
MY_LONG = float(os.getenv("LONGITUDE"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PW = os.getenv("SENDER_PW")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
MOE = 5  # margin of error for iss location overhead

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.


def is_iss_near():
    lng_diff = abs(iss_longitude - MY_LONG)
    lat_diff = abs(iss_latitude - MY_LAT)

    if lng_diff <= 5 and lat_diff <= 5:
        return True

    return False


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    res = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()
    data_rise_set = res.json()
    sunrise = int(data_rise_set["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_rise_set["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    if hour >= sunset or hour <= sunrise:
        return True
    return False


print(is_night_time())

while True:
    time.sleep(60)
    if is_night_time() and is_iss_near():
        message = f"SUBJECT: ISS VISIBLE \n\nLOOK UP, YOU CAN SEE THE ISS!!"
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(SENDER_EMAIL, SENDER_PW)
            conn.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg=message)
