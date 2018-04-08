"""
String Manipulation
=============================================================================

Common operations for working with string. There are many things you can do,
see References below. As they act like an array of characters, many list
operations also work as well.

Example Run
-----------------------------------------------------------------------------
$ python3 sring.py
This is a literal string
Single quote works exactly the same
It join using space between them
...

References
-----------------------------------------------------------------------------
https://docs.python.org/3/library/string.html
"""


def main():
    """
    This is a docstring that lets 3rd party tools to generate
    documentation for "main" function
    """

    print("This is a literal string")
    print('Single quote works exactly the same')
    print('It ' 'join ' 'using space between them')
    print('If placed into a parenthesis, '
          'it can join multiple lines')
    print("""Or use trible quotes
for multiline
works too!""")

    #: A docstring for an attribute. Notice the colon after hash.
    hello = 'hello world'
    print(hello)            # hello world

    # index starts with 0 from the left, or -1 from the right.
    print(hello[0])         # h
    print(hello[-1])        # d
    print(hello[0:5])       # hello
    print(hello[-5:-1])     # worl
    print(hello[0:5:2])     # hlo

    hello_copy = hello[:]
    print(hello_copy)       # hello world
    print(hello[::-1])      # dlrow olleh

    hello, world = hello.split()    # Split by any length of space.
    print(hello, world)             # hello world

    print('It can contain\tcontrol chars')      # ... contain       control..

    # prints \t as \t without translation as it is a raw string.- "r" prefix
    print(r'prefix with r to print\tas a raw string')  # ... print\tas...

    print('Format using positions: {} {}'.format(hello, world))
    """ ...: hello world """

    print('Format using names: {w} {h}'.format(h=hello, w=world))
    """ ...: world hello"""

    print(f'Format using f-string: {hello} {world}')
    """ ...: hello world"""

    print('Float with 2 decimals: {:.2f}'.format(1.2345))  # 1.23

    # Iterate thru each letter
    for letter in hello:
        print(letter)
    """
    h
    e
    l
    l
    o
    """

    print(len(hello))       # 5

    united = hello + ' one ' + world
    print(united)           # hello one world

    print('one' in united)  # True


if __name__ == "__main__":
    main()
