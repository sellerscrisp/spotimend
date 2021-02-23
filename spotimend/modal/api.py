from spotimend.api.spotify_handler import SpotifyHandler
from flask import Blueprint, request, jsonify, session
import requests
import json

spotify = SpotifyHandler()

modal_api_blueprint = Blueprint(
    'modal_api',
    __name__,
    template_folder='templates'
)


@modal_api_blueprint.route('/feature/song/<song_id>', methods=['GET', 'POST'])
def modal_api(id):
    """"""
    id = request.args['song_id']
    authorization_header = session['authorization_header']

    if request.method == 'GET':
        features_data = spotify.get_single_audio_features_data(
            authorization_header, id)

        return str(features_data)
