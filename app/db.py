import sqlite3 as sql
from typing import Any, Optional

import click
from flask import Flask, current_app, g
from flask.cli import with_appcontext

from app.queries import UserQueries

def get_db() -> sql.Connection | Any:
    if "db" not in g:
        g.db = sql.connect(
            current_app.config["DATABASE"], 
            detect_types=sql.PARSE_DECLTYPES
        )
        g.db.row_factory = sql.Row

    return g.db

def close_db(_: Optional[BaseException] | None) -> None:
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db() -> None:
    db = get_db()
    with current_app.open_resource("schema.sql", mode="r") as f:
        db.executescript(f.read())

@click.command("init-db")
@with_appcontext  # type: ignore
def init_db_command() -> None:
    init_db()
    click.echo("Initialised Database")

@click.command("list-users")
@with_appcontext # type: ignore
def list_users_command() -> None:
    users = get_db().execute(UserQueries['GetAllUsers']).fetchall()
    for user in users:
        print(user)

def init_app(app: Flask) -> None:
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(list_users_command)