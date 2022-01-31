from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/"

response = requests.get(URL)
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'lxml')

highest = 0


def get_popular_article(data):
    global highest
    article = []
    if data[2] > highest:
        highest = data[2]
        article = data

        return article


article_tag = soup.select(selector='.titlelink')
article_text = [tag.text for tag in article_tag]
article_link = [tag.get("href") for tag in article_tag]
# just_article = []
# for tag in article_tag:
#     just_article.append((tag.text, tag.get('href')))

article_upvote = [int(tag.text.split()[0]) for tag in soup.select(selector=".score")]
all_articles = list(zip(article_text, article_link, article_upvote))
# all_articles_2 = list(zip(just_article, article_upvote))


# BEST ARTICLE
print(all_articles[article_upvote.index(max(article_upvote))])
# print(all_articles_2[article_upvote.index(max(article_upvote))])

# bad way
# print(list(filter(get_popular_article, all_articles)))


# another way
# article_tag = soup.find_all(name='a', class_='titlelink')
# article_text = [tag.text for tag in article_tag]
# article_link = [tag.get("href") for tag in article_tag]
# article_upvote = [tag.text for tag in soup.find_all(name='span', class_="score")]
# print(article_text)
# print(article_link)
# print(article_upvote)
