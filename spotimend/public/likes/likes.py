from flask import Blueprint, request, abort, flash
import requests
from spotimend.utils.models.models import Song, db

likes_blueprint = Blueprint('likes', __name__)


def save_song():
    sp_id = request.args()


@likes_blueprint.route('/likes/toggle_like/<song_id>', methods=['POST'])
def toggle_like(song_id):
    """"""

    song = Song.query.get(song_id)

    db.session.add()
