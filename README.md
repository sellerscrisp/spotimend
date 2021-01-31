# Spotimend

An application using Spotify's API to learn more about what you listen to on a daily basis.
## Technologies & Resources

Back-end
* [Python](https://github.com/python)
* [Flask](https://flask.palletsprojects.com)
* [Spotify Web API](https://developer.spotify.com/documentation/web-api/reference/)
* [jQuery](https://api.jquery.com/)
* [Postgres](https://postgresql.org)

Front-end
* [Bootstrap v5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
* [Fontawesome](https://fontawesome.com/)
* [Proxima Nova (font)](https://www.marksimonson.com/fonts/view/proxima-nova)

## Installation

```bash
# Initial setup
python -m venv venv
source venv/bin/activate
pip install -r requirement.txt

# Config
export SECRET_KEY='some_secret_key'
export CLIENT_ID='spotify_client_id'
export CLIENT_SECRET='spotify_client_secret'
export FLASK_APP=run
export FLASK_ENV=development

# Start server
flask run # or python run.py
```

### Todo

* Modal/dynamically load track audio features per song
* Store songs and their respective likes
* Song seed recommendations
* Playlist generation
* Database configuration and implementation