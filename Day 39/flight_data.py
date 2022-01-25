

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, depart_city, depart_c_code):
        self.depart_city = depart_city
        self.depart_c_code = depart_c_code

    def scrap_imp_details(self, data):
        arrival_city = data['route'][0]['cityTo']
        arrival_city_code = data['route'][0]['cityCodeTo']
        outbound_date = data['route'][0]['utc_departure'].split("T")[0]  # to destinatio
        inbound_date = data['route'][1]['utc_departure'].split("T")[0]   # back to home city
        price = data['price']
        msg = f"Low price alert! Only £{price} to fly from {self.depart_city}-{self.depart_c_code} to " \
              f"{arrival_city}-{arrival_city_code}, from {outbound_date} to {inbound_date} (both date in UTC.)"

        return msg.encode('utf-8')
