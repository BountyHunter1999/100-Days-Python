from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "../chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

URL = "https://www.python.org/"

driver.get(URL)

sel_dates = driver.find_elements(by="css selector", value=".event-widget .menu time")
dates = [date.text for date in sel_dates]

sel_events = driver.find_elements(by="css selector", value=".event-widget .menu a")
events = [event.text for event in sel_events]
# print(dates)
# print(events)

# print(dict(zip(dates, events)))
print({i: {"time": dates[i], "name": events[i]} for i in range(len(events))})

driver.quit()
