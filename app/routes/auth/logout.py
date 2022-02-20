from typing import Tuple
from flask import Blueprint, Response, redirect, session, url_for

from app.utilities import flash_and_redirect


logout_bp = Blueprint('logout', __name__, url_prefix='/logout')

@logout_bp.route('/', methods=['GET'])
def logout() -> Tuple[Response, int]:
    try:
        session.pop('current_user')
    except KeyError:
        return flash_and_redirect(('Not Logged In', 'info'), 'auth.login.view', 200)
    return redirect(url_for('auth.login.view')), 200

__all__ =['logout_bp']