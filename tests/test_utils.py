from time import sleep
from examples.utils import show_duration


def test_duration(capsys):
    with show_duration('quick task'):
        sleep(0.01)
    out, err = capsys.readouterr()
    assert out == 'quick task took 0.01 seconds\n'
