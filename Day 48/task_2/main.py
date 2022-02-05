from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "../chromedriver"

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

URL = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(URL)

count = driver.find_element(by="css selector", value='#articlecount a')
print(count.text)

# Clicking there
# count.click()

# as we click on links often we can do something like this too
all_portals = driver.find_element(by="link text", value="All portals")
# all_portals.click()

search = driver.find_element(by="name", value="search")
search.send_keys("Python")

# if we want to send a key that's not a letter or one of the numbers or symbols, line 3
search.send_keys(Keys.ENTER)

# driver.quit()
