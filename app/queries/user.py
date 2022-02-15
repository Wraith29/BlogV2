class UserQueries:
    GetAllUsers: str       = "SELECT * FROM user"
    GetUserById: str       = "SELECT * FROM user WHERE id = ?"
    GetUserByUsername: str = "SELECT * FROM user WHERE username = ?"

__all__ = ["UserQueries"]