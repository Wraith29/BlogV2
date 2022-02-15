from flask import Blueprint


data_bp = Blueprint('data', __name__, url_prefix='/data')

from .user import user_bp
data_bp.register_blueprint(user_bp)

__all__ = ["data_bp"]