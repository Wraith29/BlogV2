from flask import Blueprint, Response, jsonify

from app.db import get_db
from app.queries import UserQueries
from app.models import User


user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/all', methods=['GET'])
def get_all_users() -> Response:
    db = get_db()
    users = [User(*data) for data in db.execute(UserQueries.GetAllUsers).fetchall()]
    return jsonify({'users': users})

__all__ = ['user_bp']