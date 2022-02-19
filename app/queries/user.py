class UserQueries:
    GetAllUsers: str       = "SELECT * FROM user"
    GetUserById: str       = "SELECT * FROM user WHERE id = ?"
    GetUserByUsername: str = "SELECT * FROM user WHERE username = ?"
    CreateUser: str        = "INSERT INTO user (username, password) VALUES (?, ?)"

__all__ = ["UserQueries"]