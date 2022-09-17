__all__ = ["UserQueries"]

UserQueries = {
    "GetAllUsers": "SELECT id, username, password FROM user",
    "GetUserById": "SELECT id, username, password FROM user WHERE id = ?",
    "GetUserByUsername": "SELECT id, username, password" +
                         "FROM user WHERE username = ?",
    "CreateUser": "INSERT INTO user (username, password) VALUES (?, ?)"
}
