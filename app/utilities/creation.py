import sqlite3 as sql

from app.models import User, Post
from app.queries import UserQueries, PostQueries

def create_user(db: sql.Connection, user: User) -> int:
    db.execute(UserQueries['CreateUser'], [user.username, user.password])
    db.commit()
    id = int(db.execute("SELECT last_insert_rowid()").fetchone()[0])
    return id

def create_post(db: sql.Connection, post: Post) -> int:
    db.execute(PostQueries['CreatePost'], [post.title, post.body, post.author_id])
    db.commit()
    id = int(db.execute("SELECT last_insert_rowid()").fetchone()[0])
    return id

__all__ = [
    "create_user",
    "create_post"
]