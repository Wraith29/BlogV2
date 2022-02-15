from typing import Tuple
from flask import Blueprint, Response, jsonify, render_template


register_bp = Blueprint('register', __name__, url_prefix='/register')

@register_bp.route('/', methods=['GET'])
def view() -> Tuple[str, int]:
    return render_template('auth/register.html'), 200

@register_bp.route('/register', methods=['POST'])
def register() -> Response:
    return jsonify({'route': '/register'})


__all__ = ["register_bp"]