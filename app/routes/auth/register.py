from typing import Tuple
from flask import Blueprint, Response, flash, jsonify, redirect, render_template, request, url_for

from app.db import get_db
from app.queries.user import UserQueries


register_bp = Blueprint('register', __name__, url_prefix='/register')

@register_bp.route('/', methods=['GET'])
def view() -> Tuple[str, int]:
    return render_template('auth/register.html', action_route="auth/register/register"), 200

@register_bp.route('/register', methods=['POST'])
def register() -> Response:
    db = get_db()
    form = request.form
    user_exists = db.execute(UserQueries.GetUserByUsername, form['username']).fetchone()

    if user_exists:
        flash("Username Taken", "error")
        return redirect(url_for('auth.login.view'))

    # TODO: add register stuff
    return redirect(url_for('view.home.home'))

__all__ = ["register_bp"]