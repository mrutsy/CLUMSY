import os
import platform
import sys
import codecs
import logging
import copy


class SO(object):
    def __init__(self):
        self.platform_uname = platform.uname()

    def _system(self):
        return self.platform_uname.system

    def _node(self):
        return self.platform_uname.node

    def package_manager(self):
        if self._node() == "fedora":
            return "dnf"
        elif self._node() == "ubuntu":
            return "apt"
        elif self._node() == "debian":
            return "dpkg"
        elif self._node() == "manjaro":
            return "pacman"
        else:
            exit("HZ SYSTEM")

    def package_install(self):
        os.system(self.package_manager() + " install git")


if __name__ == "__main__":
    pass
# print(SO().package_install())
