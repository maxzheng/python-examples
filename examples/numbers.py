"""
Number Crunching
=============================================================================

Basic operations with numbers.

Example Run
-----------------------------------------------------------------------------
$ python3 numbers.py
2
1
9
...

References
-----------------------------------------------------------------------------
https://docs.python.org/3/tutorial/introduction.html#numbers
"""


def main():
    # Basic operations
    print(1 + 1)    # 2
    print(2 - 1)    # 1
    print(3 * 3)    # 9
    print(4 / 2)    # 2.0
    print(5 / 2)    # 2.5

    # Integer divide
    print(5 // 2)   # 2

    # Modulus
    print(5 % 2)    # 1

    # Multiple operations.
    # Use parenthesis to group the operations is always preferred as that is
    # more readable instead of relying on implicit prcedence order.
    print((1 * 2) + (3 * 4))    # 14
    print((1 + 2) * (3 - 4))    # -3

    # Power
    print(2 ** 3)   # 8


if __name__ == "__main__":
    main()
