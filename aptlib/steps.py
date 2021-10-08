import aptlib
import os
import git


def file_must_exist(path):
    with aptlib.step(f'Looking for file {path}'):
        assert os.path.isfile(path)


def directory_must_exist(path):
    with aptlib.step(f'Looking for directory {path}'):
        assert os.path.isdir(path)


def open_git_repository(path):
    with aptlib.step(f'Opening repo at {path}'):
        return git.Repo(path)


def read_file_contents(path):
    file_must_exist(path)

    with aptlib.step(f'Reading contents of {path}'):
        with open(path) as f:
            return f.read()
