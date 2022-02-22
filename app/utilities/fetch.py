import sqlite3 as sql
import typing as t

from app.models import User, Post
from app.queries import UserQueries, PostQueries

def get_all_users(db: sql.Connection) -> t.List[User]:
    return [User(*user_data) for user_data in db.execute(UserQueries['GetAllUsers']).fetchall()]

def get_user_by_username(db: sql.Connection, form: t.Dict[str, str]) -> t.Union[User, None]:
    exists = db.execute(UserQueries['GetUserByUsername'], [form["username"]]).fetchone()
    return User(*exists) if exists else None

def get_user_by_id(db: sql.Connection, id: int) -> t.Union[User, None]:
    exists = db.execute(UserQueries['GetUserById'], [id]).fetchone()
    return User(*exists) if exists else None

def get_all_posts(db: sql.Connection) -> t.Union[t.List[Post], None]:
    return [Post(*post_data) for post_data in db.execute(PostQueries['GetAllPosts']).fetchall()]

def get_posts_by_user_id(db: sql.Connection, user_id: int) -> t.Union[t.List[Post], t.List[t.Any]]:
    posts = db.execute(PostQueries['GetPostsByAuthorId'], [user_id]).fetchall()
    return [Post(*post) for post in posts]

__all__ = [
    "get_all_users",
    "get_user_by_username",
    "get_user_by_id",
    "get_posts_by_user_id"
]