from typing import Union


class Post:
    def __init__(self, id: Union[int, None], title: str, content: str, author_id: int) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id

__all__ = ["Post"]
