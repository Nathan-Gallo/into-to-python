import os
import sys


def fetch_file(file):
    """Fetch a list of lines from a file.

        Args:
            file: the filepath of a UTF-8 text document.

        Returns:
            A list of strings containing the lines from 
            the document.
    """
    story = open(file, "r")
    print(story.read())


def main(file):
    try:
        fetch_file(file)
    except OSError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main(sys.argv[1])
