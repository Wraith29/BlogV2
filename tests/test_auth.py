from flask import Flask, session
from flask.testing import FlaskClient
from tests.conftest import AuthActions
from app.db import get_db
from app.utilities.fetch import get_user_by_username


def test_register(auth: AuthActions, app: Flask) -> None:
    username = "Isaac2"
    password = "password"
    with app.app_context():
        assert get_user_by_username(get_db(), username) is None
        assert auth.register(username, password).status_code == 302
        assert get_user_by_username(get_db(), username) is not None


def test_login(app: Flask, auth: AuthActions) -> None:
    username = "Isaac"
    password = "password"
    with app.app_context():
        assert get_user_by_username(get_db(), username) is not None
        assert auth.login(username, password).status_code == 302


def test_logout(client: FlaskClient, auth: AuthActions) -> None:
    with client:
        assert auth.logout().status_code == 302
        assert "current_user" not in session
