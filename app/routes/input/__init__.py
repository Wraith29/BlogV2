from flask import Blueprint


input_bp = Blueprint('input', __name__)

from .post import post_bp
input_bp.register_blueprint(post_bp)

__all__ = ["input_bp"]