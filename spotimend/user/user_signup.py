from flask import Blueprint, render_template, redirect, session, flash, request
from spotimend.models.models import db, connect_db, User
from spotimend.forms.forms import UserForm, RegisterForm, DeleteForm
from sqlalchemy import exc


user_signup_blueprint = Blueprint(
    'user_signup', __name__, template_folder='templates')


@user_signup_blueprint.route('/user-signup', methods=['GET', 'POST'])
def user_signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        try:
            username = form.username.data
            password = form.password.data
            email = form.email.data
            user = User.register(username, password, email)
            db.session.add(user)
            db.session.commit()

            session['username'] = user.username
            return redirect('/login')
        except exc.IntegrityError:
            flash('Username or email address has already been taken.')

    return render_template('signup.html', form=form)