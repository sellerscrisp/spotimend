import os
import responses
import requests

from spotimend import create_app, app
from flask import url_for, request
from sqlalchemy.exc import IntegrityError
from unittest import TestCase, mock

import spotimend.utils.api.spotify_auth
from spotimend.utils.api.spotify_client import SpotifyClient
from spotimend.utils.api.spotify_handler import SpotifyHandler


app.config['WTF_CSRF_ENABLED'] = False
app.config["DEBUG_TB_ENABLED"] = False
os.environ['DATABASE_URL'] = 'postgresql:///spotimendtest'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///spotimendtest'
os.environ['SECRET_KEY'] = 'reallygreatkeyyoucanthackme'
client_id = '3036c8e857dc4647831a52ff2a368b06'
client_secret = '905526d5c99c4f5589c48e77f21d599f'

create_app()

sc = SpotifyClient(
    client_id=client_id,
    client_secret=client_secret,
    client_side_url='127.0.0.1',
    port=5000
)
sh = SpotifyHandler()


class SpotifyAPITests(TestCase):
    """Test Spotify's API."""

    def setUp(self):
        """"""
        os.environ['CLIENT_ID'] = client_id
        os.environ['CLIENT_SECRET'] = client_secret

    def test_environment_vars(self):
        """Test that spotify auth works."""

        self.assertEqual(os.environ['CLIENT_ID'], client_id)
        self.assertEqual(os.environ['CLIENT_SECRET'], client_secret)
