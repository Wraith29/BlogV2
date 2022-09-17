__all__ = [
    "get_all_users",
    "get_user_by_username",
    "get_user_by_id",
    "get_all_posts",
    "get_posts_by_user_id"
]

import sqlite3 as sql
from app.models import User, Post
from app.queries import UserQueries, PostQueries


def get_all_users(db: sql.Connection) -> list[User]:
    return [
        User(*user_data)
        for user_data
        in db.execute(UserQueries['GetAllUsers']).fetchall()
    ]


def get_user_by_username(
    db: sql.Connection, form: dict[str, str]
) -> User | None:
    exists = db.execute(
        UserQueries['GetUserByUsername'],
        [form["username"]]
    ).fetchone()
    return User(*exists) if exists else None


def get_user_by_id(db: sql.Connection, id: int) -> User | None:
    exists = db.execute(UserQueries['GetUserById'], [id]).fetchone()
    return User(*exists) if exists else None


def get_all_posts(db: sql.Connection) -> list[Post] | None:
    return [
        Post(*post_data)
        for post_data
        in db.execute(PostQueries['GetAllPosts']).fetchall()
    ]


def get_posts_by_user_id(db: sql.Connection, user_id: int) -> list[Post]:
    posts = db.execute(PostQueries['GetPostsByAuthorId'], [user_id]).fetchall()
    return [Post(*post) for post in posts]
