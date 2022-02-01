import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Playlist:

    def __init__(self, client_id, user_id, secret, uri):
        """

        :param client_id: provided by the spotify dashboard
        :param user_id: ur spotify id, the last part of ur spotify profile url
        :param secret: provided by the spotify dashboard
        :param uri: provided in the spotify dashboard
        """
        self.client_id = client_id
        self.user_id = user_id
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                            client_secret=secret,
                                                            redirect_uri=uri,
                                                            scope="playlist-modify-private"))

    def create_playlist(self, name):
        detail = self.sp.user_playlist_create(user=self.user_id, name=name, public=False)
        return detail["id"]

    def add_song_to_playlist(self, playlist_id, tracks, position=1):
        """ Adds tracks to a playlist

            Parameters:
                - playlist_id - the id of the playlist
                - tracks - a list of track URIs, URLs or IDs
                - position - the position to add the tracks
        """
        self.sp.playlist_add_items(playlist_id=playlist_id, items=tracks)
