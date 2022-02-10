import requests

URL = "https://api.npoint.io/81be5fc04cd37384ad3a"


class Post:

    def __init__(self):
        self.data = requests.get(URL).json()
        self.amount = len(self.data)

    def get_post(self, index):
        return self.data[index]

    def get_posts(self):
        return self.data

p = Post()
print(p.amount)

