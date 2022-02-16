import sqlite3 as sql
from typing import Dict

from app.models import User
from app.queries import UserQueries

def get_user_by_username(db: sql.Connection, form: Dict[str, str]) -> User | None:
    exists = db.execute(UserQueries.GetUserByUsername, [form["username"]]).fetchone()
    return User(*exists) if exists else None
