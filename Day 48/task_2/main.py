from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "../chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(URL)

print(driver.find_element(by="css selector", value='#articlecount a').text)

driver.quit()
