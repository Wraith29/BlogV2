from typing import Generator
from pytest import fixture
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
from app import create_app


@fixture()
def app() -> Generator[Flask]:
    app = create_app()
    app.config.update({
        "UPDATE": True
    })

    yield app


@fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@fixture()
def runner(app: Flask) -> FlaskCliRunner:
    return app.test_cli_runner()
