__all__ = ["home_bp"]

from flask import Blueprint, render_template
from app.db import get_db
from app.utilities.fetch import get_all_posts, get_all_users

home_bp = Blueprint("home", __name__)


@home_bp.get("/")
def home() -> tuple[str, int]:
    posts = get_all_posts(get_db())
    users = get_all_users(get_db())
    return render_template("view/home.html", posts=posts, users=users), 200
