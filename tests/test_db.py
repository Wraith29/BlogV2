import sqlite3 as sql
from flask import Flask, g
from flask.testing import FlaskCliRunner
from pytest import raises, MonkeyPatch
from app.db import get_db


def test_get_close_db(app: Flask) -> None:
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with raises(sql.ProgrammingError) as e:
        db.execute("SELECT 1")

    assert "closed" in str(e.value)


def test_init_db(runner: FlaskCliRunner, monkeypatch: MonkeyPatch) -> None:
    class Result:
        called = False

    def _fake_init_db() -> None:
        Result.called = True

    monkeypatch.setattr("app.db.init_db", _fake_init_db)
    result = runner.invoke(args=["init-db"])
    assert "Initialised" in result.output
    assert Result.called


def test_get_db_not_sql_connection(app: Flask) -> None:
    with app.app_context():
        g.db = ""

        with raises(ConnectionError) as e:
            get_db()

    assert "Could not connect to" in str(e.value)
