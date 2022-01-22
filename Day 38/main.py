import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NUTRI_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PROJECT = os.getenv("SHEETY_PROJECT")
SHEET_NAME = os.getenv("SHEET_NAME")

SHEETY_URL = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT}/{SHEET_NAME}'
SHEETY_AUTH_BEARER_TOKEN = os.getenv("TOKEN")

headers_nutritionix = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
    "Content-Type": "application/json"
    # "x-user-jwt": os.getenv("API_KEY")
}

text = input("Tell me which exercises you did: ")

nutritionix_params = {
    "query": text,
    "gender": os.getenv("GENDER"),
    "weight_kg": os.getenv("WEIGHT_KG"),
    "height_cm": os.getenv("HEIGHT_CM"),
    "age": os.getenv("AGE")
}

sheety_header = {
    "Authorization": f"Bearer {SHEETY_AUTH_BEARER_TOKEN}"
}

response = requests.post(NUTRI_URL, json=nutritionix_params, headers=headers_nutritionix).json()

activity = []
for data in response["exercises"]:
    exercise_name = data["name"]
    duration = data['duration_min']
    calorie = data["nf_calories"]
    activity.append((exercise_name, duration, calorie))

print(activity)

"""
I ran for 30 minutes and walked 45 minutes
"""

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in activity:

    sheety_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise[0],
            "duration": exercise[1],
            "calories": exercise[2]
        }}

    sheety_res = requests.post(SHEETY_URL, json=sheety_params, headers=sheety_header)

    # sheety_res = requests.get(SHEETY_URL, headers=sheety_header)

    print(sheety_res.json())
    print(sheety_res)
    print(sheety_res.text)
