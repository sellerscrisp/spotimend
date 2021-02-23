import os

from spotimend.models.models import User
from spotimend import create_app, app
from spotimend.models.models import db

from flask import url_for, request
from sqlalchemy.exc import IntegrityError
from unittest import TestCase


app.config['WTF_CSRF_ENABLED'] = False
app.config["DEBUG_TB_ENABLED"] = False
os.environ['DATABASE_URL'] = 'postgresql:///spotimendtest'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///spotimendtest'
os.environ['SECRET_KEY'] = 'reallygreatkeyyoucanthackme'

create_app()


class UserTests(TestCase):
    """Test user views/models."""

    def setUp(self):
        """Create test client and sample data."""

        db.create_all()

        User.query.delete()

        user1 = User(
            username='test1',
            password='PASSWORD',
            email='test1@test.com'
        )

        user2 = User(
            username='test2',
            password='PASSWORD',
            email='test2@test.com'
        )

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

        self.app = app
        self.client = self.app.test_client()
        self.user1 = user1
        self.user2 = user2
        self.email1 = user1.email
        self.email2 = user2.email

    def tearDown(self):
        """Clean up test db."""

        db.session.rollback()
        registered_user = User(
            username='jamesbond',
            password='jamesbond',
            email='james@bond.com'
        )
        db.session.add(registered_user)
        db.session.commit()

    def test_login_success(self):
        """Tests that the login form is rendered and can login a user"""
        with self.client:

            res = self.client.get('/user-login')
            # html = res.get_data(as_text=True)

            login_data = {
                'username': self.user1,
                'password': 'PASSWORD',
            }

            res = self.client.post(
                '/user-login',
                data=login_data,
            )
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)

    def test_login_failure(self):
        """Tests that user is redirected to spotify auth page."""

        res = self.client.get('/user-login')

        wrong_data = {
            'username': 'dne',
            'password': 'PASSWORD1234',
        }

        res = self.client.post(
            '/user-login',
            data=wrong_data,
            follow_redirects=True,
        )
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('form method="POST"', html)
        self.assertIn('<p class="mb-0">Invalid username or password</p>', html)

    def test_signup_success(self):
        """Tests that a user can successfully register"""

        user = User.register(
            username='new_user',
            password='new_password',
            email='email@email.com',
        )

        db.session.add(user)
        db.session.commit()

        self.assertEqual(user.username, 'new_user')
        self.assertEqual(user.email, 'email@email.com')

    def test_signup_failure(self):
        """Tests that email and username must be unique."""

        res = self.client.get('/user-signup')

        signup_data = {
            'username': self.user1,
            'password': 'PASSWORD',
            'email': self.email2,
        }

        res = self.client.post(
            '/user-signup',
            data=signup_data,
            follow_redirects=True,
        )

        self.assertEqual(res.status_code, 200)
        self.assertRaises(IntegrityError)

    def test_authentication_redirect_success(self):
        """Tests authentication of a user with valid credentials."""

        res = self.client.get('/login')

        user = User.register(
            username='new_user',
            email='email@newuser.com',
            password='passw0rd',
        )

        db.session.commit()

        user_data = User.authenticate(
            username=user.username,
            password=user.password,
        )

        res = self.client.post('/login', data=user_data)

        self.assertEqual(res.status_code, 302)
        self.assertTrue(user)
        self.assertEqual(user.username, 'new_user')
        self.assertTrue(user.password)
