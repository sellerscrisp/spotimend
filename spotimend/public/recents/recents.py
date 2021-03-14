import json
import requests
from flask import Blueprint, render_template, session, url_for, request, redirect, flash
from spotimend.utils.api.spotify_handler import SpotifyHandler


recents_blueprint = Blueprint('recents', __name__, template_folder='templates')
spotify = SpotifyHandler()


@recents_blueprint.route('/recents', methods=['GET', 'POST'])
def recents():
    """"""
    try:
        authorization_header = session['authorization_header']
    except:
        flash('Your session expired so we asked you to login again.', 'success')
        return redirect('/login')

    if request.method == 'GET':
        profile_data = spotify.get_user_profile_data(
            authorization_header
        )

        user_display_name, user_id = profile_data['display_name'], profile_data['id']
        session['user_id'], session['user_display_name'] = user_id, user_display_name

        recently_played = spotify.get_recently_played_data(
            authorization_header
        )
        try:
            curr_playing = spotify.get_currently_playing_data(
                authorization_header
            )
        except ValueError:
            curr_playing = {}
            flash(
                'No song currently playing.', 'warning')

        return render_template(
            'recents.html',
            profile_data=profile_data,
            user_display_name=user_display_name,
            recently_played=recently_played,
            curr_playing=curr_playing,
        )

    return render_template('recents.html')


@recents_blueprint.route('/recents/next', methods=['GET', 'POST'])
def next_track():
    """"""

    authorization_header = session['authorization_header']

    # if request.method == 'GET':
    spotify.post_next_track(authorization_header)

    return redirect('/recents')
