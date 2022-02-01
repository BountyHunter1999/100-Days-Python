import csv

import requests
from bs4 import BeautifulSoup
import lxml
import os
from dotenv import load_dotenv
import time

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# local
from playlist import Playlist

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
USER_ID = os.getenv("USER_ID")

playlist = Playlist(client_id=SPOTIPY_CLIENT_ID, user_id=USER_ID,
                    secret=SPOTIPY_CLIENT_SECRET, uri=SPOTIPY_REDIRECT_URI)

time_period = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{time_period}/"

response = requests.get(url).text

soup = BeautifulSoup(response, "lxml")

title_tag = soup.find_all(name="h3", class_='a-no-trucate')
titles = [tag.text.strip() for tag in title_tag]

singer_tag = soup.find_all(name="span", class_='a-no-trucate')
singers = [tag.text.strip() for tag in singer_tag]

songs = list(zip(titles, singers))

#  SPOTIFY PART

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-library-read"))

# Create Playlist
playlist_id = playlist.create_playlist(name=f"{time_period} Billboard 100")

# Add track to playlist

song_uri = []
skipped_songs = []
for i in range(len(titles)):
    title = titles[i]
    singer = singers[i]
    query = f"track:{title} artist:{singer}"
    try:
        track = sp.search(q=query, type='track')['tracks']["items"][0]
    except IndexError:
        print("This song doesn't exist in spotify. SKIPPED!")
        skipped_songs.append((title, singer))
    else:
        song_uri.append(track['uri'])

    time.sleep(1)

    print(f"Went through {i + 1} / {100}")

print("ADDING SONGS")
# print(song_uri[:3])
# song_uri = ["spotify:track:1AM1o0mKbgAK5oMpY8B3Z7"]
playlist.add_song_to_playlist(playlist_id=playlist_id, tracks=song_uri)

with open("skipped_songs.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(("SONG", "ARTIST"))
    for song in skipped_songs:
        writer.writerow(song)

print(len(skipped_songs))
