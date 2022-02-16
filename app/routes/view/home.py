from typing import Tuple

from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET"])
def home() -> Tuple[str, int]:
    return render_template("view/home.html"), 200

__all__ = ["home_bp"]
