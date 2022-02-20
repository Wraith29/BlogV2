PostQueries = {
    "GetAllPosts": "SELECT * FROM post",
    "GetPostById": "SELECT * FROM post WHERE id = ?",
    "GetPostsByAuthorId": "SELECT * FROM post WHERE author_id = ?"
}

__all__ = ["PostQueries"]