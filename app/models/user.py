class User:
    def __init__(self, id: int | None, username: str, password: str) -> None:
        self.id = id
        self.username = username
        self.password = password

__all__ = ['User']