from flask import Blueprint

view_bp = Blueprint("view", __name__)

from .home import home_bp
view_bp.register_blueprint(home_bp)

from .profile import profile_bp
view_bp.register_blueprint(profile_bp)

__all__ = ["view_bp"]
