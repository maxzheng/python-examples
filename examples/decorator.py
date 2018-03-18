"""
Use decorators to make functions more fun
=============================================================================

A decorator is a wrapper for functions to add additional functionality.

Example Run
-----------------------------------------------------------------------------
$ python3 examples/decorator.py
double: Decorating  <function echo at 0x10a4dab70>
Creating decorator with factor of  3
multiply: Decorating <function mecho at 0x10a4dad90>
Main started
<function echo at 0x10a4daae8>
 Returns whatever we get
double: Wrapper called
hellohello
multiply: Wrapper called
worldworldworld
double: Decorating  <method 'upper' of 'str' objects>
double: Wrapper called
I LOVE PYTHON! I LOVE PYTHON!
Creating decorator with factor of  4
multiply: Decorating <method 'lower' of 'str' objects>
multiply: Wrapper called
don't you? don't you? don't you? don't you?

References
-----------------------------------------------------------------------------
https://www.python.org/dev/peps/pep-0318/
"""

from functools import wraps


def main():
    print('Main started')

    # Shows `echo` instead of `double` thanks to `wraps`
    print(echo)                 # <function echo at ...
    print(echo.__doc__)         # Returns whatever we get

    print(echo('hello'))        # hellohello
    print(mecho('world'))       # worldworldworld

    # We can call decorators instead of using `@` for the same result
    shout = double(str.upper)        # Decorating  <method 'upper' ...
    print(shout('I love Python! '))  # I LOVE PYTHON! I LOVE PYTHON!

    four = multiply(factor=4)(str.lower)    # Decorating <method 'lower' ...
    print(four('DON\'T YOU? '))  # don't you? don't you? don't you? don't you


def double(f):
    """
    Decorator is just a function that returns another function that wraps
    the original function
    """
    print('double: Decorating ', f)

    @wraps(f)
    def decorated(*args, **kwargs):
        print('double: Wrapper called')
        r = f(*args, **kwargs)
        return r * 2

    return decorated


@double
def echo(value):
    """ Returns whatever we get """
    return value


def multiply(factor=1):
    """
    A decorator that returns another decorator -- nested, so it looks more
    complicated but same concept / similar to `double`. It is used when
    there is a need to customize the behavior of the decorator when
    decorating.

    For this, we are allowing the user to specify a custom factor.

    :param int factor: Number of times to multiply
    """
    print('Creating decorator with factor of ', factor)

    # This is the same code as `double` except the return: r * factor
    def decorator(f):
        print('multiply: Decorating', f)

        @wraps(f)
        def decorated(*args, **kwargs):
            print('multiply: Wrapper called')
            r = f(*args, **kwargs)
            return r * factor

        return decorated

    return decorator


@multiply(factor=3)
def mecho(value):
    return value


if __name__ == "__main__":
    main()
