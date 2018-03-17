import re

from examples.understanding_async import main


def test_understanding_async(capsys):
    main()

    captured = capsys.readouterr()
    assert re.fullmatch('<function coro_alpha.*Alpha started.*Beta started.*'
                        'Flash.*Beta finished.*Alpha finished.*'
                        'from Beta: gift\nAll done!\n', captured.out,
                        flags=re.MULTILINE | re.DOTALL)
