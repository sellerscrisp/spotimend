"""Spotipy usage.

Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy
you get full access to all of the music data provided by the Spotify platform.
"""

from flask import (
    Flask, flash, redirect, render_template, request, url_for, session
)
import spotipy
from spotipy import oauth2
import config

app = Flask(__name__)

"""Required for auth.
env variables:
    - export SPOTIPY_CLIENT_ID='your-spotify-client-id'
    - export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
    - export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
"""

# Scopes allow third party apps to display what information will be gathered
# 'user-read-email' could potentially be useful for db
SCOPE = 'user-top-read user-read-currently-playing playlist-modify-public user-read-email user-read-recently-played'
# Cache requests to limit load on Spotify's API service
CACHE = '.spotifycache'
# Reads client id and client secret from env variables
spotify_oauth = oauth2.SpotifyOAuth(scope=SCOPE, cache_path=CACHE)


@app.route('/login', methods=['GET'])
def login():
    token = spotify_oauth.get_cached_token()
    # check if auth token is expired
    if token and not spotify_oauth.is_token_expired(token):
        access_token = token['access_token']
        session['access_token'] = access_token
        # some jinja template to render top tracks
        return redirect('/top_tracks')
    # if auth token isn't expired use session's auth token
    else:
        login_url = spotify_oauth.get_authorize_url()
        return redirect(login_url)


@app.route('/oauth/callback', methods=['GET'])
def spotify_redirect():
    """Callback function for Spotify's redirect after code generation"""

    code = request.args['code']
    token = spotify_oauth.get_access_token(code)
    access_token = token['access_token']
    session['access_token'] = access_token
    return redirect('/top_tracks')


@app.route('/top_tracks', methods=['GET'])
def top_tracks():
    access_token = session['access_token']
    spotify_api = spotipy.Spotify(access_token)
    option = request.args['time_range']
    result = spotify_api.current_user_top_tracks(time_range=option)

    all_results = []
    for track in result['items']:
        top_track = {}
        top_track['artist_name'] = track['artists'][0]['name']
        top_track['track_name'] = track['name']
        top_track['album_name'] = track['album']['name']
        top_track['album_image'] = track['album']['images'][0]['url']
        top_track['track_id'] = track['id']
        all_results.append(top_track)
    return render_template('top_tracks.html', top_tracks=all_results)


@app.route('/currently_playing', methods=['GET'])
def currently_playing():
    access_token = session['access_token']
    spotify_api = spotipy.Spotify(access_token)
    result = spotify_api.current_user_top_tracks()

    current_playing = {}
    result = spotify_api.current_user_playing_track()
    if result:
        current_song_result = result['item']
        current_playing['song'] = current_song_result['name']
        current_playing['image'] = current_song_result['album']['images'][0]['url']
        current_playing['artist'] = current_song_result['artists'][0]['name']
    return render_template('currently_playing.html', current_playing=current_playing)


@app.route('/currently_playing', methods=['GET'])
def currently_playing():
    access_token = session['access_token']
    spotify_api = spotipy.Spotify(access_token)
    result = spotify_api.current_user_top_tracks()
