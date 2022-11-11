from functools import wraps
from typing import Callable, Any


def check_is_zero(func: Callable) -> Callable:
    """Check element in args is not equals zero"""

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args[1] == 0:
            raise ZeroDivisionError('You can not divide by zero')
        return func(*args, **kwargs)

    return wrapper
