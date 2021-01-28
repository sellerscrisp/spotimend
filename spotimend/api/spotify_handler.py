from docs.requests.spotify.main import SPOTIFY_API_BASE_URL, SPOTIFY_API_URL
import json
import requests


class SpotifyHandler:
    """Handle spotify requests.

        - get_user_profile_data()
        - get_user_tracks_data(time_range)
        - get_single_audio_features_data(song_id)
        - get_currently_playing_data()
        - get_recently_played_data
    """

    API_VERSION = 'v1'
    SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
    SPOTIFY_API_URL = f'{SPOTIFY_API_BASE_URL}/{API_VERSION}'

    def get_user_profile_data(self, auth_header):
        """Get user profile information."""

        user_profile_endpoint = f'{self.SPOTIFY_API_URL}/me'
        profile = requests.get(user_profile_endpoint, headers=auth_header).text
        return json.loads(profile)

    def get_user_tracks_data(self, auth_header, time_range):
        """Get user's top 30 tracks.

        Return a list of track data.
        """

        user_tracks_endpoint = f'{self.SPOTIFY_API_URL}/me/top/tracks?time_range={time_range}&limit=20'
        tracks = json.loads(requests.get(
            user_tracks_endpoint, headers=auth_header).text)
        tracks = tracks['items']

        track_data = []

        for track in tracks:
            track_data.append({
                'artist_name': track['album']['artists'][0]['name'],
                'artist_id': track['album']['artists'][0]['id'],
                'artist_uri': track['artists'],
                # 'artist_url': track['artists']['external_urls']['spotify'],
                'track_name': track['name'],
                'track_id': track['id'],
                'track_uri': track['uri'],
                'track_id': track['id'],
                # 'track_url': track['external_urls']['spotify'],
                'track_img': track['album']['images'][0]['url'],
                'track_popularity': track['popularity']
                # 'track_preview': track['preview_url'],
            })
        return track_data

    def get_single_audio_features_data(self, auth_header, song_id):
        """Get audio features for a single track.

        Return a list of a song's audio features. Uses the song's id
        as an input.
        """

        # single_audio_features_endpoint = f'{self.SPOTIFY_API_URL}/audio-features/{song_id}'
        single_audio_features_endpoint = f'{self.SPOTIFY_API_URL}/audio-features/{song_id}'
        audio_features = requests.get(
            single_audio_features_endpoint, headers=auth_header)
        audio_features = audio_features

        audio_features_data = []

        for feature in audio_features:
            audio_features_data.append({
                'danceability': feature[0],
                'energy': feature[1],
                # 'loudness': feature['loudness'],
                # 'speechiness': feature['speechiness'],
                # 'acousticness': feature['acousticness'],
                # 'instrumentalness': feature['instrumentalness'],
                # 'tempo': feature['tempo'],
                # 'uri': feature['uri'],
            })
        return audio_features_data

    def get_currently_playing_data(self, auth_header):
        """Get user's currently playing song.

        Returns a list of data regarding the user's currently playing song.
        """

        user_curr_playing_endpoint = f'{self.SPOTIFY_API_URL}/me/player/currently-playing?market=US'
        curr_playing = json.loads(requests.get(
            user_curr_playing_endpoint, headers=auth_header).text)
        curr_playing = curr_playing[1]['item']

        curr_data = []

        for curr in curr_playing:
            curr_data.append({
                # 'track_img': curr['album']['images'][0]['url'],
                # 'track_artist': curr['artists']['name'],
                # 'track_name': curr['name'],
                # 'track_id': curr['id'],
                'track_uri': curr['uri'],
                # 'track_url': curr['external_urls']['spotify'],
                # 'track_preview': curr['preview_url'],
            })
        return curr_data

    def get_recently_played_data(self, auth_header):
        """Get user's recently played songs.

        From the 6 most recently played songs on a user's profile.
        """

        user_recently_played_endpoint = f'{self.SPOTIFY_API_URL}/me/player/recently-played?limit=10'
        recently_played = json.loads(requests.get(
            user_recently_played_endpoint, headers=auth_header).text)
        recently_played = recently_played['items']

        recently_data = []

        for track in recently_played:
            recently_data.append({
                'artist_name': track['track']['album']['artists'][0]['name'],
            })

        return recently_data
