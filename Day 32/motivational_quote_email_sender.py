import smtplib
import os
from dotenv import load_dotenv
import random
import datetime as dt

load_dotenv()

sender_email = os.getenv("sender_email")
sender_pw = os.getenv("sender_pw")
receiver_email = os.getenv("receiver_email")

today = dt.datetime.now()
weekday = today.weekday()  # weekday starts from Monday which is 0

with open("quotes.txt") as f:
    quotes = f.readlines()
    quotes = [(quote.strip()) for quote in quotes]


def get_quote():
    quote = random.choice(quotes)
    return quote


message = f"""FROM: {sender_email}
TO: {receiver_email}
SUBJECT: Happy Birthday!!!

{get_quote()}
"""

print(get_quote())
print(message)
with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(sender_email, sender_pw)
    conn.sendmail(sender_email, receiver_email, message)
