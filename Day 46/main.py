import requests
from bs4 import BeautifulSoup
import lxml
import os
from dotenv import load_dotenv

import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

URL = "https://www.billboard.com/charts/hot-100/1999-03-06/"

response = requests.get(URL).text

soup = BeautifulSoup(response, "lxml")

# print(soup.prettify())
song_title = soup.find(name="h3", class_='c-title').text.strip()
song_singer = soup.find(name="span", class_='a-no-trucate').text.strip()
song_ranking = soup.find(name="span", class_='c-label').text.strip()

title_tag = soup.find_all(name="h3", class_='c-title')
titles = [tag.text.strip() for tag in title_tag]

singer_tag = soup.find_all(name="span", class_='a-no-trucate')
singers = [tag.text.strip() for tag in singer_tag]

rank_tag = soup.find_all(name="span", class_='c-label')
ranks = [tag.text.strip() for tag in rank_tag]

songs = list(zip(ranks, titles, singers))

#  SPOTIFY PART

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-library-read"))


gr_uri = "spotify:artist:7tjbDPvrdvDshcpEMXKRVb"  # url end part
results = sp.artist_top_tracks(gr_uri)

for track in results['tracks'][:10]:
    print(f'Track   : {track["name"]}')
    print(f'Audio   : {track["preview_url"]}')
    print(f'Cover art   : {track["album"]["images"][0]["url"]}')
    print()

