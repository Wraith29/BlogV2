from typing import Tuple
from flask import Blueprint, Response, flash, jsonify, redirect, render_template, request, url_for

from app.db import get_db
from app.queries.user import UserQueries

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=['GET'])
def view() -> Tuple[str, int]:
    return render_template('auth/login.html', action_route="auth/login/login"), 200

@login_bp.route('/login', methods=['POST'])
def login() -> Response:
    db = get_db()
    form = request.form
    user_exists = db.execute(UserQueries.GetUserByUsername, [form['username']]).fetchone()

    if not user_exists:
        flash("User not found", "error")
        return redirect(url_for('auth.register.view')), 301
    
    # TODO: add login stuff
    return redirect(url_for('view.home.home')), 204

__all__ = ['login_bp']