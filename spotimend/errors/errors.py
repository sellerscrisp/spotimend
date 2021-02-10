from flask import Blueprint, request, abort, flash, json, render_template
from spotimend.api.spotify_handler import SpotifyHandler

from werkzeug.exceptions import BadRequestKeyError, HTTPException

spotify = SpotifyHandler()

errors_blueprint = Blueprint('errors', __name__, template_folder='templates')


@errors_blueprint.app_errorhandler(404)
def handle_404(err):
    return render_template('404.html'), 404


@errors_blueprint.app_errorhandler(500)
def handle_500(err):
    return render_template('500.html'), 500
