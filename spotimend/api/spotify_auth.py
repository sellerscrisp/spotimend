import os
from flask import Blueprint, request, redirect, url_for, session

from spotimend.api.spotify_client import SpotifyClient

auth_blueprint = Blueprint('auth', __name__)

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

client = SpotifyClient(client_id, client_secret, port=5000)


@auth_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    """Redirect to spotify's login."""

    auth_url = client.get_auth_url()
    return redirect(auth_url)


@auth_blueprint.route('/callback/q')
def callback():
    """Callback and setting session's auth header."""

    token = request.args['code']
    client.get_auth(token)
    authorization_header = client.authorization_header
    session['authorization_header'] = authorization_header
    return redirect(url_for('redirect.redirect'))
