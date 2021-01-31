from spotimend.recents.recents import recents
from flask import Blueprint, render_template, request, redirect, url_for, session

redirect_blueprint = Blueprint(
    'redirect', __name__, template_folder='templates')


@redirect_blueprint.route('/redirect', methods=['GET', 'POST'])
def redirect():
    """Redirect to /profile

    TODO: 
     - Create a redirect on each page change for better load times
     - Implement page caching
    """

    if request.method == 'GET':
        return render_template('redirect.html')
