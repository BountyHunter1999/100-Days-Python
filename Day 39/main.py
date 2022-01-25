import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData
from user_manager import UserManager

load_dotenv()

# Sheety constants
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PROJECT = os.getenv("SHEETY_PROJECT")
SHEET_NAME = os.getenv("SHEET_NAME")
SHEETY_URL = f'https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT}/{SHEET_NAME}'
SHEETY_AUTH_BEARER_TOKEN = os.getenv("SHEET_TOKEN")

USER_SHEET_PROJECT = os.getenv("USER_SHEET_PROJECT")
USER_SHEET_NAME = os.getenv("USER_SHEET_NAME")
USER_SHEETY_URL = f'https://api.sheety.co/{SHEETY_USERNAME}/{USER_SHEET_PROJECT}/{USER_SHEET_NAME}'
USER_SHEETY_TOKEN = os.getenv("USER_SHEETY_TOKEN")

# SMTP and Twilio constants
S_EMAIL = os.getenv("SENDER_EMAIL")
R_EMAIL = os.getenv("RECEIVER_EMAIL")  # this one will be provided by another sheet
EMAIL_P = os.getenv("SENDER_PW")

T_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
S_NUM = os.getenv("SENDING_NUMBER")
R_NUM = os.getenv("RECEIVING_NUMBER")  # this one will be provided by another sheet
T_SID = os.getenv("TWILIO_ACCOUNT_SID")

data_manager = DataManager(token=SHEETY_AUTH_BEARER_TOKEN, username=SHEETY_USERNAME,
                           project=SHEETY_PROJECT, name=SHEET_NAME)
flight_search = FlightSearch(os.getenv("TEQUILIA_API"))
notification_manager = NotificationManager(s_email=S_EMAIL, email_p=EMAIL_P,  # r_email=R_EMAIL,
                                           t_token=T_AUTH_TOKEN, s_num=S_NUM,
                                           t_sid=T_SID)  # r_num=R_NUM,)
flight_data = FlightData(depart_city="London", depart_c_code="STN")
user_manager = UserManager(token=USER_SHEETY_TOKEN, username=SHEETY_USERNAME,
                           project=USER_SHEET_PROJECT, name=USER_SHEET_NAME)

# Get Google Sheet Data
# data_to_check_with = data_manager.get_sheet_data()["prices"]


def add_iata_code_to_sheet(data_to_check):
    # add the iata code for flights in the sheet
    for data in data_to_check:
        code = data['id']
        data_manager.edit_sheet_data(code=code, iata=flight_search.get_flight_code(data["city"]))


# add_iata_code_to_sheet(data_to_check_with)
data_f = [
 {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
 {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
 {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
 {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
 {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}
]
# Flight Search
# for d in data_to_check_with:
user_data = user_manager.get_user()['users']
for d in data_f:
    #
    # print(f"City: {d['city']: >12} \t\t\t thresholdPrice: {d['lowestPrice']:>10} \t\t\t "
    #       f"Found Cheap Price: {flight_search.get_flight_data(d)}")
    flight = flight_search.get_flight_data(d)
    if flight:
        for user in user_data:
            r_email = user['email']
            r_num = user['phoneNumber']
            msg = flight_data.scrap_imp_details(flight)
            print(f"sending email with this {msg} to {r_email} {r_num}")
            notification_manager.send_email(r_email=r_email, msg=msg)
            # notification_manager.send_sms(r_num=r_num, msg=msg)
    else:
        print("There are no flights ")

