import os
import sys


def create_dir(*path):
    if os.path.isdir(os.path.join(*path)):
        return False
    else:
        os.mkdir(os.path.join(*path))
        return True
