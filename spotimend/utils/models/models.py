from enum import unique
from spotimend.utils.api.spotify_handler import SpotifyHandler
import datetime
from operator import contains

from sqlalchemy.sql.sqltypes import Integer
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from sqlalchemy.orm import relation, relationship, backref
from flask import url_for, jsonify
from flask_bcrypt import Bcrypt
from flask import session

bcrypt = Bcrypt()

spotify = SpotifyHandler()

db = SQLAlchemy()

db_name = 'postgres:///spotimend'


class Song(db.Model):
    """Song schema.

    After a song is liked, store song details here.
    """

    __tablename__ = 'song'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
    )

    sp_id = db.Column(
        db.String(22),
        nullable=False,
    )

    date_added = db.Column(DateTime, default=datetime.datetime.utcnow)

    likes = db.Column(
        db.Integer,
        nullable=False,
    )

    def __init__(self, id, sp_id, date_added, likes):
        """"""
        self.id = id
        self.sp_id = sp_id
        self.date_added = date_added
        self.likes = likes

    def __repr__(self):
        return f'<Song {self.sp_id}>'

    def serialize(self):
        return {
            'id': self.id,
            'sp_id': self.sp_id,
            'date_added': self.date_added,
            'likes': self.likes,
        }

    def like_song(self, post):
        """"""


class User(db.Model):

    __tablename__ = "users"

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
        primary_key=True,
    )
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)

    @classmethod
    def register(cls, username, password, email):
        """Register user, set password."""
        hashed = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = cls(
            username=username,
            password=hashed,
            email=email,

        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Validates usrname and password."""

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user
        else:
            return False

    # @classmethod
    # def check_username(cls, username):
    #     """"""

    #     authorization_header = session['authorization_header']
    #     sp_u = spotify.get_user_profile_data(authorization_header)
    #     u = User.query.filter_by(username=username).first()


def connect_db(app):
    """Connect this database to provided Flask app.

    Call this in Flask app.
    """

    db.app = app
    db.create_all()
    db.init_app(app)
