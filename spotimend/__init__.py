import os
from flask import Flask
from config import config_settings
# from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
from spotimend.models.models import connect_db
# from flask_login import LoginManager

from spotimend.index.index import index_blueprint
from spotimend.api.spotify_auth import auth_blueprint
from spotimend.profile.profile import profile_blueprint
from spotimend.redirect.redirect import redirect_blueprint
# from spotimend.audio_features.feature import audio_features_blueprint
# from spotimend.modal.api import modal_api_blueprint
from spotimend.recents.recents import recents_blueprint
from spotimend.favicon.favicon import favicon_blueprint
from spotimend.likes.likes import likes_blueprint
from spotimend.errors.errors import errors_blueprint
from spotimend.user.user_signup import user_signup_blueprint
from spotimend.user.user_login import user_login_blueprint


def create_app():
    """Create and return app."""
    app = Flask(__name__)
    db = SQLAlchemy()
    # migrate = Migrate(app, db)
    # manager = Manager(app)
    # login_manager = LoginManager()

    app.config.from_object(config_settings['development'])
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # manager.add_command('db', MigrateCommand)
    # login_manager.init_app(app)

    app.register_blueprint(index_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(redirect_blueprint)
    # app.register_blueprint(audio_features_blueprint)
    # app.register_blueprint(modal_api_blueprint)
    app.register_blueprint(recents_blueprint)
    app.register_blueprint(favicon_blueprint)
    app.register_blueprint(likes_blueprint)
    app.register_blueprint(errors_blueprint)
    app.register_blueprint(user_signup_blueprint)
    app.register_blueprint(user_login_blueprint)

    db.init_app(app)
    connect_db(app)

    return app
