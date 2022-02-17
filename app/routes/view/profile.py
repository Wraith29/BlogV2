from typing import Tuple
from flask import Blueprint, render_template

from app.db import get_db
from app.utilities import get_posts_by_user_id

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

@profile_bp.route('/<int:user_id>', methods=['GET'])
def view(user_id: int) -> Tuple[str, int]:
    posts = get_posts_by_user_id(get_db(), user_id)
    return render_template('view/profile.html', posts=(posts if posts else [])), 200

__all__ = ["profile_bp"]