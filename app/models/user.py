from typing import Dict


class User:
    def __init__(self, id: int | None, username: str, password: str) -> None:
        self.id = id
        self.username = username
        self.password = password

    def get_json(self) -> Dict[str, str | int | None]:
        return {
            "id": self.id,
            "username": self.username
        }
        
__all__ = ['User']