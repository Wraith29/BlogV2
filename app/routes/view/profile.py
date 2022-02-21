import typing as t

from flask import Blueprint, render_template

from app.db import get_db
from app.utilities.fetch import get_posts_by_user_id, get_all_users

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

@profile_bp.get('/<int:user_id>')
def view(user_id: int) -> t.Tuple[str, int]:
    posts = get_posts_by_user_id(get_db(), user_id)
    return render_template('view/profile.html', posts=posts), 200

@profile_bp.get('/all')
def all() -> t.Tuple[str, int]:
    users = get_all_users(get_db())
    return render_template('view/all-profiles.html', users=users, get_db=get_db), 200

__all__ = ["profile_bp"]
