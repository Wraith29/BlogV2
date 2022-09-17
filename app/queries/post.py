__all__ = ["PostQueries"]

PostQueries = {
    "GetAllPosts": "SELECT id, title, body, author_id FROM post",
    "GetPostById": "SELECT id, title, body, author_id FROM post WHERE id = ?",
    "GetPostsByAuthorId": "SELECT id, title, body, author_id" +
                          "FROM post WHERE author_id = ?",
    "CreatePost": "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)"
}
