"""
Flow Control and Loops
=============================================================================

Use if/elif/else for flow control and for/while for looping.

Example Run
-----------------------------------------------------------------------------
$ python3 flow_and_loops.py
Everything is true
Number is 10 or higher
Well, hello back!
...


References
-----------------------------------------------------------------------------
https://docs.python.org/3/tutorial/controlflow.html
"""


def main():
    boolean = True
    string = 'hello world'
    number = 10

    # Non-empty / non-zero values generally evaluates to true
    if boolean and number and string:
        print('Everything is true')             # Prints this
    else:
        print('At least one of them is false')

    # For multiple conditions use elif
    # For better readability when there are multiple lines in each
    # block, add a newline before if/elif/else.
    if number < 5:
        print('Number is less than 5')
        print('This is not true')

    elif number < 10:
        print('Number is less than 10')
        print('Not this one either')

    else:
        print('Number is 10 or higher')         # Prints this

        if 'hello' in string:
            print('Well, hello back!')          # And this.

    # Iterate thru string one letter at a time
    for letter in string:
        if letter in 'lo':
            continue

        if letter == ' ':
            break

        print(letter)
    """
    h
    e
    """

    # By item for a list.
    for word in ['hello', 'world']:
        print(word)
    """
    hello
    world
    """

    # By key for a dict.
    for key in {'hello': 'world', 'Python': 'is cool'}:
        print(key)
    """
    hello
    Python
    """

    # Else is run when break doesn't happen
    for obj in [boolean, string, number]:
        if type(obj) == dict:
            break

    else:
        print('Did not break')      # Prints this

    # While loop that runs while the condition is true
    while number >= 1:
        number -= 1

        if number % 2:      # Skip odd numbers
            continue

        print(number)
    """
    8
    6
    4
    2
    0
    """

    # Break works for while too
    while True:
        break
        print('Never gonna happen')


if __name__ == "__main__":
    main()
