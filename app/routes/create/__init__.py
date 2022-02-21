from flask import Blueprint


create_bp = Blueprint('create', __name__, url_prefix='/create')

from .post import post_bp
create_bp.register_blueprint(post_bp)

__all__ = ["create_bp"]