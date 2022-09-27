from src.libs.system.logger import *
import os


class FileSystem(object):

    def __init__(self, *selected_path):
        self.path = os.path.join(*selected_path)

    def mkdir(self):
        try:
            os.mkdir(self.path)
        except Exception as Error:
            Logger(Error, Error.args).error()
            return False
        else:
            Logger("OK", self.path).success()
            return True


if __name__ == "__main__":
    pass
