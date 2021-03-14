from flask import Blueprint, render_template, url_for
from spotimend.utils.api.spotify_auth import login

index_blueprint = Blueprint('index', __name__, template_folder='templates')


@index_blueprint.route('/')
def index():
    return render_template('index.html')
