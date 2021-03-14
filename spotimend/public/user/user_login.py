from flask import Blueprint, render_template, redirect, session, flash
from spotimend.utils.models.models import db, connect_db, User
from spotimend.utils.forms.forms import UserForm, RegisterForm, DeleteForm

user_login_blueprint = Blueprint(
    'user_login', __name__, template_folder='templates')


@user_login_blueprint.route('/user-login', methods=['GET', 'POST'])
def user_login():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)
        if user:

            flash(f'Welcome back, {user.username}', 'success')
            session['username'] = user.username
            return redirect('/login')
        else:
            error = 'Invalid username or password'
            flash(error, 'danger')
    return render_template('login.html', form=form)


@user_login_blueprint.route('/user-logout')
def user_logout():
    session.clear()
    return redirect('/')
