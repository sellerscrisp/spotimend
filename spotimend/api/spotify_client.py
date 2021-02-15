from docs.requests.spotify.main import CLIENT_SIDE_URL
import requests
import json
from urllib.parse import quote


class SpotifyClient:
    """"""

    # API URL Constants
    API_VERSION = 'v1'
    SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
    SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
    SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
    SPOTIFY_API_URL = f'{SPOTIFY_API_BASE_URL}/{API_VERSION}'

    # Server-side params
    STATE = ''
    SHOW_DIALOG_BOOL = True
    SHOW_DIALOD_STR = str(SHOW_DIALOG_BOOL).lower()
    SCOPE = 'user-top-read user-read-currently-playing playlist-modify-public user-read-recently-played'

    # Client-side params for callback & auth
    CLIENT_SIDE_URL = 'https://spotimend.crisp.pw'

    def __init__(self, client_id, client_secret, client_side_url=CLIENT_SIDE_URL, port=None):
        """"""

        self.client_id = client_id
        self.client_secret = client_secret
        self.client_side_url = client_side_url
        self.port = port
        self._access_token = ''
        self.authorization_header = ''
        self.redirect_uri = f'{self.client_side_url}/callback/q' if port is None else f'{self.client_side_url}:{self.port}/callback/q'

    def get_auth_url(self):
        """Get the authorization URL."""

        auth_query_params = {
            'response_type': 'code',
            'redirect_uri': self.redirect_uri,
            'scope': self.SCOPE,
            'show_dialog': self.SHOW_DIALOD_STR,
            'client_id': self.client_id,
            # 'state': STATE,
        }

        url_args = '&'.join(
            [f'{key}={quote(str(val))}' for key, val in auth_query_params.items()])
        return f'{self.SPOTIFY_AUTH_URL}/?{url_args}'

    def get_auth(self, auth_token):
        """Get the authorization params for header."""

        data = {
            'grant_type': 'authorization_code',
            'code': str(auth_token),
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        post_request = requests.post(self.SPOTIFY_TOKEN_URL, data=data)

        response_data = json.loads(post_request.text)
        self._access_token = response_data['access_token']
        self.authorization_header = {
            "Authorization": f"Bearer {self._access_token}"}

        return dict(
            access_token=response_data['access_token'],
            refresh_token=response_data['refresh_token'],
            token_type=response_data['token_type'],
            expires_in=response_data['expires_in'],
        )
