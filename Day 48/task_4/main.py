from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

chrome_driver_path = "../chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

URL = "http://orteil.dashnet.org/experiments/cookie/"

driver.get(URL)

game_start = datetime.now()
x0 = game_start

cookie = driver.find_element(by="id", value="cookie")


def get_highest_item():
    store_sel = driver.find_elements(by="css selector", value="#store div")
    items = [item.get_attribute("id")
             for item in store_sel if item.get_attribute("class") != "grayed"]
    # print(f"ITEMS BEFORE: {items}")
    items = [item for item in items if item != ""]
    # print(f"ITEMS AFTER: {items}")
    if items:
        high = driver.find_element(by="id", value=f"{items[-1]}")
        high.click()


while True:
    x1 = datetime.now()
    cookie.click()

    secs = (x1 - x0).seconds
    game_end_sec = (x1 - game_start).seconds
    if game_end_sec // 60 >= 5:
        print(driver.find_element(by="id", value="cps").text)
        break

    elif secs >= 5:
        x0 = x1
        x1 = datetime.now()
        get_highest_item()

driver.quit()
