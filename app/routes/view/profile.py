__all__ = ["profile_bp"]

from flask import Blueprint, render_template
from app.db import get_db
from app.utilities.fetch import get_posts_by_user_id, get_all_users

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')


@profile_bp.get('/<int:user_id>')
def view(user_id: int) -> tuple[str, int]:
    posts = get_posts_by_user_id(get_db(), user_id)
    return render_template('view/profile.html', posts=posts), 200


@profile_bp.get('/all')
def all() -> tuple[str, int]:
    connection = get_db()
    user_post_map = []
    for user in get_all_users(connection):
        user_post_map.append({
            "user": user,
            "posts": get_posts_by_user_id(connection, user.id)
        })

    return render_template(
        'view/all-profiles.html',
        user_post_map=user_post_map,
        len=len
    ), 200
