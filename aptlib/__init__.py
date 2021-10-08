from contextlib import contextmanager
import colorama
from termcolor import colored
import sys


colorama.init()


def print_progress(message, success):
    if success:
        print(colored("[PASS]", 'green'), message, file=sys.stderr)
    else:
        print(colored("[FAIL]", 'white', 'on_red'), message, file=sys.stderr)


@contextmanager
def step(description):
    def success():
        print_progress(description, True)

    def failure():
        print_progress(description, False)
        sys.exit(-1)

    try:
        yield

        success()
    except:
        failure()


def count_commits(start):
    result = 1
    while start.parents != ():
        result += 1
        start = start.parents[0]
    return result