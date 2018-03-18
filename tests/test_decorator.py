import re
from examples.decorator import main, echo, mecho


def test_echo():
    assert echo('hello') == 'hellohello'


def test_mecho():
    assert mecho(2) == 6


def test_main(capsys):
    main()

    captured = capsys.readouterr()
    assert re.fullmatch('Main started.*don\'t you?.*',
                        captured.out,
                        flags=re.MULTILINE | re.DOTALL)
