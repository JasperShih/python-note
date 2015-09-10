# -*- coding: utf8 -*-
from contextlib import contextmanager
import os


@contextmanager
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)

    # return "123"
    try:
        yield  # !

    # except:

    finally:
        os.chdir(current_dir)


with working_directory("data/stuff"):
    pass
    # do something within data/stuff
# here I am back again in the original working director

"""執行with working_directory("data/stuff"):時
會先執行
def working_directory(path):
    current_dir = os.getcwd()
    os.chdir(path)

    # return "123"
    try:
而到了 yield
才會回去執行pass部分
pass執行完後,再去執行
    #except:

    finally:
        os.chdir(current_dir)
部分
"""
