import json
import requests
import os
from flask import Flask, render_template, flash, abort, request, redirect
from urllib.parse import quote

app = Flask(__name__)

# Client keys:
# export CLIENT_ID=qwerty6789
# export CLIENT_SECRET=asdf1234
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

# Spotify URLs
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
API_VERSION = 'v1'
SPOTIFY_API_URL = f'{SPOTIFY_API_BASE_URL}/{API_VERSION}'

# Server side params
CLIENT_SIDE_URL = 'http://127.0.0.1'
PORT = 5000
REDIRECT_URI = f'{CLIENT_SIDE_URL}:{PORT}/callback/q'
SCOPE = 'user-top-read user-read-currently-playing playlist-modify-public user-read-email user-read-recently-played'
STATE = ''
SHOW_DIALOG_BOOLEAN = True
SHOW_DIALOG_STRING = str(SHOW_DIALOG_BOOLEAN).lower()

auth_params = {
    'response_type': 'code',
    'redirect_uri': REDIRECT_URI,
    'scope': SCOPE,
    'state': STATE,
    'show_dialog': SHOW_DIALOG_STRING,
    'client_id': CLIENT_ID,
}


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login')
def login():
    """Auth step 1."""

    url_args = '&'.join(['{}={}'.format(key, quote(val))
                         for key, val in auth_params.items()])
    auth_url = f'{SPOTIFY_AUTH_URL}/?{url_args}'
    return redirect(auth_url)


@app.route('/callback/q')
def callback():
    """Auth step 4."""

    auth_token = request.args['code']
    code_payload = {
        'grant_type': 'authorization_code',
        'code': str(auth_token),
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }

    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # Auth step 5. Tokens returned to app
    response_data = json.loads(post_request.text)
    access_token = response_data['access_token']
    refresh_token = response_data['refresh_token']
    token_type = response_data['token_type']
    expires_in = response_data['expires_in']

    # Auth step 6. Use the access token to access Spotify API
    authorization_header = {"Authorization": f"Bearer {access_token}"}

    # Get profile data
    user_profile_api_endpoint = f'{SPOTIFY_API_URL}/me'
    profile_response = requests.get(
        user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)

    # Get user playlist data
    playlist_api_endpoint = f'{profile_data["href"]}/playlists'
    playlist_response = requests.get(
        playlist_api_endpoint, headers=authorization_header
    )
    playlist_data = json.loads(playlist_response.text)

    # Get top songs
    top_api_endpoint = f'{SPOTIFY_API_URL}/me/top/tracks'
    top_response = requests.get(
        top_api_endpoint, headers=authorization_header
    )
    top_data = json.loads(top_response.text)

    # Combine profile and playlist data to display
    display_arr = [top_data]
    return render_template('index.html', sorted_array=display_arr)


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
