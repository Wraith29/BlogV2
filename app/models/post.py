import typing as t

class Post:
    def __init__(self, id: t.Union[int, None], title: str, body: str, author_id: int) -> None:
        self.id = id
        self.title = title
        self.body = body
        self.author_id = author_id
    
__all__ = ["Post"]
