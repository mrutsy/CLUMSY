import os
import platform
import sys
import codecs
import logging
import copy


class SO(object):
    def __init__(self):
        self.platform_uname = platform.uname()

    def system(self):
        return self.platform_uname.system

    def node(self):
        return self.platform_uname.node

    def package_manager(self):
        if self.node() == "fedora":
            return "dnf"
        elif self.node() == "ubuntu":
            return "apt"
        elif self.node() == "debian":
            return "dpkg"
        elif self.node() == "manjaro":
            return "pacman"
        else:
            exit("HZ SYSTEM")

    def package_install(self):
        os.system(self.package_manager() + " install git")


if __name__ == "__main__":
    pass
# print(SO().package_install())
