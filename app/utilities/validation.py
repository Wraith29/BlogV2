from functools import wraps
import typing as t

from flask import Response, session

from . import flash_and_redirect

class ValidationError(BaseException):
    """"""

T = t.TypeVar("T")

def login_required(fn: t.Callable[..., T]) -> t.Callable[..., t.Union[T, t.Tuple[Response, int]]]:
    """Will redirect the user to the login page if they are not logged in"""
    @wraps(fn)
    def inner(*args: t.Any) -> t.Union[T, t.Tuple[Response, int]]:
        if 'current_user' not in session:
            return flash_and_redirect(('You must be logged in to do that', 'error'), 'auth.login.view')
        return fn(*args)
    return inner

__all__ = ["login_required"]