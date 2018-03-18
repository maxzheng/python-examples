import re
from examples.decorator import main


def test_decorator(capsys):
    main()

    captured = capsys.readouterr()
    assert re.fullmatch('Main started.*',
                        captured.out,
                        flags=re.MULTILINE | re.DOTALL)
