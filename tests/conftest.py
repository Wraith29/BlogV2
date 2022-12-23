__all__ = ["AuthActions"]

from abc import ABC
import os
import tempfile
from pytest import fixture
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
from werkzeug.test import TestResponse
from app import create_app
from app.db import get_db, init_db


class Actions(ABC):
    def __init__(self, client: FlaskClient) -> None:
        self._client = client


class AuthActions(Actions):
    def login(
        self, username: str = "Isaac", password: str = "password"
    ) -> TestResponse:
        return self._client.post(
            "/auth/login/login",
            data={"username": username, "password": password}
        )

    def register(
        self, username: str = "Isaac", password: str = "password"
    ) -> TestResponse:
        return self._client.post(
            "/auth/register/register",
            data={"username": username, "password": password}
        )

    def logout(self) -> TestResponse:
        return self._client.get("/auth/logout")


class CreateActions(Actions):
    def create_post(self, title: str, body: str) -> TestResponse:
        return self._client.post(
            "/post/create",
            data={"title": title, "body": body}
        )


@fixture
def app() -> Flask:
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        "TESTING": True,
        "DATABASE_URI": db_path
    })

    with open(os.path.join(os.path.dirname(__file__), "data.sql"), "r") as f:
        _data = f.read()

    with app.app_context():
        init_db()
        get_db().executescript(_data)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@fixture
def runner(app: Flask) -> FlaskCliRunner:
    return app.test_cli_runner()


@fixture
def auth(client: FlaskClient) -> AuthActions:
    return AuthActions(client)
