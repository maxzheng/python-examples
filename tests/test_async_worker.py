import re
from examples.async_worker import main, AsyncManager


def test_async_worker(capsys):
    AsyncManager._TASK_DURATION = 0.001
    main()

    captured = capsys.readouterr()
    assert re.fullmatch('\[0 running tasks].*Running "Task 1".*Done with Task 0 after 0.003 seconds!\n', captured.out,
                        flags=re.MULTILINE | re.DOTALL)
