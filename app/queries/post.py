class PostQueries:
    GetAllPosts: str = "SELECT * FROM post"
    GetPostById: str = "SELECT * FROM post WHERE id = ?"
    GetPostsByAuthorId: str = "SELECT * FROM post WHERE author_id = ?"

__all__ = ["PostQueries"]