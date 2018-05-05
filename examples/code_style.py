"""
PEP8+ code style for better code
=============================================================================

PEP8 is the defacto standard for coding style for Python. Code conforming to
that is fairly readable, but some cases could be better. From experience,
I have learned additional guidelines to improve code readability and
robustness, hence PEP8+.

To ensure conformity to PEP8, flake8 can be used to check. The additional
guidelines would need to be checked manually.

This non-working program demonstrates many PEP8 styles along with the
additional guidelines.

References
-----------------------------------------------------------------------------
PEP8: https://www.python.org/dev/peps/pep-0008/
flake8: http://flake8.pycqa.org/en/latest/
"""

# Standard libraries. Imports should be sorted in alphabetical order.
import logging
import random

# 3rd-party libraries
from mysql import FakeDBConnection

# Local libraries
from mycompany.models import DataTable

log = logging.getLogger(__name__)
CONSTANTS = 'can be listed here too'


def main():
    # GUIDELINE #1: Use new string format
    # -----------------------------------------------------------------------
    # String formatting should use f-string or .format() instead of %
    # as % substitute is not as flexible and may become deprecated in the
    # future. See https://www.python.org/dev/peps/pep-3101/
    hello = 'hello {}'.format('world')
    greeting = f'{hello}, how are you'

    # The only place where %s is used would be methods that accept them
    # natively, which may have performance improvements. E.g. logging
    # module would skip string formatting if the log level is higher.
    log.debug('This %s formatting does not happen for INFO level', greeting)

    # GUIDELINE #2: Separate/group logic blocks
    # -----------------------------------------------------------------------
    # For `if` blocks, add an extra blank line to group each block to improve
    # readability.
    if len(hello) < 1:
        print('nothing')
        print('was')
        print('said')

    elif len(hello) < 5:
        print('quick hello')

    else:
        print('long')
        print('greeting')

    # Same for `try/except` blocks.
    try:
        1/0

    except Exception:
        log.info('Yep, that happened')

    # GUIDELINE #3: Use bare except with care
    # -----------------------------------------------------------------------
    # While we are talking about exceptions, never use bare except without
    # re-throwing. Generally, it should not be used unless there is a need to
    # handle system exceptions, such as SystemExit, to rollback a database
    # transaction. See https://docs.python.org/2/howto/doanddont.html#except
    db = FakeDBConnection()
    try:
        db.insert(DataTable, [])
        db.update(DataTable, column1='new value')
        db.commit()

    except:     # noqa
        db.rollback()

        raise  # Always re-raise bare except so system exceptions are handled

    # GUIDELINE #4: Separate/group related code
    # -----------------------------------------------------------------------
    # Related/similar stuff should be separated by blank line for readability
    hello = 1
    world = 2
    hello_world = hello / world

    print(f'{hello} + {world} = ', 3)
    print(f'{hello} / {world} = {hello_world}')

    # GUIDELINE #5: Use parenthesis instead of backward slash
    # -----------------------------------------------------------------------
    # Parenthesis is more readable than backward slash that appears at the
    # end of each line.
    if (hello > world and
            world > hello_world):
        print('This is not so '
              'bad, right?')

    else:
        print('No backward slash used')


class Superhero:
    """ A hero with superpowers.  """

    #: This is a class level constant
    CLASS_LEVEL_CONSTANT = True

    def __init__(self, powers):
        """
        Initialize the superhero with powers.

        :param list[str] powers: List of superpowers. It's possible to
                                 use type hints in Python 3, but the
                                 readability isn't great for optional
                                 args with default values, so *I* prefer
                                 to continue documenting them via
                                 docstrings.
        """
        #: List of superpowers.
        self.powers = powers

        # Hidden power that no one knows about
        self._hidden_power = 'glow in the dark'

    def fight(self):
        """ Fight villian using one of the superpowers """
        print(random.choice(self.powers))

        if random.random() > 0.99:
            print(self._hidden_power)


if __name__ == "__main__":
    main()
