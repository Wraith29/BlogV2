import typing as t

from flask import Blueprint, Response, redirect, render_template, request, session, url_for

from app.db import get_db
from app.models import Post
from app.utilities.creation import create_post
from app.utilities.validation import login_required

post_bp = Blueprint('post', __name__, url_prefix='/post')

@post_bp.get('/')
@login_required
def view() -> t.Tuple[str, int]:
    return render_template('input/post.html'), 200

@post_bp.post('/create')
@login_required
def create() -> Response:
    new_post = Post(None, request.form['title'], request.form['body'], session['current_user'].id)
    create_post(get_db(), new_post)
    return redirect(url_for('view.home.home'))

__all__ = ["post_bp"]