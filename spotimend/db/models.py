import datetime

from operator import contains
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from sqlalchemy.orm import relation, relationship, backref
from flask import url_for, jsonify

db_name = 'postgres:///spotimend'
db = SQLAlchemy()


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

    likes = relationship('Like')
    dislikes = relationship('Dislike')


class Like(db.Model):
    """Liked schema.

    Store the number of likes in relation to a song's ID.
    """

    __tablename__ = 'liked_song'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
    )

    song_id = db.Column(
        db.String(22),
        db.ForeignKey(
            'song.sp_id',
            ondelete='cascade'
        ),
        nullable=False,
    )

    date_added = db.Column(DateTime, default=datetime.datetime.utcnow)


class Dislike(db.Model):
    """Disliked schema.

    Store the number of dislikes in relation to a song's ID.
    """

    __tablename__ = 'dislike'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
    )

    song_id = db.Column(
        db.String(22),
        db.ForeignKey(
            'song.sp_id',
            ondelete='cascade'
        ),
        nullable=False,
    )

    date_added = db.Column(DateTime, default=datetime.datetime.utcnow)


def connect_db(app):
    """Connect this database to provided Flask app.

    Call this in Flask app.
    """

    db.app = app
    db.init_app(app)
