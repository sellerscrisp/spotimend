import os
from flask import Blueprint, send_from_directory

favicon_blueprint = Blueprint('favicon', __name__)


@favicon_blueprint.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(
        favicon_blueprint.root_path, 'static'
    ),
        'favicon.ico', mimetype='image/vnd.microsoft.icon'
    )
