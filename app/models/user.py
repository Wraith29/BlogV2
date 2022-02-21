import sqlite3 as sql
from typing import Dict, Union

from app.queries import PostQueries

class User:
    def __init__(self, id: Union[int, None], username: str, password: str) -> None:
        self.id = id
        self.username = username
        self.password = password

    def get_json(self) -> Dict[str, Union[str, int, None]]:
        return {
            "id": self.id,
            "username": self.username
        }
        
    def number_of_posts(self, db: sql.Connection) -> int:
        posts = db.execute(PostQueries['GetPostsByAuthorId'], [self.id]).fetchall()
        return len(posts)

__all__ = ['User']
