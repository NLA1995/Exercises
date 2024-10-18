from functools import wraps
from contextlib import ContextDecorator


class ContextManager_Manual:
    """Implementing __call__ function from scratch."""

    def __enter__(self):
        print('Printing BEFORE')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Printing AFTER')

    def __call__(self, f):
        print(f)
        @wraps(f)
        def decorated(*args, **kwds):
            with self:
                return f(*args, **kwds)
        return decorated


class ContextManager_Inheritance(ContextDecorator):
    """Using base class inheritance."""

    def __enter__(self):
        print('Printing BEFORE')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Printing AFTER')


def function_decorator(f):
    """
    Implementing a decorator using a function, instead of a class.
    f(function): This the original function that we are wrapping with the decorator.

    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        """This function is the wrapper itself that will contain the original function."""

        # Do something before
        print('Print BEFORE')

        # Call the original function
        f(*args, **kwargs)

        # Do something after
        print('Print AFTER')

    return wrapper


def non_wrapper_decorator(*args, **kwargs):
    """Example of a function decorator without a nested wrapper function"""

    print("ARGS:", args)
    print("KWARGS", kwargs)

    # Args is a tuple, and the first item in the tuple is the decorated function
    # so we capture that, and return it to be called by Python
    decorated_function = args[0]
    return decorated_function


@function_decorator
def ejemplo(nombre):
    print(f'Hola {nombre}')


ejemplo('Natalia')

