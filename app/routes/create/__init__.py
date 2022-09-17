__all__ = ["create_bp"]

from flask import Blueprint
from .post import post_bp

create_bp = Blueprint('create', __name__, url_prefix='/create')
create_bp.register_blueprint(post_bp)
