from typing import Tuple

from flask import Blueprint, render_template, session, flash

home_bp = Blueprint("home", __name__)

@home_bp.get("/")
def home() -> Tuple[str, int]:
    return render_template("view/home.html", session=session), 200

__all__ = ["home_bp"]
