import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, token, username, project, name):
        self.headers = {
            "Authorization": f"Bearer {token}"
        }
        self.username = username
        self.project = project
        self.name = name
        self.url = f"https://api.sheety.co/{self.username}/{self.project}/{self.name}"

    def get_sheet_data(self):
        res = requests.get(self.url, headers=self.headers)
        return res.json()

    def add_sheet_data(self, city, code, price):
        sheety_params = {
            f"{self.name[:-1]}": {
                "city": city,
                "iataCode": code,
                "lowestPrice": price,
            }}
        sheety_res = requests.post(self.url, json=sheety_params, headers=self.headers)
        return sheety_res.text

    def edit_sheet_data(self, code, iata):
        url = self.url + f'/{code}'

        parms = {
            f"{self.name[:-1]}": {
                "iataCode": iata,
            }}

        res = requests.put(url, json=parms, headers=self.headers)
        return res.text


