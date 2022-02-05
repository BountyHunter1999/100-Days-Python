from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "./chromedriver"

ser = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser)

URL = "https://www.amazon.com/Lenovo-Legion-Pro-Gaming-GeForce/dp/B09923Z7MN/ref=sr_1_2?crid=213MST8LR84ST&keywords=" \
      "lenovo+legion+5+pro&qid=1643780869&sprefix=lenevo+legion+5+pro%2Caps%2C492&sr=8-2"

# Open the particular url in chrome
# driver.get("https://www.amazon.com")
driver.get(URL)

# no need to provide the header as we did in day 47
price = driver.find_element(by="css selector", value=".apexPriceToPay")
print(price.text)

image = driver.find_element(by="css selector", value="#landingImage")
print(image.size)

price = driver.find_element(by="xpath", value="//*[@id='corePrice_desktop']/div/table/tbody/tr[2]/td[2]/span[1]/span[2]")
print(price.text)


# close a single active tab
# driver.close()

# quit the entire browser
driver.quit()
