__all__ = ["is_valid_username", "is_logged_in", "flash_and_redirect"]

import string
from flask import Response, flash, redirect, session, url_for
import werkzeug


def is_valid_username(username: str) -> bool:
    for c in username:
        if c not in [*string.ascii_letters, *string.digits, '_']:
            return False
    return True


def is_logged_in() -> bool:
    return 'current_user' in session


def flash_and_redirect(
    flash_details: tuple[str, str], redirect_route: str
) -> tuple[Response | werkzeug.Response, int]:
    flash(*flash_details)
    return redirect(url_for(redirect_route)), 302
