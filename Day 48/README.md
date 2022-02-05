# Essentials

1. [Chrome](https://www.google.com/chrome/)
2. [Check the version of the chrome u have](chrome://settings/help)
3. [Download the version of webdriver for that specific chrome version](https://chromedriver.chromium.org/downloads)
4. unzip the file and get that file **(full path)** in `main.py` as `chrome_driver_path`
5. Install selenium:  `pipenv install selenium`

# Tasks


## Task_1
- Scraped upcoming events from python.org (`by="css selector"`)
- got the events on a nested dictionary using dict comprehension

## Task_2
- count the no. of article in wikipedia main page (`by="css selector"`)
- used link name to travel to other pages `by="link text", value="All portals")`
- also used the search and pressed entered automatically 
    - `(by="name", value="search")`
    - `send_keys(Keys.ENTER)`

## Task_3
- filled a form (first name, last name, and email) (`by="name"`)
- clicked a button (`by="xpath"`)

## Task_4
