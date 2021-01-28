import os
from flask import Flask

from spotimend.views.views import blueprint
from spotimend.index.index import index_blueprint
from spotimend.api.spotify_auth import auth_blueprint
from spotimend.profile.profile import profile_blueprint
from spotimend.redirect.redirect import redirect_blueprint
from spotimend.audio_features.feature import audio_features_blueprint
from spotimend.modal.api import modal_api_blueprint
from spotimend.recents.recents import recents_blueprint
from spotimend.favicon.favicon import favicon_blueprint


def create_app():
    """Create and return app."""

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    app.register_blueprint(blueprint)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(redirect_blueprint)
    app.register_blueprint(audio_features_blueprint)
    app.register_blueprint(modal_api_blueprint)
    app.register_blueprint(recents_blueprint)
    app.register_blueprint(favicon_blueprint)

    return app
