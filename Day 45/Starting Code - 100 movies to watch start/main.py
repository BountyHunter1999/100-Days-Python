import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL).text

soup = BeautifulSoup(response, 'lxml')

title_tags = soup.find_all(name='h3', class_="title")
titles = [tag.text.strip() for tag in title_tags][::-1]

with open("top_100_movies_of_all_time.txt", "w") as f:
    for line in titles:
        f.write(line + "\n")

