import sqlite3 as sql
import string
from typing import Dict, List, Any, Tuple

from flask import Response, flash, redirect, url_for

from app.models import User, Post
from app.queries import UserQueries, PostQueries

def get_user_by_username(db: sql.Connection, form: Dict[str, str]) -> User | None:
    exists = db.execute(UserQueries.GetUserByUsername, [form["username"]]).fetchone()
    return User(*exists) if exists else None

def create_user(db: sql.Connection, user: User) -> int:
    db.execute(UserQueries.CreateUser, [user.username, user.password])
    id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    print(id)
    return 0

def get_user_by_id(db: sql.Connection, id: int) -> User | None:
    exists = db.execute(UserQueries.GetUserById, [id]).fetchone()
    return User(*exists) if exists else None

def get_posts_by_user_id(db: sql.Connection, user_id: int) -> List[Post] | List[Any]:
    posts = db.execute(PostQueries.GetPostsByAuthorId, [user_id]).fetchall()
    return [Post(*post) for post in posts] if posts else []

def is_valid_username(username: str) -> bool:
    for c in username:
        if c not in [*string.ascii_letters, *string.digits]:
            return False
    return True 

def flash_and_redirect(flash_details: Tuple[str, str], redirect_route: str, status_code: int) -> Tuple[Response, int]:
    flash(*flash_details)
    return redirect(url_for(redirect_route)), status_code

__all__ = [
    "get_user_by_username",
    "get_user_by_id",
    "get_posts_by_user_id",
    "is_valid_username",
    "flash_and_redirect"
]