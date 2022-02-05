from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "../chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

URL = "https://secure-retreat-92358.herokuapp.com/"

driver.get(URL)

fname = driver.find_element(by="name", value="fName")
fname.send_keys("LOL")

lname = driver.find_element(by="name", value="lName")
lname.send_keys("UFF")

email = driver.find_element(by="name", value="email")
email.send_keys("email@emai.com")

button = driver.find_element(by="xpath", value="/html/body/form/button")
button.click()

