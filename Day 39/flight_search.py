import requests
from datetime import datetime


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, key):
        self.kiwi_header = {
            "apikey": key
        }
        self.url = "https://tequila-api.kiwi.com"
        self.currency = "GBP"
        self.departure_airport_code = "LON"

    def get_flight_code(self, flight_name):
        url = self.url + "/locations/query"
        parms = {
            "term": flight_name
        }
        res = requests.get(url, params=parms, headers=self.kiwi_header)
        return res.json()["locations"][0]["code"]

    def get_flight_data(self, flight_detail):
        iata_code = flight_detail['iataCode']
        lowest_price = flight_detail['lowestPrice']
        url = self.url + '/v2/search'
        now = datetime.now()
        from_date = datetime(year=now.year, month=now.month, day=now.day + 1).strftime("%d/%m/%Y")
        to_date = datetime(year=now.year, month=now.month + 6, day=now.day + 1).strftime("%d/%m/%Y")

        kiwi_params = {
            "fly_from": self.departure_airport_code,
            "fly_to": iata_code,
            "date_from": from_date,
            "date_to": to_date,
            "price_to": lowest_price,
            "flight_type": "round",
            "curr": self.currency,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0
        }
        res = requests.get(url=url, params=kiwi_params, headers=self.kiwi_header)

        if res.json():
            if res.json()['data']:
                # return res.json()['data'][0]['price']
                return res.json()['data'][0]

        return False
