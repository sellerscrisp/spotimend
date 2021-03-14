from docs.requests.spotify.main import SPOTIFY_API_BASE_URL, SPOTIFY_API_URL
import json
import requests


class SpotifyHandler:
    """Handle spotify requests.
        - get_user_profile_data()
        - get_user_tracks_data(time_range)
        - get_single_audio_features_data(song_id)
        - get_currently_playing_data()
        - get_recently_played_data()
        - skip, play, pause, and resume user playback
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
        curr = json.loads(requests.get(
            user_curr_playing_endpoint, headers=auth_header).text)
        curr = curr

        curr_data = []

        curr_data.append({
            'track_artist': curr['item']['artists'][0]['name'],
            'track_name': curr['item']['name'],
            'track_id': curr['item']['id'],
            'track_img': curr['item']['album']['images'][0]['url'],
            # 'track_url': curr['external_urls']['spotify'],
            # 'track_preview': curr['preview_url'],
        })

        return curr_data

    def refresh_data():
        """"""

        curr_data = []
        curr_data.clear()

    def post_next_track(self, auth_header):
        """Skip user playback to next track."""

        next_track_endpoint = f'{self.SPOTIFY_API_URL}/me/player/next'
        next_track = requests.post(next_track_endpoint, headers=auth_header)

        return next_track

    def post_previous_track(self, auth_header):
        """Skip user playback to previous track."""

        previous_track_endpoint = f'{self.SPOTIFY_API_URL}/me/player/previous'
        previous_track = requests.post(
            previous_track_endpoint,
            headers=auth_header
        )

        return previous_track

    def post_pause_track(self, auth_header):
        """Pause user playback."""

        pause_track_endpoint = f'{self.SPOTIFY_API_URL}/me/player/pause'
        pause_track = requests.post(
            pause_track_endpoint,
            header=auth_header
        )

        return pause_track

    def play_track(self, auth_header):
        """Resume user playback."""

        play_track_endpoint = f'{self.SPOTIFY_API_URL}/me/player/play'
        play_track = requests.post(
            play_track_endpoint,
            header=auth_header
        )

        return play_track

    def get_recently_played_data(self, auth_header):
        """Get user's recently played songs.

        From the 6 most recently played songs on a user's profile.
        """

        user_recently_played_endpoint = f'{self.SPOTIFY_API_URL}/me/player/recently-played?limit=20'
        recently_played = json.loads(requests.get(
            user_recently_played_endpoint, headers=auth_header).text)
        recently_played = recently_played['items']

        recently_data = []

        for track in recently_played:
            recently_data.append({
                'artist_name': track['track']['artists'][0]['name'],
                'track_name': track['track']['name'],
                'track_img': track['track']['album']['images'][0]['url'],
                'track_popularity': track['track']['popularity'],
                'track_uri': track['track']['uri'],
            })

        return recently_data
