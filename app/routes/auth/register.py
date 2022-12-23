__all__ = ["register_bp"]

from flask import (
    Blueprint,
    Response,
    flash,
    redirect,
    render_template,
    request,
    url_for
)
from werkzeug.security import generate_password_hash
from app.db import get_db
from app.models import User
from app.utilities import is_valid_username, flash_and_redirect
from app.utilities.creation import create_user
from app.utilities.fetch import get_user_by_username

register_bp = Blueprint("register", __name__, url_prefix="/register")


@register_bp.get("/")
def view() -> tuple[str, int]:
    return render_template(
        "auth/register.html",
        action_route="/auth/register/register"
    ), 200


@register_bp.post("/register")
def register() -> tuple[Response, int]:
    user_exists = get_user_by_username(get_db(), request.form["username"])
    if user_exists:
        return flash_and_redirect(
            ('Username Taken', 'danger'),
            'auth.login.view'
        )

    if not is_valid_username(request.form['username']):
        return flash_and_redirect(
            ('Invalid Username', 'danger'),
            'auth.register.view'
        )

    new_user = User(
        0,
        request.form['username'],
        generate_password_hash(request.form['password'])
    )

    create_user(get_db(), new_user)
    flash('Account Created', 'success')
    return redirect(url_for('auth.login.view')), 302
