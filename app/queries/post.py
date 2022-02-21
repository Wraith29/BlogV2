PostQueries = {
    "GetAllPosts": "SELECT * FROM post",
    "GetPostById": "SELECT * FROM post WHERE id = ?",
    "GetPostsByAuthorId": "SELECT * FROM post WHERE author_id = ?",
    "CreatePost": "INSERT INTO post (title, content, author_id) VALUES (?, ?, ?)"
}

__all__ = ["PostQueries"]