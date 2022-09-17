__all__ = ["login_required"]

from functools import wraps
from typing import TypeVar, Callable, Any
from flask import Response, session
from . import flash_and_redirect


class ValidationError(BaseException):
    """"""


T = TypeVar("T")


def login_required(
    fn: Callable[..., T]
) -> Callable[..., T | tuple[Response, int]]:
    """Will redirect the user to the login page if they are not logged in"""
    @wraps(fn)
    def inner(*args: Any) -> T | tuple[Response, int]:
        if 'current_user' not in session:
            return flash_and_redirect(
                ('You must be logged in to do that', 'error'),
                'auth.login.view'
            )
        return fn(*args)
    return inner
