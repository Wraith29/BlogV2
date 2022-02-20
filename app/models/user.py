from typing import Dict, Union


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
        
__all__ = ['User']
