__all__ = ["view_bp"]

from flask import Blueprint
from .home import home_bp
from .profile import profile_bp

view_bp = Blueprint("view", __name__)
view_bp.register_blueprint(home_bp)
view_bp.register_blueprint(profile_bp)
