__all__ = ['User']

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class User:
    id: int
    username: str
    password: str

    def get_json(self) -> dict[str, str | int]:
        return {
            "id": self.id,
            "username": self.username
        }
