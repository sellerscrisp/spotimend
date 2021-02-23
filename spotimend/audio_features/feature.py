import requests
from flask import Blueprint, render_template, request, session, url_for
from spotimend.api.spotify_handler import SpotifyHandler

audio_features_blueprint = Blueprint(
    'audio_features',
    __name__,
    template_folder='templates'
)


@audio_features_blueprint.route('/get-features', methods=['GET', 'POST'])
def get_features(song_id):
    """"""
