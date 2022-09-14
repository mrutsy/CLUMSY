import subprocess


class Docker(object):

    def __init__(self):
        self.current_version = None

    def check_current_version(self):

        output = str(subprocess.check_output("dc -v", shell=True).rstrip()).replace("b'", "").replace(",", "")\
            .split(" ")

        if output[0] == "Docker":
            self.current_version = output[2]
        else:
            self.current_version = None

        return self.current_version

    def install_on_fedora(self):
        pass


class Compose(object):
    def __init__(self):
        self.current_version = None

    def check_current_version(self):

        output = str(subprocess.check_output("dc-compose -v", shell=True).rstrip()).replace("b'", "")\
            .replace(",", "").split(" ")

        if output[0] == "dc-compose":
            self.current_version = output[2]
        else:
            self.current_version = None

        return self.current_version
