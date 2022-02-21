import sqlite3 as sql
import typing as t

from app.queries import PostQueries

class User:
    def __init__(self, id: t.Union[int, None], username: str, password: str) -> None:
        self.id = id
        self.username = username
        self.password = password

    def get_json(self) -> t.Dict[str, t.Union[str, int, None]]:
        return {
            "id": self.id,
            "username": self.username
        }
        
    def number_of_posts(self, db: sql.Connection) -> int:
        posts = db.execute(PostQueries['GetPostsByAuthorId'], [self.id]).fetchall()
        return len(posts)

__all__ = ['User']
