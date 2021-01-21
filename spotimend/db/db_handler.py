from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util.langhelpers import NoneType
from sqlalchemy_utils.functions import database_exists, drop_database

from spotimend.db.models import Song, Like, Dislike, db_name

engine = create_engine(db_name)
SQLAlchemy.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# ------------------------- Database Helper Functions ------------------------ #

def create_db():
    engine = create_engine(db_name)
    SQLAlchemy.metadata.create_all(engine)
    print('Database created!')


def drop_db():
    if database_exists(db_name):
        drop_database(db_name)
        print('Database dropped!')


def reset_db():
    session.query(Song).delete()
    session.query(Like).delete()
    session.query(Dislike).delete()
    session.commit()
    print('Database reset!')


# --------------------------- Song Helper Functions -------------------------- #

def get_song_by_id(id):
    try:
        return session.query(Song).filter_by(id=id).one()
    except:
        return NoneType


def get_all_songs():
    return session.query(Song).all()
