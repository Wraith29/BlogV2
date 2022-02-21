import json
import typing as t

from flask import Blueprint, Response, flash, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash

from app.db import get_db
from app.models import User
from app.utilities import is_valid_username, flash_and_redirect
from app.utilities.creation import create_user
from app.utilities.fetch import get_user_by_username, get_user_by_id

register_bp = Blueprint("register", __name__, url_prefix="/register")


@register_bp.get("/")
def view() -> t.Tuple[str, int]:
    return render_template("auth/register.html", action_route="/auth/register/register"), 200


@register_bp.post("/register")
def register() -> t.Tuple[Response, int]:
    user_exists = get_user_by_username(get_db(), request.form)
    if user_exists:
        return flash_and_redirect(('Username Taken', 'error'), 'auth.login.view')
    if not is_valid_username(request.form['username']):
        return flash_and_redirect(('Invalid Username', 'error'), 'auth.register.view')

    new_user = User(None, request.form['username'], generate_password_hash(request.form['password']))

    id = create_user(get_db(), new_user)
    user = get_user_by_id(get_db(), id)
    if not user:
        return flash_and_redirect(("There was an with logging you in.", "error"), "auth.login.view")

    session['current_user'] = json.dumps(user.get_json())
    flash("Logged in", 'success')
    return redirect(url_for("view.home.home")), 302


__all__ = ["register_bp"]
