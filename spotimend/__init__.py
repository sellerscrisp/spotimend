import os

from flask import Flask

from config import config_settings

from flask_sqlalchemy import SQLAlchemy
from spotimend.utils.models.models import connect_db

from spotimend.public.index.index import index_blueprint
from spotimend.utils.api.spotify_auth import auth_blueprint
from spotimend.public.profile.profile import profile_blueprint
from spotimend.public.redirect.redirect import redirect_blueprint
from spotimend.public.recents.recents import recents_blueprint
from spotimend.public.favicon.favicon import favicon_blueprint
from spotimend.utils.errors.errors import errors_blueprint
from spotimend.public.user.user_signup import user_signup_blueprint
from spotimend.public.user.user_login import user_login_blueprint

app = Flask(__name__)
db = SQLAlchemy()


def create_app():
    """Create and return app."""

    app.config.from_object(config_settings['development'])
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    app.register_blueprint(index_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(redirect_blueprint)
    app.register_blueprint(recents_blueprint)
    app.register_blueprint(favicon_blueprint)
    app.register_blueprint(errors_blueprint)
    app.register_blueprint(user_signup_blueprint)
    app.register_blueprint(user_login_blueprint)

    db.init_app(app)
    connect_db(app)

    return app
