import smtplib

import requests
from bs4 import BeautifulSoup
import lxml
from dotenv import load_dotenv
import os

load_dotenv()

USER_AGENT = os.getenv("USER_AGENT")
ACCEPT_LANG = os.getenv("ACCEPT_LANG")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PW = os.getenv("SENDER_PW")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

URL = "https://www.amazon.com/Lenovo-Legion-Pro-Gaming-GeForce/dp/B09923Z7MN/ref=sr_1_2?crid=213MST8LR84ST&keywords=" \
      "lenovo+legion+5+pro&qid=1643780869&sprefix=lenevo+legion+5+pro%2Caps%2C492&sr=8-2"
# URL = "https://www.amazon.com/Lenovo-Legion-Pro-Gaming-GeForce/dp/B09PTHV1Z1/ref=sr_1_1?crid=213MST8LR84ST&keywords=
# lenovo%2Blegion%2B5%2Bpro&qid=1643780869&sprefix=lenevo%2Blegion%2B5%2Bpro%2Caps%2C492&sr=8-1&th=1"

# http://myhttpheader.com/ we can find this here
header = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANG
}

# we need to pass the header otherwise we won't get our desired response
response = requests.get(URL, headers=header).text

soup = BeautifulSoup(response, "lxml")

# this works lol
# print(soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay"))
# print(soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay").span)

price_right_now = float(soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay")
                        .span.text.split("$")[1].replace(",", ""))
product_title = soup.find(name='span', id='productTitle').text.strip()
# print(product_title)
print(price_right_now)


def send_mail(title, price):
    msg = f"{title} is now ${price} \n {URL}"
    print("SENDING MAIL")
    message = f"SUBJECT: PRICE WITHIN YOUR RANGE!! \n\n {msg}"
    with smtplib.SMTP('smtp.gmail.com') as con:
        con.starttls()
        con.login(SENDER_EMAIL, SENDER_PW)
        con.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg=message)


desired_price = float(input("Enter the desired price for the product: "))
if price_right_now <= desired_price:
    send_mail(product_title, price_right_now)
