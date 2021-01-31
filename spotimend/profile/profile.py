import json
import requests
from flask import Blueprint, render_template, session, redirect, url_for, request
from spotimend.api.spotify_handler import SpotifyHandler

profile_blueprint = Blueprint('profile', __name__, template_folder='templates')

spotify = SpotifyHandler()


@profile_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    authorization_header = session['authorization_header']

    def extract_letters(str):
        return ''.join([letter for letter in str if not letter.isdigit()])

    # if request.method == 'POST':

    if request.method == 'GET':
        profile_data = spotify.get_user_profile_data(
            authorization_header
        )

        # user_display_name, user_id = profile_data_test['display_name'], profile_data_test['id']
        # session['user_id'], session['user_display_name'] = user_id, user_display_name

        top_tracks_short = spotify.get_user_tracks_data(
            authorization_header,
            time_range='short_term'
        )

        top_tracks_medium = spotify.get_user_tracks_data(
            authorization_header,
            time_range='medium_term'
        )

        return render_template(
            'profile.html',
            profile_data=profile_data,
            top_tracks_short=top_tracks_short,
            top_tracks_medium=top_tracks_medium,
            func=extract_letters,
        )

    return render_template('profile.html')
