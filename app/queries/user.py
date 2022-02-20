UserQueries = {
    "GetAllUsers": "SELECT * FROM user",
    "GetUserById": "SELECT * FROM user WHERE id = ?",
    "GetUserByUsername": "SELECT * FROM user WHERE username = ?",
    "CreateUser": "INSERT INTO user (username, password) VALUES (?, ?)"
}

__all__ = ["UserQueries"]