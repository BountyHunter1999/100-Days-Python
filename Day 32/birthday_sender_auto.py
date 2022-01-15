import datetime as dt
import pandas as pd
import os
from dotenv import load_dotenv
from random import choice
import smtplib


load_dotenv()
sender_email = os.getenv("sender_email")
sender_pw = os.getenv("sender_pw")


def get_letter(b_name):
    letter_file = choice(letters)
    with open(f"letter_templates/{letter_file}") as f:
        letter = f.readlines()
        letter = "".join(letter)
    letter = letter.replace("[NAME]", b_name)
    return letter


def send_birthday_wish(receiver_email, b_name):
    letter = get_letter(b_name)
    message = f"SUBJECT: Happy Birthday!!!\n\n{letter}"
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(sender_email, sender_pw)
        conn.sendmail(sender_email, receiver_email, msg=message)


# Get today's date
today = dt.datetime.now()
day = today.day
month = today.month

# Get birthdays
data = pd.read_csv("birthdays.csv")

# Get Letters
letters = os.listdir("letter_templates")
match_bdate_data = data.loc[data["month"] == month].to_dict(orient="records")

if match_bdate_data:
    for row in match_bdate_data:
        email_receiver = row['email']
        name = row['name']
        send_birthday_wish(email_receiver, name)
