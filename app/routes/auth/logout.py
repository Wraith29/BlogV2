__all__ = ['logout_bp']
from flask import Blueprint, Response, session
from app.utilities import flash_and_redirect

logout_bp = Blueprint('logout', __name__, url_prefix='/logout')


@logout_bp.get('/')
def logout() -> tuple[Response, int]:
    try:
        session.pop('current_user')
    except KeyError:
        return flash_and_redirect(('Not Logged In', 'info'), 'auth.login.view')
    return flash_and_redirect(('Logged out', 'info'), 'auth.login.view')
