import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}


def get_news(stock_data):
    data = list(stock_data.items())[:2]
    d1 = float(data[0][1]["4. close"])  # yesterday
    # d1_date = data[0][0]
    # d2_date = data[1][0]
    d2 = float(data[1][1]["4. close"])  # day before yesterday

    diff = round(d1 - d2, 2)
    per_change = round((diff / d1) * 100, 2)
    if abs(per_change) > 5:
        return per_change
    else:
        return False


def get_headline_and_brief(news_data):
    # hd_br = []
    for news in news_data:
        title = news["title"]
        brief = news["content"]
        # hd_br.append((title, brief))
        send_sms(title, brief)

    # return hd_br


def send_sms(hd, brief):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    if per_inc > 0:
        sign = "🔺"
    else:
        sign = "🔻"
    msg = f"{STOCK}: {sign}{abs(per_inc)}%\nHeadline: {hd}\nBrief: {brief}"
    message = client.messages.create(
        body=msg,
        from_=os.getenv("SENDING_NUMBER"),
        to=os.getenv("RECEIVING_NUMBER")
    )
    print(message.status)


#  STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response_stock = requests.get(STOCK_URL, params=stock_params)
data_stock = response_stock.json()
ds_daily = data_stock["Time Series (Daily)"]

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


per_inc = get_news(ds_daily)
if per_inc:
    response_news = requests.get(NEWS_URL, params=news_params)
    data_news = response_news.json()
    # print(type(data_news["articles"]))
    hl_br = get_headline_and_brief(data_news["articles"][:3])
    # get_headline_and_brief(data_news[:3])
else:
    print("NO STOCK CHANGE ABOVE THRESHOLD SO NO NEWS, EW!!🤣")


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
