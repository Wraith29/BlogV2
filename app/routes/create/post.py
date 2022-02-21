from typing import Tuple
from flask import Blueprint, Response, redirect, render_template, url_for


post_bp = Blueprint('post', __name__, url_prefix='/post')

@post_bp.get('/')
def view() -> Tuple[str, int]:
    return render_template('input/post.html'), 200

@post_bp.post('/create')
def create() -> Response:
    return redirect(url_for('view.home.home'))

__all__ = ["post_bp"]