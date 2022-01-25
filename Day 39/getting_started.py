import os
from dotenv import load_dotenv
from user_manager import UserManager

load_dotenv()

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
USER_SHEET_PROJECT = os.getenv("USER_SHEET_PROJECT")
USER_SHEET_NAME = os.getenv("USER_SHEET_NAME")
USER_SHEETY_URL = f'https://api.sheety.co/{SHEETY_USERNAME}/{USER_SHEET_PROJECT}/{USER_SHEET_NAME}'
USER_SHEETY_TOKEN = os.getenv("USER_SHEETY_TOKEN")

user_manager = UserManager(token=USER_SHEETY_TOKEN, username=SHEETY_USERNAME,
                           project=USER_SHEET_PROJECT, name=USER_SHEET_NAME)

if __name__ == '__main__':
    user_manager.new_user()
