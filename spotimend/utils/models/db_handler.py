from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from spotimend.utils.models.models import Song

# app = Flask(__name__)


# --------------------------- Song Helper Functions -------------------------- #

# def get_song_by_id(id):
#     try:
#         return session.query(Song).filter_by(id=id).one()
#     except:
#         return NoneType


# def get_all_songs():
#     return session.query(Song).all()
