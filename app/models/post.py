__all__ = ["Post"]

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Post:
    id: int | None
    title: str
    body: str
    author_id: int
