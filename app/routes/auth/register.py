from typing import Tuple

from flask import (Blueprint,Response ,redirect,
                    render_template, request, url_for)
from werkzeug.security import generate_password_hash

from app.db import get_db
from app.models import User
from app.utilities import flash_and_redirect, get_user_by_username, is_valid_username

register_bp = Blueprint("register", __name__, url_prefix="/register")

@register_bp.route("/", methods=["GET"])
def view() -> Tuple[str, int]:
    return (
        render_template("auth/register.html", action_route="/auth/register/register"),
        200
    )

@register_bp.route("/register", methods=["POST"])
def register() -> Tuple[Response, int]:
    user_exists = get_user_by_username(get_db(), request.form)
    if user_exists:
        return flash_and_redirect(('Username Taken', 'error'), 'auth.login.view', 301)

    if not is_valid_username(request.form['username']):
        return flash_and_redirect(('Invalid Username', 'error'), 'auth.register.view', 301)
    
    new_user = User(None, request.form['username'], generate_password_hash(request.form['password']))

    return redirect(url_for("view.home.home")), 200

__all__ = ["register_bp"]
