from bs4 import BeautifulSoup
import lxml

with open("website.html") as f:
    contents = f.read()

# print(contents)
soup = BeautifulSoup(contents, 'lxml')  # sometimes html.parser won't work for some sites
# everything appears without any indentation
# print(soup)
# print("---------------After prettify ------------------")
# # now everything is indented properly and easier to read
# print(soup.prettify())

#  get the first anchor tag, or any tag
# print(soup.a)

#  get all the specified tag
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

text_in_a_tag = [tag.getText() for tag in all_anchor_tags]
# print(text_in_a_tag)

href_in_a_tag = [tag.get('href') for tag in all_anchor_tags]
# print(href_in_a_tag)

#  get something with their attributes
heading = soup.find(name="h1", id='name')  # tag name h1 and id name
# print(heading)

section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)
# print(section_heading.text)  # get the text inside the tag
# print(section_heading.name)  # get the name of the tag
# print(section_heading.get('class'))  # get hold of the class attribute

# narrow down using css selectors
company_url = soup.select_one(selector="p a")  # get an `a` tag that sits inside a p tag

# id
name = soup.select_one(selector="#name")
print(name)

# class
print(soup.select(selector='.heading'))
