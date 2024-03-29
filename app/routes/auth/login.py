__all__ = ["login_bp"]

from flask import (
    Blueprint,
    Response,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from werkzeug.security import check_password_hash
from app.db import get_db
from app.utilities import flash_and_redirect
from app.utilities.fetch import get_user_by_username

login_bp = Blueprint("login", __name__, url_prefix="/login")


@login_bp.get("/")
def view() -> tuple[str, int]:
    return (
        render_template("auth/login.html", action_route="/auth/login/login"),
        200
    )


@login_bp.post("/login")
def login() -> tuple[Response, int]:
    user_exists = get_user_by_username(get_db(), request.form["username"])
    if not user_exists:
        return flash_and_redirect(
            ('User not found', 'danger'),
            'auth.register.view'
        )

    if not check_password_hash(user_exists.password, request.form['password']):
        return flash_and_redirect(
            ('Incorrect username or password', 'danger'),
            'auth.login.view'
        )

    session['current_user'] = user_exists.get_json()
    flash("Logged in", "success")

    return redirect(url_for('view.home.home')), 302
