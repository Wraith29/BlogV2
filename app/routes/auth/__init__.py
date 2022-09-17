__all__ = ["auth_bp"]

from flask import Blueprint
from .login import login_bp
from .register import register_bp
from .logout import logout_bp

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_bp.register_blueprint(login_bp)
auth_bp.register_blueprint(register_bp)
auth_bp.register_blueprint(logout_bp)
