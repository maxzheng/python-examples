"""
Files and Directories
=============================================================================

When you need to save data to a local computer, you have to know how to work
with files and directories.

Example Run
-----------------------------------------------------------------------------
Doing everything in a temp dir so it cleans up automatically ...
Hello, stranger!
Welcome to python-exmaples
...

References
-----------------------------------------------------------------------------
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

import os
from pathlib import Path
from tempfile import TemporaryDirectory


def main():
    with TemporaryDirectory() as tmpdir:
        print('Doing everything in a temp dir so it cleans up '
              'automatically after we are done! Temp dir is at', tmpdir)

        # Change to the temp dir
        os.chdir(tmpdir)

        # Let's write a file
        with open('hello.txt', 'w') as fp:
            fp.write('Hello, stranger!\n')
            fp.write('Welcome to python-exmaples')

        # Now, we can read it back.
        with open('hello.txt') as fp:

            # Reads everything
            print(fp.read())

            # Go back to the beginning of the file
            fp.seek(0)

            # Read one line at a time
            for line in fp:
                print(line, end='')  # Line has \n, skip same from print

            # Read a few characters at a time
            fp.seek(0)
            print(fp.read(5))

            # Or just one line
            fp.seek(0)
            print(fp.readline())

        # Using pathlib.Path to create a new dir
        new_dir = Path('.') / 'subdir'
        new_dir.mkdir()

        # Create a new file
        new_file = new_dir / 'world.txt'
        with new_file.open('w') as fp:
            fp.write('Path is pretty cool')

        # Read the file
        with new_file.open() as fp:
            print(fp.read())  # Path is pretty cool

        # Or do it using open works too
        with open(new_file) as fp:
            print(fp.read())

        # List all the files in current dir
        for f in Path.cwd().iterdir():
            print(f)
        """
        /tmp/tmpyjm9e_20/hello.txt
        /tmp/tmpyjm9e_20/subdir
        """

        # Glob for only txt files
        for f in Path.cwd().glob('*.txt'):
            print(f)
        """
        /tmp/tmpyjm9e_20/hello.txt
        """


if __name__ == "__main__":
    main()
