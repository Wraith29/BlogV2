import typing as t
import string

from flask import Response, flash, redirect, session, url_for

def is_valid_username(username: str) -> bool:
    for c in username:
        if c not in [*string.ascii_letters, *string.digits]:
            return False
    return True 

def is_logged_in() -> bool:
    return 'current_user' in session

def flash_and_redirect(flash_details: t.Tuple[str, str], redirect_route: str) -> t.Tuple[Response, int]:
    flash(*flash_details)
    return redirect(url_for(redirect_route)), 302

__all__ = [
    "is_valid_username",
    "flash_and_redirect"
]