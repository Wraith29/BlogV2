from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

from .login import login_bp
auth_bp.register_blueprint(login_bp)

from .register import register_bp
auth_bp.register_blueprint(register_bp)

__all__ = ["auth_bp"]
